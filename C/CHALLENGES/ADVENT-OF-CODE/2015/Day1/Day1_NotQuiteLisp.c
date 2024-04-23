#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* read_data() {
    FILE *fp;
    long size;
    char *buffer;

    fp = fopen("data.txt", "r");
    if (fp == NULL){
        printf("Error Opening File.");
        return NULL;
    }

    fseek(fp,0,SEEK_END);
    size = ftell(fp);
    fseek(fp,0,SEEK_SET);

    buffer = (char*) malloc(size + 1);
    if (!buffer){
        printf("Memory allocation error\n");
        fclose(fp);
        return NULL;
    }

    fread(buffer, size, 1, fp);
    buffer[size] = '\0';

    fclose(fp);

    return buffer;
}

int part_one(){
    char* data = read_data();
    if (data == NULL){ 
        return 1;
    }

    // printf("%c\n", data[0]);
    char prent_left = ')';
    char prent_right = '(';
    int floor = 0;

    for (int i = 0; i <= strlen(data); i++){
        if (data[i] == prent_left){
            floor -= 1;
            if (floor == -1){
                printf("%i %i\n", i+1, floor);
            }
        } else if (data[i] == prent_right){
            floor += 1;
        }
    }

    free(data);
    return floor;
}

int main() {
    printf("%i\n", part_one());
    return 0;
}