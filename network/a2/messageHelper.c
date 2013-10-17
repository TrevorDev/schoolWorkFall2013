#include <fcntl.h>
#include <stdio.h>
#include <sys/stat.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include <time.h>
#include <errno.h>
#include "messageHelper.h"

void makePipes(char * children[], int size){
    if(children!=NULL){
        for(int i=0;i<size;i++){
                mkfifo(children[i], 0666);
                printf("made %s\n", children[i]);
        }
    }
}

void deletePipes(char * children[], int size){
    if(children!=NULL){
        for(int i=0;i<size;i++){
                unlink(children[i]);
        }
    }
}

void sendMessage(char * message, char * link){
	int fd;
    fd = open(link, O_WRONLY);
    write(fd, message, sizeof(char)*strlen(message));
    close(fd);
}

char * getMessage(char * link){
	int fd=-1;
    char * message = (char *)calloc(MAX_BUF, sizeof(char));
    while(fd==-1){
        fd = open(link, O_RDONLY);
    }
    printf("hit1\n");
    fgets(message, MAX_BUF, fd);
    printf("hit\n");
    close(fd);
    return message;
}

void makeNode(char * name, char * parent, char * children[], int size){
    
    int running = 1;
    makePipes(children, size);
    while(running){
        char * message = getMessage(parent);
        printf("%c%c-%c%c-%c\n",message[1],message[2],name[0],name[1],message[0]);
        if(message[1]==name[0]&&message[2]==name[1]){
            //printf("%c\n",message[0]);
        }
        
        
        //sendMessage(message, parent);
        if(strcmp(message, "q")==0){
            running=0;
        }
        free(message);
    }
    deletePipes(children, size);
    
}