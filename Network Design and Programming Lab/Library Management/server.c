#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>
#include<sys/socket.h>
#include<sys/types.h>
#include<netinet/in.h>
#define MAXSIZE 100

struct Book
{
    int ID;
    char Name[MAXSIZE];
    char pub[MAXSIZE];
    char auth[MAXSIZE];
    char genre[MAXSIZE];
};

struct Book* getDetails(){
    struct Book *listOfBooks = malloc(MAXSIZE * sizeof(struct Book));

    FILE *ptr;
    ptr = fopen("Database.txt","r");

    fread(listOfBooks, sizeof(struct Book), MAXSIZE, ptr);

    fclose(ptr);
    return listOfBooks;

}

struct Book* insert(char Name[MAXSIZE], char pub[MAXSIZE], char auth[MAXSIZE], char genre[MAXSIZE]){
    struct Book* listofBooks = getDetails();
    
    int i;
    for( i = 0; i < listofBooks[0].ID ; i++);

    struct Book newBook = {i+1, "", "", "", ""};
    strcpy(newBook.Name,Name);
    strcpy(newBook.pub,pub);
    strcpy(newBook.auth,auth);
    strcpy(newBook.genre,genre);

    listofBooks[i] = newBook;
    listofBooks[0].ID += 1;

    FILE* ptr;
    ptr = fopen("Database.txt", "w");

    fwrite(listofBooks, sizeof(struct Book), MAXSIZE, ptr);

    fclose(ptr);
    return listofBooks;

}

struct Book* update(char Name[MAXSIZE], char genre[MAXSIZE]){
    struct Book* listOfBooks = getDetails();

    int i;
    for( i = 0; i < listOfBooks[0].ID ; i++){
        if(strcmp(Name, listOfBooks[i].Name) == 0){
            strcpy(listOfBooks[i].genre,genre);
            break;
        }
    }


    FILE* ptr;
    ptr = fopen("Database.txt", "w");

    fwrite(listOfBooks, sizeof(struct Book), MAXSIZE, ptr);

    fclose(ptr);
    return listOfBooks;

}

int search(char Name[MAXSIZE]){
    struct Book* listOfBooks = getDetails();

    int i;
    for( i = 0; i < listOfBooks[0].ID ; i++){
        if(strcmp(Name, listOfBooks[i].Name) == 0){
            return 1;
        }
    }

    return 0;
}



int main(){
    
    int sockfd,newsockfd,retval,i;
	socklen_t actuallen;
	int recedbytes,sentbytes;
	struct sockaddr_in serveraddr,clientaddr;
	
	int a=0;
	sockfd=socket(AF_INET,SOCK_STREAM,0);

	if(sockfd==-1)
	{
	printf("\nSocket creation error");
	}

	serveraddr.sin_family=AF_INET;
	serveraddr.sin_port=htons(8080);
	serveraddr.sin_addr.s_addr=htons(INADDR_ANY);
	retval=bind(sockfd,(struct sockaddr*)&serveraddr,sizeof(serveraddr));
	if(retval==1)
	{
		printf("\nBinding error");
		close(sockfd);
	}

	retval=listen(sockfd,1);
	if(retval==-1)
	{
	close(sockfd);
	}
	actuallen=sizeof(clientaddr);
	newsockfd=accept(sockfd,(struct sockaddr*)&clientaddr,&actuallen);
	if(newsockfd==-1)
	{
		close(sockfd);
	}

    char name[MAXSIZE], pub[MAXSIZE], genre[MAXSIZE], auth[MAXSIZE];
    int buff[MAXSIZE];


    while(1){
        recv(newsockfd, buff, sizeof(buff), 0);
        int opt = buff[0];

        switch(opt){
            case 1:
                {
                    send(newsockfd, "Enter Name : ", sizeof("Enter Name : "), 0);
                    recv(newsockfd, name, sizeof(name), 0);
                    send(newsockfd, "Enter Publisher : ", sizeof("Enter Publisher : "), 0);
                    recv(newsockfd, pub, sizeof(pub), 0);
                    send(newsockfd, "Enter Author : ", sizeof("Enter Author : "), 0);
                    recv(newsockfd, auth, sizeof(auth), 0);
                    send(newsockfd, "Enter Genre : ", sizeof("Enter Genre : "), 0);
                    recv(newsockfd, genre, sizeof(genre), 0);

                    insert(name,pub,auth,genre);
                    send(newsockfd, "SUCCESSFUL!\n", sizeof("SUCCESSFUL!\n"), 0);
                    break;
            }
            case 2:{
                    send(newsockfd, "Enter Name : ", sizeof("Enter Name : "), 0);
                    recv(newsockfd, name, sizeof(name), 0);
                    send(newsockfd, "Enter Genre : ", sizeof("Enter Genre : "), 0);
                    recv(newsockfd, genre, sizeof(genre), 0);

                    update(name,genre);
                    send(newsockfd, "SUCCESSFUL!\n", sizeof("SUCCESSFUL!\n"), 0);
                    break;
            }
            case 3:{
                    send(newsockfd, "Enter Name : ", sizeof("Enter Name : "), 0);
                    recv(newsockfd, name, sizeof(name), 0);

                    if(search(name) == 1){
                        send(newsockfd, "SUCCESSFUL!\n", sizeof("SUCCESSFUL!\n"), 0);
                    }
                    else{
                        send(newsockfd, "FAILED!\n", sizeof("FAILED!\n"), 0);
                    }
                    break;

            }
            case 4:{
                recv(newsockfd, name, sizeof(name), 0);
                if(strcmp(name,"bye") == 0){
                    close(newsockfd);
                    exit(0);
                }
                break;
            }
            case 5: {
                struct Book* listOfBooks = getDetails();

                for(int i = 1; i <= listOfBooks[0].ID; i++){
                    printf("%s\t%s\n", listOfBooks[i].Name, listOfBooks[i].genre);
                }

                break;
            }
        };
    }
}