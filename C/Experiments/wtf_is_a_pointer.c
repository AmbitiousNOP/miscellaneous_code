#include <stdio.h>

int main(){
    // * means dereference 
    // & means address of
    int i = 10;
    printf("%d\n", i); // prints 10
    printf("%p\n", &i); // prints address

    int *y = &i; // holds address of i
    printf("%i\n", *y); // prints 10

    return 0;
}