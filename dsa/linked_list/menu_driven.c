#include <stdio.h>
#include <stdlib.h>

struct node{
    int data;
    struct node* next;
};

void create_linked_list(struct node* head,int n)
{
    struct node *fnNode,*tmp;
    fnNode = (struct node*)malloc(sizeof(struct node));

    if(fnNode == NULL)
    {
        printf("The memory has not been allocated");
    }

    for(int i=0;i<n;i++)
    {
      int val;
      pritnf("Enter the values of linked list");
      scanf("%d",&val);

      fnNode->data = val;
      fnNode->next = NULL;

      tmp->next = fnNode;
      fnNode = fnNode->next;
    }
}

void display(struct node* head)
{
    while(head != NULL)
    {
        printf("%d",head->data);
        head = head->next;
    }
}

void create_node_at_beginning(struct node* head)
{
    struct node *new_node;

    new_node = (struct node*)malloc(sizeof(struct node));
    
    int val;
    pritnf("Enter the value of the value to be replaced");
    scanf("%d",&val);

    new_node->data = val;
    new_node->next = head;
    head = new_node; 
}

void create_node_at_end(struct node* head)
{
    struct node *new_node,*last;

    new_node = (struct node*)malloc(sizeof(struct node));
    last = head;
    
    int val;
    pritnf("Enter the value of the value to be replaced");
    scanf("%d",&val);

    new_node->data = val;
    new_node->next = NULL;

    while(last != NULL)
    {
        last = last->next; 
    }
    
    last = new_node;
}

void create_node_before_a_node(struct node* head)
{
    struct node* new_node;
    struct node* ptr=head;
    new_node = (struct node*)malloc(sizeof(struct node));

    int val;
    pritnf("Enter the value of the value to be replaced");
    scanf("%d",&val);

    int pos;
    printf("Enter the position at which node must be added");
    scanf("%d",&pos);

    new_node->data = val;
    new_node->next = NULL;

    pos--;
    while(pos!=1)
    {
        ptr = ptr->next;
        pos--;  
    }

    new_node->next = ptr->next;
    ptr->next = new_node;
}

void create_node_after_a_node(struct node* head)
{
    struct node* new_node;
    struct node* ptr=head;

    int val;
    printf("Enter the value to be entered");
    scanf("%d",&val);

    int pos;
    printf("Enter the position at which the node to enter");
    scanf("%d",&pos);

    new_node->data = val;
    new_node->next = NULL;

    for(int i=0;i<pos;i++)
    {
       ptr = ptr->next;
    }

    new_node->next = ptr->next;
    ptr->next = new_node;
}

void delete_a_node_at_beginning(struct node* head)
{
    struct node* n=head;
    struct node* current=head;

    int position;
    printf("Enter the position at which node must be deleted");
    scanf("%d",&position);

    if(head == NULL)
    {
        printf("The list is already empty");
    }    

    else if(position == 1)
    {
        head = current->next;
        free(current);
        current == NULL;
    }
}
    
void delete_a_node_at_end(struct node* head)
{
    struct node* n = head;
    struct node* current = head;

    int position;
    printf("Enter the position at which the node must be deleted");
    scanf("%d",&position);

    while(position != 1)
    {
        n->next = current->next;
        current = current->next;
        position--;
    }
    n->next = current->next;
    free(current);
    current = NULL;
}

void delete_entire_list(struct node* head)
{
    free(head);
}


int main()
{
    struct node* head;

    int n;
    printf("Enter the number of elements in linked list");
    scanf("%d",&n);

    int op;
    printf("Enter the option");
    scanf("%d",&op);

    int opt;
    printf("Enter the option to be selected");
    scanf("%d",&opt);

    while(op != 0);
    {
        switch(opt){
        case 1:
        create_linked_list(&head,n);
        case 2:
        create_node_at_beginning(head);
        break;
        case 3:
        create_node_at_end(head);
        break;
        case 4:
        create_node_before_a_node(head);
        break;
        case 5:
        create_node_after_a_node(head);
        break;
        case 6:
        delete_a_node_at_beginning(head);
        break;
        case 7:
        delete_a_node_at_end(head);
        break;
        case 8:
        break;
        case 9:
        break;
        case 10:
        delete_entire_list(head);
        break;
        case 11:
        break;

     }
    }


}