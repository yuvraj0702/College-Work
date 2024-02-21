#include <stdio.h>
#include <stdlib.h>
// creating a node
struct node {
    int value;
    struct node *next;
};
//print the linked list value
void printlinkedlist(struct node *p)
{
    while (p != NULL){
        printf("%d",p->value);
        p = p->next;
    }
}
int main() {
    //initialize node
    struct node *head;
    struct node *one= NULL;
    struct node *two= NULL;
    struct node *three= NULL;
    //allocated memory
     one = malloc(sizeof(struct node));
     two = malloc(sizeof(struct node));
     three = malloc(sizeof(struct node));
     //assign value values
     one->value=100;
     two->value=200;
     three->value=300;
     //connect nodes 
     one->next=two;
     two->next=three;
     three->next=NULL;
     //printing node-value
     head=one;
     printlinkedlist(head);
     }