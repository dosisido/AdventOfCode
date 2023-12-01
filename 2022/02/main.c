#include<stdio.h>
#include<stdlib.h>
#define FILE_IN "file.txt"
#define rock_i 'A'
#define paper_i 'B'
#define scissors_i 'C'
#define rock_o 'X'
#define paper_o 'Y'
#define scissors_o 'Z'

int move(char car){
    switch(car){
        case rock_o:
            return 1;
        case paper_o:
            return 2;
        case scissors_o:
            return 3;
    }
}

int outcome(char in, char out){
    if(in - 'A' == out - 'X')   // patta
        return 3;
    if(in == rock_i && out == scissors_o)
        return 0;
    if(in == paper_i && out == rock_o)z
        return 0;
    if(in == scissors_i && out == paper_o)
        return 0;
    return 6;
}

int calcola(char in, char out){
    int tmp = 0;
    tmp = move(out);
    tmp+= outcome(in, out);
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
        i++;
        total+= calcola(in, out);
    }

    printf("Numero righe: %d\n", i);
    printf("Il totale e': %d", total);


    fclose(fin);
    return 0;
}