/********
messageHelper.h -- header file for messageHelper.c
********/
#ifndef MHELPER_H
#define MHELPER_H 1

#define MAX_BUF 30

void sendMessage(char * message, char * link);
char * getMessage(char * link);
//char * getMessage(char * link);

#endif