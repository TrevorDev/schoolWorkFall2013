#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

typedef struct Tile {
   int size;	
   int x;
   int y;
} Tile;

typedef struct Board {
   char ** board;
   int size;
} Board;

Board * createBoard(int size){
	Board *b = (Board *) calloc(sizeof(Board), 1);
	b->size=size;
	b->board=(char**)calloc(b->size,sizeof(char*));
	for(int i = 0;i<b->size;i++){
		b->board[i]=(char*)calloc(b->size,sizeof(char));
	}
	return b;
}

void randBoard(Board * b){
	srand(time(NULL));
	for(int i = 0;i<b->size;i++){
		for(int j = 0;j<b->size;j++){
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
	for(int i = 0;i<from->size;i++){
		for(int j = 0;j<from->size;j++){
			into->board[i][j]=from->board[i][j];
		}
	}
}

char getBoardVal(Board * b, int x, int y){
	return b->board[x%(b->size)][y%(b->size)];
}

void setBoardVal(Board * b, int x, int y, char val){
	b->board[x%(b->size)][y%(b->size)]=val;
}

void destroyBoard(Board * b){
	for(int i = 0;i<b->size;i++){
		free(b->board[i]);
	}
	free(b->board);
	free(b);
}

int stepRB(Board * b){
	int hitCount = 0;
	Board * c = createBoard(b->size);
	cpyBoard(c,b);
	for(int i = 0;i<c->size;i++){
		for(int j = 0;j<c->size;j++){
			if(getBoardVal(c,i,j)=='R'&&getBoardVal(c,i+1,j)==' '){
				hitCount++;
				setBoardVal(b, i, j, ' ');
				setBoardVal(b, i+1, j, 'R');
			}
		}
	}
	cpyBoard(c,b);
	for(int i = 0;i<c->size;i++){
		for(int j = 0;j<c->size;j++){
			if(getBoardVal(c,i,j)=='B'&&getBoardVal(c,i,j+1)==' '){
				hitCount++;
				setBoardVal(b, i, j, ' ');
				setBoardVal(b, i, j+1, 'B');
			}
		}
	}
	destroyBoard(c);
	return hitCount;
}



void printBoard(Board * b){
	for(int i = 0;i<b->size;i++){
	for(int j = 0;j<b->size;j++){
		
			printf("%c",b->board[j][i]);
		}
		printf("\n");
	}
	printf("----------------------------------------------\n");
}

int main()
{
	//setting values
	int numProcessors=3,boardSize=50,tileSize=10,maxDensity=50,maxSteps=10,seed=10,interactive=0;
	//error checking
	if(boardSize%tileSize!=0){
		printf("Invalid args, b mod t must equal 0\n");
		return 0;
	}

	//Setting up board
	Board * b = createBoard(boardSize);
	randBoard(b);

	int numTiles=(boardSize*boardSize)/(tileSize*tileSize);
	Tile* tiles[numTiles];
	for(int i=0;i<numTiles;i++){
		tiles[i] = (Tile*) calloc(sizeof(Tile), 1);
	}

	//work loop
	do{
		printBoard(b);
		fgetc(stdin);
	}while(stepRB(b)!=0);
	

	destroyBoard(b);
	return 0;
}