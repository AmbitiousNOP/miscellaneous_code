#include<stdio.h>


int foo(int x, int y){
    return x + y;
}

int print_foo(int i, int j, int (*f)(int, int)){
    return f(i,j);

}


int main(){

    int (*f)(int,int) = foo;
    printf("%d\n", f(3,2));

    printf("%d\n", print_foo(1,2,foo));

    return 0;
}
