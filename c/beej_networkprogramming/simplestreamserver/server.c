/* 
** server.c -- a stream socket server demo

All this server does is send the string "hello word" out over a stream connection.
All you need to do to test this server is run it in one window, and telnet to it from
another with:
    telent remotehostname 3490
where remotehostname is the name of the machine you're running it on.
*/

#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>
#include <signal.h>
#include <arpa/inet.h>

#define LISTEN_PORT "3494"
#define BACKLOG 10

volatile sig_atomic_t keep_running = 1;

void signal_handler(int s){
    keep_running = 0;
}

int main(){
    int status; 
    int sockfd;
    // init the server
    struct addrinfo hints, *serverinfo, *next; 
    struct sigaction sig;

    // init signal catch
    memset(&sig, 0, sizeof(sig));
    sigemptyset(&sig.sa_mask);
    sig.sa_handler = signal_handler;
    sigaction(SIGINT, &sig, NULL);

    memset(&hints, 0, sizeof(hints));
    hints.ai_flags = AI_PASSIVE;
    hints.ai_family = AF_INET; // only ipv4
    hints.ai_socktype = SOCK_STREAM;

    if ((status = getaddrinfo(NULL, LISTEN_PORT, &hints, &serverinfo)) != 0){
        fprintf(stderr, "[-] getaddrinfo error: %s\n", gai_strerror(status));
        return 1;
    }

    // loop over the linked list returned by getaddrinfo. 
    // attempt to create a socket and when successful create a bind.
    for (next = serverinfo; next != NULL; next = next->ai_next){
        if (next == NULL){
            fprintf(stderr, "[-] Socket creation ran out of values %s\n", strerror(errno));
            return 1;
        }
        sockfd = socket(next->ai_family, next->ai_socktype, next->ai_protocol);
        if (sockfd == -1){ // socket creation errored out
            fprintf(stderr, "[-] Socket creation error: %s\n", strerror(errno));
        }else{ // socket successfully made
            printf("[+] Socket successfully made\n");
            // bind the server's addr and port with bind()
            if ((bind(sockfd, next->ai_addr, next->ai_addrlen)) == -1){ // bind failed
                fprintf(stderr, "[-] bind error: %s\n", strerror(errno));
                close(sockfd);
            }else{ // bind successful 
                printf("[+] Bind successfully made\n");
                // listen for incoming connections using listen()
                if ((listen(sockfd, BACKLOG)) == -1){ // listen fail
                    fprintf(stderr, " [-] Listening error: %s\n", strerror(errno));
                } else{ // listen success
                    printf("[+] Listening for connections on port: %s\n", LISTEN_PORT);
                    break;
                }
            }
        }
    }


    while(keep_running){
        // accept incoming connections 
        struct sockaddr_storage their_addr;
        int new_fd; 
        void *addr;
        socklen_t addr_size = sizeof(their_addr);
        new_fd = accept(sockfd, (struct sockaddr *)&their_addr, &addr_size);

        // getting the ip addr of the connected host
        if (their_addr.ss_family == AF_INET){ // ipv4
            char ipstr[INET_ADDRSTRLEN];
            struct sockaddr_in *ipv4 = (struct sockaddr_in *)&their_addr;
            inet_ntop(their_addr.ss_family, &(ipv4->sin_addr), ipstr, sizeof(ipstr));
            printf("[+] Connection made: %s:%u\n", ipstr, ntohs(ipv4->sin_port));
        }else{ //ipv6
            char ipstr[INET6_ADDRSTRLEN];
            struct sockaddr_in6 *ipv6 = (struct sockaddr_in6 *)&their_addr;
            inet_ntop(their_addr.ss_family, &(ipv6->sin6_addr), ipstr, sizeof(ipstr));
            printf("[+] Connection made: %s:%u\n", ipstr, ntohs(ipv6->sin6_port));
        }


        if (new_fd == -1){
            if ((errno == EINTR) && (keep_running == 0)){
                break;
            }else{ // error other than signal interupt
                fprintf(stderr, "Accept Error: %s\n", strerror(errno));
                printf("Trying accept again...\n");
                continue;
            }
        } else{
            printf("[+] Accepted connection\n");
        }

        //sending data
        char *msg = "Hello world!\n";
        int len, bytes_sent;

        len = strlen(msg);
        bytes_sent = send(new_fd, msg, len, 0);

        // close the socket
        close(new_fd);
    }

    printf("\n[+] Caught Signal\n");
    printf("[+] Exiting program\n");

    close(sockfd);
    // free mem
    freeaddrinfo(serverinfo);
    return 0;
}
