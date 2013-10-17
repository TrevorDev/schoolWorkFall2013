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
			int r = rand()% 3;
			if(r==0){
				b->board[i][j]='R';
			}else if(r==1){
				b->board[i][j]='B';
			}else if(r==2){
				b->board[i][j]=' ';
			}
			//b->board[i][j]=i+48;
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
		return '*';
	}else{
		return b->board[x][y];
	}
}

void destroyBoard(Board * b){
	for(int i = 0;i<b->x;i++){
		free(b->board[i]);
	}
	free(b->board);
	free(b);
}

int stepRB(Board * b){
	int hitCount = 0;
	Board * c = createBoard(b->x,b->y);
	cpyBoard(c,b);
	for(int i = 0;i<c->x;i++){
		for(int j = 0;j<c->y;j++){
			if(getBoardVal(c,i,j)=='R'&&getBoardVal(c,i+1,j)==' '){
				hitCount++;
				b->board[i][j]=' ';
				b->board[i+1][j]='R';
			}
		}
	}
	cpyBoard(c,b);
	for(int i = 0;i<c->x;i++){
		for(int j = 0;j<c->y;j++){
			if(getBoardVal(c,i,j)=='B'&&getBoardVal(c,i,j+1)==' '){
				hitCount++;
				b->board[i][j]=' ';
				b->board[i][j+1]='B';
			}
		}
	}
	destroyBoard(c);
	return hitCount;
}



void printBoard(Board * b){
	for(int i = 0;i<b->x;i++){
	for(int j = 0;j<b->y;j++){
		
			printf("%c",b->board[j][i]);
		}
		printf("\n");
	}
	printf("----------------------------------------------\n");
}

int main()
{
	Board * b = createBoard(30,30);
	randBoard(b);
	printBoard(b);
	while(stepRB(b)!=0){
		printBoard(b);
	}
	

	destroyBoard(b);
	return 0;
}