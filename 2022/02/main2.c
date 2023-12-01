#include<stdio.h>
#include<stdlib.h>
#define FILE_IN "file.txt"
#define rock_i 'A'
#define paper_i 'B'
#define scissors_i 'C'
#define lose 'X'
#define patta 'Y'
#define win 'Z'

enum {zero, rock,paper,scissors};

int move(char in, char outcome){ // il punteggio della mossa che devo fare per l'outcome
    if(outcome == patta)
        return in - 'A' + 1;
    if(outcome == win)
        switch(in){
            case rock_i: return paper;
            case paper_i: return scissors;
            case scissors_i: return rock;
        }
    if(outcome == lose)
        switch(in){
            case rock_i: return scissors;
            case paper_i: return rock;
            case scissors_i: return paper;
        }
}

int outcome(char out){
    switch(out){
        case 'X':
            return 0;
        case 'Y':
            return 3;
        case 'Z':
            return 6;
    }
}

int calcola(char in, char out){
    int tmp = 0;
    tmp = move(in, out);
    tmp+= outcome(out);
    return tmp;
}

int main(int argc, char* argv[]){
    char in, out;
    int total=0, i=0;
    FILE *fin;
    if ((fin = fopen(FILE_IN, "r")) == NULL){
        printf("Errore nell'apertura del file: \"%s\"", FILE_IN);
        exit(-1);
    }

    while(fscanf(fin, " %c %c ", &in, &out) == 2){
        total+= calcola(in, out);
    }

    printf("Il totale e': %d", total);


    fclose(fin);
    return 0;
}