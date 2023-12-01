#include<stdio.h>
#include<stdlib.h>
#define FILE_IN "input.txt"

int main(int argc, char* argv[]){
    int Ai, Af, Bi, Bf, count=0;
    FILE *fin;
    if ((fin = fopen(FILE_IN, "r")) == NULL){
        printf("Errore nell'apertura del file: \"%s\"", FILE_IN);
        exit(-1);
    }
    
    for(int i=0; i<1000; i++){
        fscanf(fin, " %d %d %d %d ", &Ai, &Af, &Bi, &Bf);

        // scambia
        if(Bi<Ai){int tmp = Ai;Ai = Bi;Bi = tmp;tmp = Af;Af = Bf;Bf = tmp;}
        
        if(Bi<=Af) 
            count++;       
    }

    printf("count: %d", count);
    fclose(fin);
    return 0;
}