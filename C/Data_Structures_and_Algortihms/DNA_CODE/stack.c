#include <stdio.h>

#define MAX_SIZE 10

typedef struct
{
    int items[MAX_SIZE];
    int top;
} stack ;


void init_stack(stack *s){
    s->top = -1;
}

int push(stack *s, int item){
    // check for overflow
    if (s->top == MAX_SIZE){
        return 1;

    }else{
        s->top += 1;
        s->items[s->top] = item; 
        return 0;
    }
}

int pop(stack *s){
    //check for underflow
    if (s->top == -1){
        return 1; //not ideal return since stack can contain 1.
    } else{
        s->top -= 1;
        return s->items[s->top+1];
    }
}

int stack_size(stack *s){
    return s->top +1;
}

int main(){
    stack s;
    init_stack(&s);
    push(&s, 10);
    push(&s, 12);
    
    // prints 10,12, 
    for (int i = 0; i < stack_size(&s); i++){
        printf("%d, ", s.items[i]);
    }
    printf("\n");

    pop(&s);
    pop(&s);
    push(&s, 100);
    
    // prints 100,
    for (int i = 0; i < stack_size(&s); i++){
        printf("%d, ", s.items[i]);
    }
    printf("\n");

    return 0;
}
