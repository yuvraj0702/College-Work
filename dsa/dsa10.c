#include<stdio.h>
int main()
{
    int a[10]= {12,24,36,48,72,84,108,120};
    int i,n;
    printf("given array\n");
    for (i=0;i<9;i++)
    {
        printf("%d\t",a[i]);
    }
    printf("element to be inserted\n");
    scanf("%d",&n);
    printf("updated array\n");
    for(i=0;i<10;i++)
    {
        printf("%d\t",a[i]);
    }
}