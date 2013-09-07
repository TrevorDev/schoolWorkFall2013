#include <fcntl.h>
#include <stdio.h>
#include <sys/stat.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include "messageHelper.h"

void sendMessage(char * message, char * link){
	int fd;

    mkfifo(link, 0666);

    fd = open(link, O_WRONLY);
    write(fd, message, strlen(message));
    close(fd);

    unlink(link);
}

char * getMessage(char * link){
	int fd=-1;
    char * message = (char *)malloc(sizeof(char)*MAX_BUF);
    strcpy(message,"\0");
    while(fd==-1){
    fd = open(link, O_RDONLY);
    }
    int notRead = 0;
    notRead = read(fd, message, MAX_BUF);
    close(fd);
    return message;
}