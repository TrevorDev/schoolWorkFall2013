/********
messageHelper.h -- header file for messageHelper.c
author: Trevor Baron
********/
#ifndef MHELPER_H
#define MHELPER_H 1

#define MAX_BUF 32
void makePipes(char * children[], int size);
void deletePipes (char * children[], int size);
void sendMessage(char * message, char * link);
char * getMessage(char * link);
void makeNode(char * name, char * parent, char * children[], int size);

#endif