#include<stdio.h>
#include<stdlib.h>
struct node {
    int num;
    struct node *nextptr;
}*stnode;
void createnodelist(int n);
void displaylist();
int main()
{
    int n;
    printf("\n\nlinked list:to create and display singly linked list:\n");
    printf("---------------------------------------------------------\n");
    printf("input the number of nodes:");
    scanf("%d",&n);
    createnodelist(n);
    printf("\ndata entered in the list:\n");
    displaylist();
    return 0;

}
void createnodelist(int n){
    struct node*fnnode,*tmp;
    int num,i;
    stnode=(struct node*)malloc(sizeof(struct node));
    if (stnode==NULL){
        printf("memory can not be allocated:");
    }else{
        printf("input data for node1:");
        scanf("%d",&num);
        stnode->num=num;
        stnode->nextptr=NULL;
        tmp=stnode;
        for(i=2;i<=n;i++){
            fnnode=(struct node *)malloc(sizeof(struct node));
            if(fnnode==NULL){
                printf("memory can not be allocated.");
                break;
            }
            else{
                printf("input data for node%d:",i);
                scanf("%d",&num);
                fnnode->num=num;
                fnnode->nextptr=NULL;
                tmp->nextptr=fnnode;
                tmp=tmp->nextptr;
            }
        }
    }
}
void displaylist()
{
    struct node*tmp;
    if (stnode==NULL){
        printf("list is empty.");
    }else{
        tmp=stnode;
        while(tmp!=NULL){
            printf("data=%d\n",tmp->num);
            tmp=tmp->nextptr;
        }
    }
}

                
               
            
        
    



