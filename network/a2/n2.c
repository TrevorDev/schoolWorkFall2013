#include <fcntl.h>
#include <stdio.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include "messageHelper.h"

int main()
{
	char * name = "n2";
	char * parent = "link1";
	char * children[1];
	children[0]="link3";
	makeNode(name, parent, children, 1);
    return 0;
}