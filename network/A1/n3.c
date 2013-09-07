#include <fcntl.h>
#include <stdio.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include "messageHelper.h"

int main()
{
	int running = 1;
	if(running){
		char * message = getMessage("link2");
	    printf("n3, message %s received\n", message);
	    if(strcmp(message, "q")==0){
	    	running=0;
	    }
	    free(message);
	}
    return 0;
}