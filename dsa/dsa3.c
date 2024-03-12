#include <stdio.h>
void main()
{
    char name[2][10],dummy;//2-dimensional character array names is used to store the names of the students 
    int roll_numbers[2],i;
    float marks[2];
    for (i=0;i<3;i++)
    {
        printf("enter the name,roll number,and marks of the students%d,i+1");
        scanf("%s%d%f",&name[i],&roll_numbers[i],&marks[i]);
        scanf("%c",&dummy);//enter will be stored into dummy character at each iteration
    }
    printf("printing the students details...\n");
    for(i=0;i<3;i++)
    {
        printf("%s%d%f\n"),name[i]; 
    } 