#include <fcntl.h>
#include <stdio.h>
#include <sys/stat.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include "messageHelper.h"

int main()
{
	char * nodes[2];
	nodes[0]="link1";
	nodes[1]="link2";
	char * message = malloc(sizeof(char)*MAX_BUF);
	int running = 1;
	if(running){
		printf("Enter your message\n");
		fgets(message, sizeof(message), stdin);
		message[strlen(message)-1]='\0';

		for(int i=0;i<sizeof(nodes)/sizeof(nodes[0]);i++){
			sendMessage(message, nodes[i]);
		}

		if(strcmp(message, "q")==0){
	    	running=0;
	    }
	}
	free(message);
	return 0;
}

