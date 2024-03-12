#include<stdio.h>
int main(void)
{
    int a;
    printf("Enter the size of array\n");
    scanf("%d",&a);
    int numbers[a] ;
    for(int i=0;i<a;i++)
    {
         scanf("%d",numbers[i]);
         
    }
    for(int i=0;i<a;i++)
    {
        printf("%d",numbers[i]);
         
    }
}