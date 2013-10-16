#include <fcntl.h>
#include <stdio.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include "messageHelper.h"

int main()
{
	char * name = "n5";
	char * parent = "link4";
	char ** children = NULL;
	makeNode(name, parent, children, 0);
    return 0;
}