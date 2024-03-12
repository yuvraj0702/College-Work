#include<stdio.h>
int main()
{
    char t;
    printf("Enter the no. of which you want to print the table : ");
    scanf("%c",&t);
    int table[2][11];
    for(int i=0;i<11;i++)
    {
        table[0][i]= i*2;
    }
    for(int i=0;i<11;i++)
    {
        table[1][i]= i*3;
    }
    switch(t)
    {
    case '2':
    for(int i=0;i<11;i++)
    {
        printf("%d ",table[0][i]);
    }
    break;

    case '3':
    for(int i=0;i<11;i++)
    {
        printf("%d ",table[1][i]);
    }
    break;

    default:
    printf("Enter a valid output");
    }
    }