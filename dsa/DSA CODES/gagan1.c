#include <stdio.h>
#include <stdlib.h>

typedef struct node{
    struct node* left;
    int data;
    struct node* right;
}node:

node* create_BT(){
    node* p;
    int key;
    printf("Enter the value of key");
    scanf("%d",&key);

    p=(node*)malloc(sizeof(node));
    p->data = key;
    printf("Enter the left node of%d\n",key);

    p->left = create_BT();
    printf("Enter the right node of %d\n",key);
    p->right = create_BT();
    
    return p;
}

void preorder(node *T)
{
    if(T!=NULL)
    {
        printf("%d",T->data);
        preorder(T->left);
        preorder(T->right);
    }
}

void inorder(node* T)
{
    if(T!=NULL){
        inorder(T->left);
        printf("%d",T->data);
        indorder(T->right);
    }
}

void postorder(node *T)
{
    if(T!=NULL)
    {
        postoder(T->left);
        postoder(T->right);
        printf("%d",T->data);
    }
}

int main()
{
    node *root;
    root = create_BT();

    printf("The preoderbtraversal is:\n");
    preorder(root);

    printf("the inorder traversal is:\n");
    inorder(root);

    printf("the postorder traversal is:\n");
    postorder(root);

    return 0;
}
