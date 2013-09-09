#include <fcntl.h>
#include <stdio.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include "messageHelper.h"

int main()
{
	char * name = "n4";
	char * parent = "link3";
	char ** children = NULL;
	makeNode(name, parent, children, 0);
    return 0;
}