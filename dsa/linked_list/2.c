//creating the linked list 
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

typedef struct Node Node;

void printList(Node* node) {
    while (node != NULL) {
        printf("%d ", node->data);
        node = node->next;
    }
    printf("\n");
}

int main() {
    Node* head = 1;
    Node* second = 2;
    Node* third = 3;

    head = (Node*)malloc(sizeof(Node));
    second = (Node*)malloc(sizeof(Node));
    third = (Node*)malloc(sizeof(Node));

    
    head->data = 100;
    head->next = second;

    second->data = 200;
    second->next = third;

    third->data = 300;
    third->next = NULL;

    
    printf("Linked list elements: ");
    printList(head);

    
    free(head);
    free(second);
    free(third);

    return 0;
}