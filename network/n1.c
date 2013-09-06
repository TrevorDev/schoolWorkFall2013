#include <fcntl.h>
#include <stdio.h>
#include <sys/stat.h>
#include <string.h>
#include <unistd.h>
#include "messageHelper.h"
#define MAX_BUF 30

int main()
{
	char word[MAX_BUF]="";
	printf("Enter your word\n");
	fgets(word, sizeof(word), stdin);
	//word[strlen(word)]='\0';
	printf("You entered %s\n", word);
	printf("entered this\n");
	sendMessage(word);

	
	return 0;
}

