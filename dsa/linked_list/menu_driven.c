#include <stdio.h>
#include <stdlib.h>

struct node{
    int data;
    struct node* next;
};

void create_linked_list(struct node** head, int n)
{
    struct node *fnNode,*tmp;
    fnNode = (struct node*)malloc(sizeof(struct node));

    if(fnNode == NULL)
    {
        printf("The memory has not been allocated");
        return;
    }

    *head = fnNode;

    for(int i=0; i<n; i++)
    {
        int val;
        printf("Enter the values of linked list: ");
        scanf("%d", &val);

        fnNode->data = val;
        fnNode->next = NULL;

        if(i == n - 1)
            break;

        tmp = fnNode;
        fnNode = (struct node*)malloc(sizeof(struct node));
        if(fnNode == NULL)
        {
            printf("The memory has not been allocated");
            return;
        }
        tmp->next = fnNode;
    }
}

void display(struct node* head)
{
    while(head != NULL)
    {
        printf("%d -> ", head->data);
        head = head->next;
    }
    printf("NULL\n");
}

void create_node_at_beginning(struct node** head)
{
    struct node *new_node;
    new_node = (struct node*)malloc(sizeof(struct node));
    
    if(new_node == NULL)
    {
        printf("The memory has not been allocated");
        return;
    }

    int val;
    printf("Enter the value of the node to be inserted at the beginning: ");
    scanf("%d", &val);

    new_node->data = val;
    new_node->next = *head;
    *head = new_node; 
}

void create_node_at_end(struct node** head)
{
    struct node *new_node, *last;

    new_node = (struct node*)malloc(sizeof(struct node));
    if(new_node == NULL)
    {
        printf("The memory has not been allocated");
        return;
    }

    int val;
    printf("Enter the value of the node to be inserted at the end: ");
    scanf("%d", &val);

    new_node->data = val;
    new_node->next = NULL;

    if (*head == NULL) {
        *head = new_node;
        return;
    }

    last = *head;
    while(last->next != NULL)
        last = last->next;
    
    last->next = new_node;
}

void create_node_before_a_node(struct node** head)
{
    struct node *new_node, *ptr, *prev;
    new_node = (struct node*)malloc(sizeof(struct node));
    if(new_node == NULL)
    {
        printf("The memory has not been allocated");
        return;
    }

    int val, pos;
    printf("Enter the value of the node to be inserted: ");
    scanf("%d", &val);

    printf("Enter the position before which the node should be inserted: ");
    scanf("%d", &pos);

    new_node->data = val;
    new_node->next = NULL;

    ptr = *head;
    prev = NULL;
    pos--;
    while(pos != 0 && ptr != NULL)
    {
        prev = ptr;
        ptr = ptr->next;
        pos--;
    }

    if(prev == NULL)
    {
        new_node->next = *head;
        *head = new_node;
    }
    else
    {
        prev->next = new_node;
        new_node->next = ptr;
    }
}

int main()
{
    struct node* head = NULL;

    int n;
    printf("Enter the number of elements in the linked list: ");
    scanf("%d", &n);

    create_linked_list(&head, n);

    printf("Initial linked list: ");
    display(head);

    int op;
    printf("Enter the option: ");
    scanf("%d", &op);

    switch(op) {
        case 1:
            create_node_at_beginning(&head);
            printf("Linked list after inserting at the beginning: ");
            display(head);
            break;
        case 2:
            create_node_at_end(&head);
            printf("Linked list after inserting at the end: ");
            display(head);
            break;
        case 3:
            create_node_before_a_node(&head);
            printf("Linked list after inserting before a node: ");
            display(head);
            break;
        default:
            printf("Invalid option\n");
    }

    return 0;
}

