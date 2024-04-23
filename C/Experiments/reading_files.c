#include <stdio.h>

int main(){
    // define variable for type file.
    FILE *fp;

    // open the file
    fp = fopen("data.txt", "r");

    // init an empty multi-dimensional array of known size. 
    int arr[1000][3] = {{0}};
    
    // init a buffer to capture and store each line from data.txt
    char buffer[10];

    // init row value so we can loop over each row in arr.
    int row = 0;
    while (fgets(buffer, 10, fp) != NULL){
        //printf("%s", buffer);
        sscanf(buffer, "%d%*c%d%*c%d", &arr[row][0], &arr[row][1], &arr[row][2]);
        //printf("current row = %d data = %d %d %d\n", row, arr[row][0], arr[row][1], arr[row][2]);
        row ++;
    }

    fclose(fp);

    
    for (int i = 0; i < 1000; i++){
        for (int j = 0; j < 3; j++){
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }
    

    return 0;
}