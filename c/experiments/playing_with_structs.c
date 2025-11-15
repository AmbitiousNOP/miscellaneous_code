#include <stdio.h>
#include <stdlib.h>


struct Testing{
    int item;
    int next_item;
};


int main(){
    struct Testing example;
    
    example.item = 10;
    example.next_item = 11;
    
    printf("%d\n", example.item); // prints 10
    printf("%d\n", example.next_item); // prints 11

    //struct Testing *testPTR;

    printf("%lu\n", sizeof(struct Testing)); // prints 8 because int size is 4 bytes.
    

    return 0;
}

