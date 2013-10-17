#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

typedef struct Board {
   char ** board;
   int x;
   int y;
} Board;

Board * createBoard(int x, int y){

	Board *b = (Board *) calloc(sizeof(Board), 1);
	b->x=x;
	b->y=y;
	b->board=(char**)calloc(b->x,sizeof(char*));
	for(int i = 0;i<b->x;i++){
		b->board[i]=(char*)calloc(b->y,sizeof(char));
	}
	return b;
}

void randBoard(Board * b){
	srand(time(NULL));
	for(int i = 0;i<b->x;i++){
		for(int j = 0;j<b->y;j++){
			int r = rand()% 4;
			if(r==0){
				b->board[i][j]='R';
			}else if(r==1){
				b->board[i][j]='B';
			}else if(r==2){
				b->board[i][j]=' ';
			}
		}
	}
}

void cpyBoard(Board * into, Board * from){
	for(int i = 0;i<from->x;i++){
		for(int j = 0;j<from->y;j++){
			into->board[i][j]=from->board[i][j];
		}
	}
}

char getBoardVal(Board * b, int x, int y){
	if(x<0||x>=b->x||y<0||y>=b->y){
		return 'X';
	}else{
		return b->board[x][y];
	}
}

int stepRB(Board * b){
	Board * c = createBoard(b->x,b->y);
	cpyBoard(c,b);
	for(int i = 0;i<b->x;i++){
		for(int j = 0;j<b->y;j++){
			if(getBoardVal(b,i,j)=='R'&&getBoardVal(b,i+1,j)==' '){
				b->board[i][j]=' ';
				b->board[i+1][j]='R';
			}
		}
	}
	return 0;
}

void destroyBoard(Board * b){
	for(int i = 0;i<b->x;i++){
		free(b->board[i]);
	}
	free(b->board);
	free(b);
}

void printBoard(Board * b){
	for(int i = 0;i<b->x;i++){
		for(int j = 0;j<b->y;j++){
			printf("%c",b->board[i][j]);
		}
		printf("\n");
	}
	printf("----------------------------------------------\n");
}

int main()
{
	Board * b = createBoard(5,5);
	randBoard(b);

	printBoard(b);
	int check = stepRB(b);
	printBoard(b);

	destroyBoard(b);
	return 0;
}