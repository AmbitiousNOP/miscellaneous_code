// usage: showip <hostname>
#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <netinet/in.h>

int main(int argc, char *argv[])
{
    struct addrinfo hints, *response, *next;
    int status;
    char ipstr[INET6_ADDRSTRLEN];

    if (argc != 2){
        fprintf(stderr, "usage: showip hostname\n");
    }

    memset(&hints, 0, sizeof(hints));

    hints.ai_family = AF_UNSPEC;    // means AF_INET or AF_INET6 is accepted
    hints.ai_socktype = SOCK_STREAM;    //TCP

    if ((status = getaddrinfo(argv[1], NULL, &hints, &response)) != 0){
        fprintf(stderr, "getaddrinfo: %s\n", gai_strerror(status));
    }

    printf("Finding IP Address Of: %s:\n\n", argv[1]);

    for (next = response; next != NULL; next = next->ai_next){
        void *addr;
        char *ipver;

        //get the point to address itself.
        //different fields in IPv4 and IPv6
        if (next->ai_family == AF_INET){ //ipv4
            struct sockaddr_in *ipv4 = (struct sockaddr_in *)next->ai_addr;
            addr = &(ipv4->sin_addr);
            ipver = "IPv4";
        }else { //ipv6
            struct sockaddr_in6 *ipv6 = (struct sockaddr_in6 *)next->ai_addr;
            addr = &(ipv6->sin6_addr);
            ipver = "IPv6";
        }

        //conver ip to a string and print it
        inet_ntop(next->ai_family, addr, ipstr, sizeof(ipstr));
        printf(" %s: %s\n", ipver, ipstr);
    }

    freeaddrinfo(response); //free the linked list

    return 0;

}