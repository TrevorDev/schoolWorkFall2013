CC          =	gcc
# Flags that are sent to the compiler
# Do not change these
CFLAGS      = -g -pedantic -Wall -std=c99
LDFLAGS     =

#Directories where the compiler can find things
INCLUDES    =
LIBDIRS     = 
LIBS        = 

BINDIR = ./
SRCDIR = ./

#Put the names of your source code files in the lines below.  You will need both your
# Solution source code file and the source code with the main program in it

SOURCE = $(SRCDIR)n1.c $(SRCDIR)n2.c $(SRCDIR)n3.c $(SRCDIR)messageHelper.c 


#The list of object files for each program is below.  
# The object file names here must match the file names of your source code 
# except with .o instead of .c.   Make changes as appropriate


OBJS    = messageHelper.o


PROGNAME = $(BINDIR)N1

default : all

all : prog


prog : build
	$(CC) $(LIBDIRS) $(LDFLAGS) -o $(PROGNAME) n1.o $(OBJS) $(LIBS)
	$(CC) $(LIBDIRS) $(LDFLAGS) -o $(BINDIR)N2 n2.o $(OBJS) $(LIBS)
	$(CC) $(LIBDIRS) $(LDFLAGS) -o $(BINDIR)N3 n3.o $(OBJS) $(LIBS)

build: $(SOURCE)
	$(CC) $(CFLAGS) -c $(SOURCE) $(INCLUDES)

clean:
	@ rm *.o

run: prog 
	$(BINDIR)N3 &
	$(BINDIR)N2 &
	$(PROGNAME)
 
val: prog
	valgrind --dsymutil=yes --leak-check=full --show-reachable=yes $(PROGNAME) 
