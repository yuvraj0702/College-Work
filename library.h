#ifndef LIBRARY_H
#define LIBRARY_H

#include<stdbool.h>
typedef struct node
{
    int number;
    struct node * next;
} node;

void addNode (node ** head,int data);
int countNode(node * head);
bool searchNode(node * head,int data);
void insertNodeEnd(node * head,int data);
void deleteNode(node ** head,int data);
int sumNode(node * head);
void display (node * head);
void insertAt(node ** head,int data,int position);
int givePosition(node * head,int data);
void printLastNode(node * head);

#endif