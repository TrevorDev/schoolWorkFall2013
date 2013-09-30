#include <stdio.h>
#include <string.h>
#include <stdlib.h>

enum COLLUM            /* Defines an enumeration type    */
{
    C_YEAR,C_MNTH,C_WDAY,C_HOUR,C_SEV,C_VEHS,C_CONF,C_RCFG,C_WTHR,C_RSUR,C_RALN,C_TRAF,V_ID,V_TYPE,V_YEAR,P_ID,P_SEX,P_AGE,P_PSN,P_ISEV,P_SAFE,P_USER
} crashInfo;

char * getLine(char line[], long unsigned int size, FILE * file){
	char * ret = fgets ( line, size, file );
	if(line[strlen(line)-1]=='\n'){
		line[strlen(line)-1]='\0';
	}
	return ret;
}

void getRow(char ** row,char*line){
	int i;
	char * token = strtok(line, ",");

	for(i=0;i<22;i++){
		row[i]=token;
		token = strtok(NULL, ",");
	}
}

char ** readFileToMem(FILE *file){
	char line[256];
	int i = 0;
	int j = 0;

	getLine(line, sizeof(line), file);
	long offset = (long)ftell(file);
	getLine(line, sizeof(line), file);
	long lineSize = (long)ftell(file)-offset;

	fseek(file, 0L, SEEK_END);
	long size = (long)ftell(file)-offset;
	fseek(file, 0L, SEEK_SET);
	long lineCount = size/lineSize;
	char ** rowArray = calloc(lineCount, sizeof(char *));
	printf("%ld\n", lineCount);
	fseek(file, offset, SEEK_SET);
	while (getLine(line, sizeof(line), file) != NULL) {
		rowArray[i] = strdup(line);
		i++;
	}
	return rowArray;
}

int freeMemFile(char ** rows){
	int i;
	int j;
	for(i=0;i<3933312;i++){
		free(rows[i]);
	}
	free(rows);
}
int splitEven(int*array,int size,int num){
	int val = num/size;
	int remain = num%size;
	int i;
	for(i=0;i<size;i++){
		array[i]=val;
		if(remain>0){
			array[i]++;
			remain--;
		}
	}
	return 0;
}

int main()
{	
	FILE *file;
	file = fopen("db.csv", "r");
	if (file == NULL){
		printf("invalid db file\n");
		return -1;
	}

	/*char line[256];
	getLine(line, sizeof(line), file);
	long start = (long)ftell(file);
	getLine(line, sizeof(line), file);
	long lineSize = (long)ftell(file)-start;

	fseek(file, 0L, SEEK_END);
	long size = (long)ftell(file)-start;
	fseek(file, 0L, SEEK_SET);
	long lineCount = size/lineSize;*/

	
	/*int len = 5;
	int ar[len];
	splitEven(ar,len,11);
	int i;
	for(i=0;i<len;i++){
		printf("%d\n", ar[i]);
	}*/

	//readFile(file, 0, -1, lineSize, start);
	char ** data = readFileToMem(file);
	freeMemFile(data);
	//printf("%s\n", data[0][C_YEAR]);
	fclose ( file );
	return 0;
}





/*int readFile(FILE *file, long startLine, long endLine, long lineSize, long offset){
	size_t len;
	char line[256];
	char* row[22];
	int lineCount = 0;
	int collisionCount = 0;
	int i;
	//Move to startLine position
	fseek(file, offset+(lineSize*startLine), SEEK_SET);
	while ( getLine(line, sizeof(line), file) != NULL && (endLine<0||ftell(file)<=offset+(lineSize*endLine))) {
		getRow(row, line);
		lineCount++;
		int pID = strtol(row[P_ID], (char **)NULL, 10);
		int vID = strtol(row[V_ID], (char **)NULL, 10);
			if(vID==1&&pID==1){
				collisionCount++;
			}
	}
	printf("Records:%d\n", lineCount);
	printf("Collisions:%d\n", collisionCount);
	
	return 0;
}*/

/*typedef struct collision collision;
typedef struct vehicle vehicle;
typedef struct person person;
typedef struct crash crash;

struct collision {
   char *year;
   char *month;
   char *weakDay;
   char *hour;
   char *severity;
   char *numVehicle;
   char *collisionConf;
   char *roadConf;
   char *weather;
   char *roadSurface;
   char *roadAlignment;
   char *trafficControl;
};

struct vehicle {
   char *id;
   char *type;
   char *year;
};

struct person {
   char *id;
   char *sex;
   char *age;
   char *pos;
   char *needMed;
   char *usedSafety;
   char *roadUserClass;
};

struct crash {
	collision * c;
	vehicle * v;
	person * p;
};

crash * createCrash(collision * c, vehicle *v, person * p){
	crash*ret = calloc(1, sizeof(collision *) + sizeof(vehicle*) + sizeof(person*));
	ret->c=c;
	ret->v=v;
	ret->p=p;
	return ret;
}

collision * createCollision(){
	collision*ret = calloc(12, sizeof(char *));
	return ret;
}

vehicle * createVehicle(){
	vehicle*ret = calloc(3, sizeof(char *));
	return ret;
}

person * createPerson(){
	person*ret = calloc(7, sizeof(char *));
	return ret;
}

crash * createCrashFromLine(char * line){
	char * token = strtok(line, ",");
	while( token != NULL ) 
	{
	  printf( " %s\n", token );

	  token = strtok(NULL, ",");
	}


	crash * ret = createCrash(NULL,NULL,NULL);
	return ret;
}*/