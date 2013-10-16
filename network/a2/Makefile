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

SOURCE = $(SRCDIR)n1.c $(SRCDIR)n2.c $(SRCDIR)n3.c $(SRCDIR)n4.c $(SRCDIR)n5.c $(SRCDIR)n6.c $(SRCDIR)n7.c $(SRCDIR)messageHelper.c 


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
	$(CC) $(LIBDIRS) $(LDFLAGS) -o $(BINDIR)N4 n4.o $(OBJS) $(LIBS)
	$(CC) $(LIBDIRS) $(LDFLAGS) -o $(BINDIR)N5 n5.o $(OBJS) $(LIBS)
	$(CC) $(LIBDIRS) $(LDFLAGS) -o $(BINDIR)N6 n6.o $(OBJS) $(LIBS)
	$(CC) $(LIBDIRS) $(LDFLAGS) -o $(BINDIR)N7 n7.o $(OBJS) $(LIBS)

build: $(SOURCE)
	$(CC) $(CFLAGS) -c $(SOURCE) $(INCLUDES)

clean:
	@ rm *.o

run: prog 
	$(BINDIR)N7 &
	$(BINDIR)N6 &
	$(BINDIR)N5 &
	$(BINDIR)N4 &
	$(BINDIR)N3 &
	$(BINDIR)N2 &
	$(PROGNAME)
 
val: prog
	valgrind $(BINDIR)N7 &
	valgrind $(BINDIR)N6 &
	valgrind $(BINDIR)N5 &
	valgrind $(BINDIR)N4 &
	valgrind $(BINDIR)N3 &
	valgrind $(BINDIR)N2 &
	valgrind $(PROGNAME)