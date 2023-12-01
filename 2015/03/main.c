#include<stdio.h>
#define DIM 1000000
#define FIN "file.txt"


int main(int argc, char* argv[]){
    short int board[DIM][DIM];
    int x = DIM/2, y = DIM/2, sum = 0;
    char c;

    FILE *fin = fopen(FIN, "r");

    while(!feof(fin)){
        fscanf(fin, " %c", &c);
        switch(c){
            case '^': 
                y--;
                break;
            case 'v':
                y++;
                break;
            case '<':
                x--;
                break;
            case '>':
                x++;
                break;
        }

        if(board[x][y] == 0)
            sum++;

        board[x][y]++;

    }
    fclose(fin);

    printf("Santa visited %d houses\n", sum);

    return 0;
}