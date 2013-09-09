#include <fcntl.h>
#include <stdio.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include "messageHelper.h"

int main()
{
	char * name = "n3";
	char * parent = "link2";
	char * children[3];
	children[0]="link4";
	children[1]="link5";
	children[2]="link6";
	makeNode(name, parent, children, 3);
    return 0;
}