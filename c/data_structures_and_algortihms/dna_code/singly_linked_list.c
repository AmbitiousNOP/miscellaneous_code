#include <stdio.h>
#include <stdlib.h>

// INSERTING AT THE HEAD OF THE LIST EACH TIME.

struct Node{
    int element;
    struct Node *next_node;
};

// first node in the list
struct Node* head = NULL; 

int insert(int elem){
    //allocating memory.
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    
    // assign elem to element in newNode.
    newNode->element = elem;

    // The new node's next_node should point to the current head
    newNode->next_node = head;

    // Update head to be the new node
    head = newNode;
    
    return 0;
}

int traverse_list(){
    struct Node *current = head;

    while (current != NULL){
        printf("%d ", current->element);
        current = current->next_node;
    }
    printf("\n");
    return 1;
}


int main(){
    // linked list: []
    insert(8);
    // linked list: [8, NULL]
    insert(12);
    // linked list: [12,addr_of_8], [8,NULL]
    printf("%d\n", head->element); //12
    printf("%p\n", (void *)head->next_node); //addr_of_8
    printf("%d\n", head->next_node->element); //8

    //traverse list
    printf("TRAVERSING:\n");
    traverse_list();

    
    return 0;
}
