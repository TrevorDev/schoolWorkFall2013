#include <fcntl.h>
#include <stdio.h>
#include <sys/stat.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include "messageHelper.h"

int main()
{
	char * children[2];
	children[0]="link1";
	children[1]="link2";
	int size = 2;
	makePipes(children,size);
	
	int running = 1;
	while(running){
		char * message = (char *)calloc(MAX_BUF, sizeof(char));;
		printf("Enter your message\n");
		fgets(message, sizeof(char)*MAX_BUF, stdin);
		if(message[strlen(message)-1]=='\n'){
			message[strlen(message)-1]='\0';
		}

		for(int i=0;i<size;i++){
			sendMessage(message, children[i]);
		}
		for(int i=0;i<size;i++){
			char * recMessage = getMessage(children[i]);
			//printf("%s, received %s from %s\n","n1",recMessage,children[i]);
			free(recMessage);
		}

		printf("all messages received\n");

		if(strcmp(message, "q")==0){
	    	running=0;
	    }
	    free(message);
	}

	deletePipes(children,size);
	
	return 0;
}

