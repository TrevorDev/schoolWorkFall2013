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
	
	char * message = (char *)calloc(MAX_BUF, sizeof(char));;
	char*charPacket = calloc(MAX_BUF,sizeof(char));
	char * toSend = (char *)calloc(MAX_BUF, sizeof(char));

	int running = 1;
	while(running){
		
		printf("Enter your file and node to send to eg. test.txt n4\n");
		fgets(message, sizeof(char)*MAX_BUF, stdin);
		if(message[strlen(message)-1]=='\n'){
			message[strlen(message)-1]='\0';
		}
		char*file = strtok(message," ");
		char*toNode = strtok(NULL," ");
		if(toNode!=NULL){
			charPacket[0]=' ';
			for(int i=0;i<strlen(toNode);i++){
				charPacket[i+1]=toNode[i];
				charPacket[i+2]='\n';
				charPacket[i+3]='\0';
			}
		
		FILE * fd = fopen(file, "r");
		if(fd!=NULL){
			 while(fgets(toSend, MAX_BUF, fd)!=NULL ) {
			 	for(int j=0;j<strlen(toSend);j++){
			 		charPacket[0]=toSend[j];
			 		//printf("HERE:::::%s\n", charPacket);
			 		//Send message to child nodes
					for(int i=0;i<size;i++){
						sendMessage(charPacket, children[i]);
					}

					//Receive done message from child nodes
					for(int i=0;i<size;i++){
						char * recMessage = getMessage(children[i]);
						free(recMessage);
					}
			 	}
			 }
			 
		}else{
			printf("Invalid File\n");
		}
	}else{
		printf("Invalid Input\n");
	}


		

		printf("Do you want to continue(Y/N)?\n");
		fgets(message, sizeof(char)*MAX_BUF, stdin);
		if(message[strlen(message)-1]=='\n'){
			message[strlen(message)-1]='\0';
		}
		//Quit once all children are closed
		if(strcmp(message, "N")==0||strcmp(message, "n")==0){
			for(int i=0;i<size;i++){
				sendMessage("q", children[i]);
			}

			//Receive done message from child nodes
			for(int i=0;i<size;i++){
				char * recMessage = getMessage(children[i]);
				free(recMessage);
			}
	    	running=0;
	    }
	    
	}

	free(message);
	free(charPacket);
	free(toSend);
	deletePipes(children,size);
	
	return 0;
}

