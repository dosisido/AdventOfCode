#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#define FILE_IN "input.txt"

typedef enum {False, True} bool;

// alloca e dealloca
void init(int*** bosco, int* R, int* C){
    int i, j;
    long long int tmp;
    char str[2];
    str[1] = '\0';
    FILE *fin;

    if ((fin = fopen(FILE_IN, "r")) == NULL){
        printf("Errore nell'apertura del file: \"%s\"", FILE_IN);
        exit(-1);
    }

    for (i=0; fgetc(fin) != '\n'; i++);
    *R = i;
    i=0;
    while(!feof(fin)){
        fscanf(fin, "%*lld", &tmp);
        i++;
    }
    *C = i+1;
    fclose(fin);


    if ((fin = fopen(FILE_IN, "r")) == NULL){
        printf("Errore nell'apertura del file: \"%s\"", FILE_IN);
        exit(-1);
    }

    *bosco = (int**)malloc(*R * sizeof(int*));
    for (i=0; i<*R; i++){
        (*bosco)[i] = (int*)malloc(*C * sizeof(int));
        for (j=0; j<*C; j++){
            str[0] = fgetc(fin);
            (*bosco)[i][j] = atoi(str);
        }
        fscanf(fin, " ");
    }
    fclose(fin);
}

void release(int** bosco, int R, int C){
    for (int i=0; i<R; i++) free(bosco[i]);
    free(bosco);
}

int calcola(int** bosco, int R, int C){
    int i, j, k, count=0, visibileDaLati, albero, maxR=-1, maxC=-1, value=-1;
    int tmp[4], tmpValue;
    bool flag;

    for(i=1; i<R-1; i++){               // i riga
        for(j=1; j<C-1; j++){           // i colonna
            // verifico se l'albero in posizione (i,j) e' visibile dall'esterno
            visibileDaLati=0;
            albero = bosco[i][j];
            tmp[0]=0; tmp[1]=0; tmp[2]=0; tmp[3]=0;

            // dall'alto
            flag=True;
            for(k=i-1; k>=0; k--){
                tmp[0]++;
                if(bosco[k][j] >= albero){
                    flag=False;
                    break;
                }
            }
            if(flag) visibileDaLati++;

            // dal basso
            flag=True;
            for(k=i+1; k<R; k++){
                tmp[1]++;
                if(bosco[k][j] >= albero){
                    flag=False;
                    break;
                }
            }
            if(flag) visibileDaLati++;

            // da sinistra
            flag=True;
            for(k=j-1; k>=0; k--){
                tmp[2]++;
                if(bosco[i][k] >= albero){
                    flag=False;
                    break;
                }
            }
            if(flag) visibileDaLati++;

            // da destra
            flag=True;
            for(k=j+1; k<C; k++){
                tmp[3]++;
                if(bosco[i][k] >= albero){
                    flag=False;
                    break;
                }
            }
            if(flag) visibileDaLati++;

            printf("Albero in posizione (%d,%d) [%d] visibile da %d direzioni\n", i, j, albero, visibileDaLati);
            if(visibileDaLati!=0)count++;

            tmpValue = tmp[0] * tmp[1] * tmp[2] * tmp[3];
            if(tmpValue > value){
                value = tmpValue;
                maxR = i;
                maxC = j;
            }
        }
        printf("\n");
    }

    printf("Albero in posizione (%d,%d) [%d] ha il valore massimo: %d\n", maxR, maxC, bosco[maxR][maxC], value);

    return count + R + R + C + C - 4;
}

int main(int argc, char* argv[]){
    int** bosco, R, C;
    init(&bosco, &R, &C);

    printf("Trovati %d alberi visibili dall'esterno", calcola(bosco, R, C));
    return 0;
}