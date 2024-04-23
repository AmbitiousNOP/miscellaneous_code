// find the surface area: 2*l*w + 2*w*h + 2*h*l
// The elves also need a little extra paper for each present: 
// the area of the smallest side.

/*
A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52
square feet of wrapping paper plus 6 square feet of slack, 
for a total of 58 square feet.

*/
#include <stdio.h>

#define MIN(a, b, c) ((a) < (b) ? ((a) < (c) ? (a) : (c)) : ((b) < (c) ? (b) : (c)))

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

    // loop over the file (fp) and read in each row to buffer. NOTE: if buffer is to small, array will contain 0's from initialization.
    while (fgets(buffer, 10, fp) != NULL){
        sscanf(buffer, "%d%*c%d%*c%d", &arr[row][0], &arr[row][1], &arr[row][2]);
        row ++;
    }
    fclose(fp);

    // declare lw, wh, hl for easy MIN compare and math calc.
    int lw = 0; // length width
    int wh = 0; // width height 
    int hl = 0; // height length
    int smallest_side = 0;
    int square_feet = 0;
    int answer = 0;

    for (int i = 0; i < 1000; i++){
        lw = arr[i][0] * arr[i][1];
        wh = arr[i][1] * arr[i][2];
        hl = arr[i][2] * arr[i][0];
        smallest_side = MIN(lw, wh, hl);

        square_feet = ((2*lw) + (2*wh) + (2*hl)) + smallest_side;
        answer += square_feet;
    }
    printf("ANSWER: %d\n", answer);
    return 0;
}