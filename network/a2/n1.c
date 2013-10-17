#include <fcntl.h>
#include <stdio.h>
#include <sys/stat.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include "messageHelper.h"

int main()
{

	//Create children pipes
	char * children[2];
	children[0]="link1";
	children[1]="link2";
	int size = 2;
	makePipes(children,size);
	
	int running = 1;
	while(running){
		char * message = (char *)calloc(MAX_BUF, sizeof(char));
		char * toSend = (char *)calloc(MAX_BUF, sizeof(char));
		printf("Enter your file and node to send to eg. file.txt n4\n");
		fgets(message, sizeof(char)*MAX_BUF, stdin);

		if(message[strlen(message)-1]=='\n'){
			message[strlen(message)-1]='\0';
		}
		char*file = strtok(message," ");
		char*toNode = strtok(NULL," ");
		char*charPacket = calloc(MAX_BUF,sizeof(char));
		if(toNode!=NULL){
			charPacket[0]='T';
			for(int i=0;i<strlen(toNode);i++){
				charPacket[i+1]=toNode[i];
				charPacket[i+2]='\0';
			}
			printf("TO: %s\n",charPacket);
		}
		printf("%s-%s\n",file,toNode);
		FILE * fd = fopen(file, "r");
		if(fd!=NULL){
			 while(fgets(toSend, 25, fd)!=NULL ) {
				printf("%s",toSend);
				for(int i=0;i<size;i++){
					for(int j=0;j<size;j++){
						charPacket[0]=toSend[j];
						sendMessage(charPacket, children[i]);
					}
				}
			 }
			 printf("\n");
			 
		}else{
			printf("Invalid File\n");
		}

		/*//Send message to child nodes
		for(int i=0;i<size;i++){
			sendMessage(message, children[i]);
		}

		//Receive done message from child nodes
		for(int i=0;i<size;i++){
			char * recMessage = getMessage(children[i]);
			free(recMessage);
		}

		printf("all messages received\n");
*/
		//Quit once all children are closed
		if(strcmp(message, "q")==0){
	    	running=0;
	    }
	    free(message);
	    free(charPacket);
	    free(toSend);
	}

	deletePipes(children,size);
	
	return 0;
}

