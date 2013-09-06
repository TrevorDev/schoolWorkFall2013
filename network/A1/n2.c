#include <fcntl.h>
#include <stdio.h>
#include <sys/stat.h>
#include <unistd.h>

#define MAX_BUF 30

int main()
{
    int fd;
    char * link1 = "/tmp/link1";
    char buf[MAX_BUF];

    /* open, read, and display the message from the FIFO */
    fd = open(link1, O_RDONLY);
    read(fd, buf, MAX_BUF);
    printf("n2, message %s received\n", buf);
    close(fd);

    return 0;
}