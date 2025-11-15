/*
** client.c -- a stream socket client demo

All this program does is connect to a given host and accept the string "hello word" over a stream connection.
All you need to do to test this server is run it in one window, and netcat to it from
another with:
    nc remotehostname 3490
where remotehostname is the name of the machine you're connecting to.
*/


// init socket lib
#include <stdio.h> //input output
#include <sys/socket.h> //socket 
#include <netdb.h> //getaddrinfo()
#include <string.h> //memset()
#include <errno.h> //errno
#include <unistd.h> //close()

// usage: ./client <host> <port>
int main(int argc, char *argv[]){
    // handle improper argument error
    if (argc != 3){
        fprintf(stderr, "[-] USAGE: ./client <hostname> <port>\n");
    }

    // define struct for getaddrinfo()
    struct addrinfo hints, *response, *next;
    // set hints memory to 0's
    memset(&hints, 0, sizeof(hints));

    int status;
    // call getaddrinfo
    if ((status = getaddrinfo(argv[1], argv[2], &hints, &response)) != 0){
        fprintf(stderr, "[-] Getaddr() error: %s\n", gai_strerror(status));
    }

    // creating a socket
    int socket_fd;
    // loop over the linked list returned by getaddrinfo() and try to get a socket.
    for (next = response; next != NULL; next = next->ai_next){
        if ((socket_fd = socket(next->ai_family, next->ai_socktype, next->ai_protocol)) == -1){
            fprintf(stderr, "[-] Socket Creation Error:%s\n", strerror(errno));
            close(socket_fd);
        }else{
            printf("[+] Socket Successfully created\n");
            // connect to the server
            if ((connect(socket_fd, next->ai_addr, next->ai_addrlen)) != -1){
                printf("[+] Connection Successfully made\n");
                break;
            }else{
                fprintf(stderr, "[-] Connection Failed:%s\n", strerror(errno));
                close(socket_fd);
            }
        }
        if (next == NULL){
            printf("[-] Socket Creation Error: Ran out of addrs");
        }
    }

    // free mem... no longer needed after socket creation
    freeaddrinfo(response);

    // communicate with the server
    //Hello world!\n + \0
    char data[14];
    ssize_t bytes_received;
    if ((bytes_received = recv(socket_fd, data, 14, 0)) == -1){
        fprintf(stderr, "Error recieveing data:%s\n", strerror(errno));
    }else{
        printf("[+] Successfully recieved data\n");
    }

    //append null terminated character (\0) to end of data since recv() does not.
    // check if data size is 1 less than max size (14). 
    if (bytes_received < 14){
        data[bytes_received] = '\0';
        // print data to terminal
        printf("[+] Recieved Following Message: %s\n", data);
    }else{
        printf("[-] NOT ALL EXPECTED DATA RECIEVED\n");
    }

    // close the connection
    close(socket_fd);
    


}


