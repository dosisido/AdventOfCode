#include<stdio.h>
#include<stdlib.h>
#define FILE_IN "input.txt"

int main(int argc, char* argv[]){
    int count=0, max1=0, max2=0, max3=0, tmp;
    char str[100];
    FILE *fin;
    if ((fin = fopen(FILE_IN, "r")) == NULL){
        printf("Errore nell'apertura del file: \"%s\"", FILE_IN);
        exit(-1);
    }

    while(!feof(fin)){
        fgets(str, 100, fin);
        if(sscanf(str, " %d ", &tmp)==1){
            count+= tmp;
            if(count>max1){
                max3=max2;
                max2=max1;
                max1=count;
            }
            else if(count>max2){
                max3=max2;
                max2=count;
            }
            else if(count>max3){
                max3=count;
            }
        }else count=0;
    }
    
    printf("L'elfo con le calorie maggiori porta %d calorie", max1 + max2 + max3);

    fclose(fin);
    return 0;
}