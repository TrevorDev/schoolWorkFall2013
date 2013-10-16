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
    write(fd, message, strlen(message));
    close(fd);
}

char * getMessage(char * link){
	int fd=-1;
    char * message = (char *)calloc(MAX_BUF, sizeof(char));
    while(fd==-1){
        fd = open(link, O_RDONLY);
    }
    read(fd, message, sizeof(char)*MAX_BUF);
    close(fd);
    return message;
}

void makeNode(char * name, char * parent, char * children[], int size){
    
    int running = 1;
    makePipes(children, size);
    while(running){
        char * message = getMessage(parent);
        printf("%s, message %s received\n", name, message);
        if(children!=NULL){
            for(int i=0;i<size;i++){
                sendMessage(message, children[i]);
            }
            for(int i=0;i<size;i++){
                char * recMessage = getMessage(children[i]);
                //printf("%s, received %s from %s\n",name,recMessage,children[i]);
                free(recMessage);
            }
        }
        sendMessage(message, parent);
        if(strcmp(message, "q")==0){
            running=0;
        }
        free(message);
    }
    deletePipes(children, size);
    
}