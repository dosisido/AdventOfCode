#include<stdio.h>
#define FILE_IN "file.txt"


void readFile(){
    FILE *fp;
    int* seq = malloc(sizeof(int) * 100);
    char ch;

    fp = fopen(FILE_IN, "r");
    if(fp == NULL){
        printf("Error opening file\n");
        return;
    }
    while((ch = fgetc(fp)) != EOF){
        printf("%c", ch);
    }
    fclose(fp);

}

int main(int argc, char* argv[]){
    
    return 0;
}