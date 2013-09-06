#include <fcntl.h>
#include <stdio.h>
#include <sys/stat.h>
#include <string.h>
#include <unistd.h>
#define MAX_BUF 30

int sendMessage(char * link, char * word){
	int fd;
    char * link1 = "/tmp/link1";

    mkfifo(link1, 0666);

    fd = open(link1, O_WRONLY);
    write(fd, word, strlen(word));
    close(fd);

    unlink(link1);
    return 0;
}