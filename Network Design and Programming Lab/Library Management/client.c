#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>
#include<sys/socket.h>
#include<sys/types.h>
#include<netinet/in.h>
#define MAXSIZE 100

main()
{
	char buff[MAXSIZE];
	int sockfd,retval,i;
	int recedbytes,sentbytes;
	struct sockaddr_in serveraddr;
	sockfd=socket(AF_INET,SOCK_STREAM,0);
	if(sockfd==-1)
	{
		printf("\nSocket Creation Error");
		return;
	}

	serveraddr.sin_family=AF_INET;
	serveraddr.sin_port=htons(8080);
	serveraddr.sin_addr.s_addr=inet_addr("127.0.0.1");
	retval=connect(sockfd,(struct sockaddr*)&serveraddr,sizeof(serveraddr));
	if(retval==-1)
	{
		printf("Connection error");
		return;
	}

	char arr[MAXSIZE], name[MAXSIZE];

	while(1){
		//int condition;
        printf("What would you like to do?\n1.Insert Book\n2.Update Book Genre\n3.Search for a Book\n4.Exit\n5.get details server side\n");
        int condition, value[MAXSIZE];
        scanf("%d",&condition);
        fflush(stdin);
        value[0] = condition;
        send(sockfd, value, sizeof(value),0);
        switch(condition){
            case 1:{
                recv(sockfd, arr, sizeof(arr), 0);
                printf("%s",arr);
                fflush(stdin);
                scanf(" %99[^\n]", name);
                send(sockfd, name, sizeof(name), 0);
                recv(sockfd, arr, sizeof(arr), 0);
                printf("%s",arr);
                fflush(stdin);
                scanf(" %99[^\n]", name);
                send(sockfd, name, sizeof(name), 0);
                recv(sockfd, arr, sizeof(arr), 0);
                printf("%s",arr);
                fflush(stdin);
                scanf(" %99[^\n]", name);
                send(sockfd, name, sizeof(name), 0);
                recv(sockfd, arr, sizeof(arr), 0);
                printf("%s",arr);
                fflush(stdin);
                scanf(" %99[^\n]", name);
                send(sockfd, name, sizeof(name), 0);

                recv(sockfd, arr, sizeof(arr), 0);
                printf("%s",arr);
                break;
            }
            case 2:{
                recv(sockfd, arr, sizeof(arr), 0);
                printf("%s",arr);
                fflush(stdin);
                scanf(" %99[^\n]", name);
                send(sockfd, name, sizeof(name), 0);
                recv(sockfd, arr, sizeof(arr), 0);
                printf("%s",arr);
                fflush(stdin);
                scanf(" %99[^\n]", name);
                send(sockfd, name, sizeof(name), 0);
                
                recv(sockfd, arr, sizeof(arr), 0);
                printf("%s",arr);
                break;
            }
            case 3:{
                recv(sockfd, arr, sizeof(arr), 0);
                printf("%s",arr);
                fflush(stdin);
                scanf(" %99[^\n]", name);
                send(sockfd, name, sizeof(name), 0);
                
                recv(sockfd, arr, sizeof(arr), 0);
                printf("%s",arr);
                break;
            }
            case 4:{
                send(sockfd, "bye", sizeof("bye"), 0);
                close(sockfd);
                exit(0);
            }
            case 5:{
                break;
            }
            default:
                printf("INVALID");

        };
	}
	close(sockfd);
}