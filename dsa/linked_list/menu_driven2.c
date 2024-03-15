//to compile: gcc final.c library.c -o final 
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct  node { int number; struct node *next; };
typedef struct node node;

void addNode (node ** head,int data);
int countNode(node * head);
bool searchNode (node * head, int data);
void insertNodeEnd (node * head,int data);
void deleteNode (node ** head, int data);
int sumNodes(node * head);
void Display (node * head);
void insertAt (node ** head, int data,int position);
int givePosition(node * head,int data);
int giveLastNode (node * head);
//give data from position
// int dataFromPosition (node * head,int position)
//to do
//13 march
void add_node_after (node * head,int data,int number);
void add_node_before (node ** head,int data,int number);
void freeList (node * head);
void sort (node * head);
void reverse (node ** head);
bool iscycle (node * head);

int main()
{   
    node * list = NULL;
    int data;
    int givenData;
    bool running = true;
    int choice ;
    do {
        printf("\n1. Create a list\n");
        printf("2. Display the list\n");
        printf("3. Add a node at the beginning\n");
        printf("4. Add a node at the end\n");
        printf("5. Add the node before a given node\n");
        printf("6. Add the node after a given node\n");
        printf("7. Delete a node from the beginning\n");
        printf("8. Delete a node from the end\n");
        printf("9. Delete a given node\n");
        printf("10. print sum of the list\n"); 
        printf("11. Delete the entire list\n");
        printf("12. Sort the list\n");
        printf("13. Reverse the list\n");
        printf("0. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) 
        {
            case 1:
                
                break;
            case 2:
                Display(list);
                break;
            case 3:
                printf("Enter data for the new node: ");
                scanf("%d", &data);
                addNode(&list, data);
                break;
            // Implement other cases similarly
            case 4:
                printf("Enter data for the new node: ");
                scanf("%d", &data);
                insertNodeEnd(list,data);
                break;

            case 5:
                printf("Enter data of the before node: ");
                scanf("%d", &data);
                printf("Enter data for the new node: ");
                scanf("%d", &givenData);
                add_node_before(&list,data,givenData);
            
	            
                break;
            case 6:
	            printf("Enter data of the after node: ");
                scanf("%d", &data);
                printf("Enter data for the new node: ");
                scanf("%d", &givenData);
                add_node_after(list,data,givenData);
                break;

            case 7:
	            data = list->number;
                deleteNode(&list,data);
                break;

            case 8:
                data = giveLastNode(list);
                deleteNode(&list,data);
                break;

            case 9:
                printf("Enter data to delete node: ");
                scanf("%d", &data);
	            deleteNode(&list,data);
                break;

            case 10:
	            printf("%d\n",sumNodes(list));
                break;
            
            case 11:
	            freeList (list);
                break;
            
            case 12:
	            sort(list);
                break;
            
            case 13:
	            reverse(&list);
                break;

            case 0:
	            running = false;
                break;

            default:
                printf("Invalid choice. Please try again.\n");
        }
    } while (running);

}


void addNode (node ** head,int data)
{
    node * new_node = malloc(sizeof(node));
    new_node ->number = data;
    new_node ->next = *head;
    *head = new_node;
}

//create a function  to count nodes ,, valid for circular linked list as well
 int countNode(node * head)
{
    int count = 0;
    node * ptr = head;
    do
    {
        count++;
        head = head->next;
    }while (head != NULL && head != ptr);
    return count;
    
}

//create a search function
bool searchNode (node * head, int data)
{
    while (head != NULL)
    {
        if (data == head->number)
        {
            return true;
        }
        head = head->next;
        
    }
    return false;
}

//function to insert at the end
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

//to calculate sum of all the data in linked list
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

//delete node
void deleteNode (node ** head, int data)
{
    //here we're taking double pointer beacause if we have to remove first node than we have to change the list pointer(the pointer pointing towards the list aka the very first pointer) itself.
    node * ptr = *head;
    node * temp = NULL;
    while (ptr != NULL)
    {
        if ((*head)->number == data)
        {
            temp = *head;
            *head = (*head)->next;
            free(temp);
            return;
        }
        
        if (ptr->number == data)
        {   
            temp->next = ptr->next;
            free(ptr);
            return;
        }   
        temp = ptr;
        ptr = ptr->next;
    }
    
}

//TO display the linked list,, valid for circular linked list as well
 void Display (node * head)
{
    node * ptr = head;
    do
    {
        printf("%d\n",ptr->number);
        ptr = ptr->next;
    }while(ptr != NULL && ptr != head);

}

//To insert node at particular location
void insertAt (node ** head, int data,int position)
{
    node * ptr = *head;
    node * temp = NULL;
    int count = 1;

    node * n = malloc(sizeof(node));
    if(n == NULL)
    {
        free(n);
        printf("memory allocation failed\n");
        return;
    }
    n->next = NULL;
    n->number = data;

    if (position == 1)
    {
        n->next = *head;
        *head = n;
        return;
    }
    

    while (ptr !=NULL)
    {
        if (count == position)
        {
            temp->next = n;
            n->next = ptr;
        }
        count++;
        temp = ptr;
        ptr = ptr->next;
        
    }
}

//to give the position of a specific node if the given data matches
int givePosition(node * head,int data)
{
    int count = 1;
    node * ptr = head;
    while (ptr != NULL)
    {
        if (ptr->number == data)
        {
            return count;
        }
        count++;
        ptr = ptr->next;
        
    }

    printf("data not found\n");
    return 0;
    
}

//to print the last node of the linked list
 int giveLastNode (node * head)
{
    node * ptr = head;
    while (ptr != NULL)
    {
        if(ptr->next == NULL)
        {
            return ptr->number;
        }
        ptr = ptr->next;
    }
    
}

//to add node after the given data
void add_node_after (node * head,int data,int number)
{
    node * new_node = malloc(sizeof(node));
    if (new_node == NULL) 
    {
        printf("Memory allocation failed\n");
        return;
    }
    new_node -> number = number;
    node * ptr = head;
    while (ptr != NULL)
    {
        if (ptr->number == data)
        {
            break;
        }
        ptr = ptr->next;  
    }
    new_node->next = ptr->next;
    ptr->next = new_node;
    return;
}

//to add node before a given data
void add_node_before (node ** head,int data,int number)
{
    node * new_node = malloc(sizeof(node));
    if (new_node == NULL) 
    {
        printf("Memory allocation failed\n");
        return;
    }
    new_node -> number = number;
    node * ptr = *head;
    node * tmp = ptr;
    if (ptr->number == data)
    {
            new_node->next=*head;
            *head=new_node;
            return;
    }
    
    while (ptr != NULL)
    {
        if (ptr->number == data)
        {
            break;
        }
        tmp = ptr;
        ptr = ptr->next;  
    }
    new_node->next = ptr;
    tmp->next = new_node;
    return;
}

//to free the whole linked list
void freeList(node * head)
{
    node*tmp = head;
    node*ptr = head;
    while (ptr != NULL)
    {
        tmp = ptr;
        ptr=ptr->next;
        free(tmp);
    }
    
}

//to sort a linked list in ascending order 
void sort (node * head)
{
    int temp;
    node * tmp;
    node * ptr = head;
    while (ptr != NULL) 
    {
        tmp = ptr->next; // Initialize tmp to the node after ptr
        while (tmp != NULL) {
            if (ptr->number > tmp->number) {
                // Swap the numbers
                temp = ptr->number;
                ptr->number = tmp->number;
                tmp->number = temp;
            }
            tmp = tmp->next;
        }
        ptr = ptr->next; // Move ptr to the next node
    }
}

void reverse (node ** head)
{
    node * ptr = *head;
    node * temp1 = ptr->next;
    node * temp2 = temp1->next;

    ptr->next = NULL;
    while (temp2 != NULL)
    {
        temp1->next = ptr;
        ptr = temp1;
        temp1 = temp2;
        temp2 = temp2->next;
    }  
    temp1->next = ptr;
    *head = temp1;
}

//to check if there is any cycle in linked list
bool iscycle (node * head)
{
    node * slow = head;
    node * fast = head;

    while (fast != NULL && fast->next != NULL )
    {
        fast = fast->next->next;
        if (fast == slow)
        {
            return true;
        }
        slow = slow->next;
    }
    return false;
}
