#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node * next;
}node;

void insertNodeEnd (node * head,int data);
int sumNodes(node * head);
void addNode (node ** head,int data);
int countNode(node * head);
void Display (node * head);






int main()
{
    //defining nodes ;
    struct node * head;
    struct node * first;
    struct node * second;
    struct node * third;

//allocating memory
first = malloc(sizeof (node));
second = malloc(sizeof (node));
third = malloc(sizeof (node));
// fourth = malloc(sizeof (struct node));

//pointer head to first node,you can't assin a pointer head to first 
// before assigning the memory to first;
head = first;


first -> number = 1;
first -> next = second;

second -> number = 2;
second -> next = third;

third -> number = 3;
third -> next = NULL;

addNode(&head,5);

Display(head);
insertNodeEnd(head,9);
printf("Total nodes :%d\n",countNode(head));
printf("Sum: %d",sumNodes(head));

free(first);
free(second);
free(third);



}


void insertNodeEnd (node * head,int data)
{
    node * n = malloc(sizeof(node));
    if(n == NULL)
    {
        printf("memory allocation failed");
        return;
    }
    while (head->next != NULL)
    {
        //doing it in the loop is wrong because
        // if(head->next == NULL)
        // {
        //     n->next = NULL;
        //     n->number = data;
        //     head->next = n;
        //     return;
        // }
        //when the if condition run head points to n
        //and n next is null so it recusively run the if condition
        //and never comes out of the loop
        //so you have to return the function after the if condition
        //or you can change the data outside the loop
        head = head->next;
    }
    n->number = data;
    n->next = NULL;
    head->next = n;
    return;
}


int sumNodes(node * head)
{
    int sum = 0;
    while (head != NULL)
    {
        sum += head->number;
        head = head->next;
    }

    return sum;
    
}



void addNode (node ** head,int data)
{
    node * n = malloc(sizeof(node));
    if (n == NULL)
    {
        printf("memory allocation failed");
    }
    n->number = data;
    n->next = *head;
    *head = n;
    
}



int countNode(node * head)
{
    int count = 0;
    while (head != NULL)
    {
        count++;
        head = head->next;
    }
    return count;
    
}

void Display (node * head)
{
    node * ptr = head;
    while(ptr != NULL)
    {
        printf("%d\n",ptr->number);
        ptr = ptr->next;
    }

}