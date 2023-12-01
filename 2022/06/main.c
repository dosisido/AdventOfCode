#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#define FILE_IN "06/input.txt"
#define N 14

typedef enum {False, True} bool;


bool isNotEqual(char arr[N]){
    int i, j;
    for(i=0; i<N; i++)
        for(j=0; j<N; j++)
            if(arr[i] == arr[j] && i != j)
                return False;
    return True;
}

int main(int argc, char* argv[]){
    time_t tot = clock();
    int i =N, j;
    char arr[N],car;
    FILE *fin;
    if ((fin = fopen(FILE_IN, "r")) == NULL){
        printf("Errore nell'apertura del file: \"%s\"", FILE_IN);
        exit(-1);
    }
    
    for(j=0; j<N; j++)
        arr[j] = fgetc(fin);

    while(!feof(fin)){
        if(!isNotEqual(arr)){
            for(j=0; j<N-1; j++)
                arr[j] = arr[j+1];
            arr[N-1] = fgetc(fin);
            i++;
        }else{
            break;
        }
    }

    printf("Il numero di caratteri letti e' %d\n", i);
    fclose(fin);    
    printf("Tempo impiegato: %f", ((double) (clock() - tot)) / CLOCKS_PER_SEC);
    return 0;
}