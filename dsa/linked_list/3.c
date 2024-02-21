#include<stdio.h>
#include<stdlib.h.>
// represent a node of singly linked list 
struct node
{
    int data;
    struct node *next;
};
// represent the head and tail of the singley linked list
struct node *head,*tail=NULL;
//addnode() will add a new node to the list 
void addnode(int data){
    //create a new node
    struct node *newnode = (struct node *)malloc(sizeof(struct node ));
    newnode->data=data;
    newnode->next=NULL;
    //check if the list is empty
    if(head==NULL)
    {
        //if list is empty,both head and tail will point to new node 
        head =newnode;
        tail =newnode;

    }
    else{
        ///newnode will be added after tail
        tail-> next=newnode;
        //newnode will become new tail of the list
        tail=newnode;
    }
    }
    //display()will display all the nodes present in the list
    void display(){
        //node current will poiunt to head
        struct node *current = head;
        if (head==NULL){
            printf("list is empty\n");
            return;
        }
        printf("nodes of singly linked list:\n");
        while(current!=NULL){
         //prints each node y incrementing pointer
         printf("%d",current->data);
         current=current->next;
       }
       printf("\n");
    }
    int main()
    {
        //add nodes to the list 
        addnode(1000);
        addnode(2000);
        addnode(3000);
        addnode(4000);
        //displays the nodes present in the list
        display();
        return 0;
    }


