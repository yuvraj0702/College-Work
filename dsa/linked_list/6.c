#include <stdio.h>
#include <stdbool.h>

void push(int data);
void display();

#define MAX 7
int st[MAX],top=-1;

int main()
{
    char choice;
    

    while (true)
    {
        printf("To add data press y:");
        scanf("%c",&choice);
        printf("\n");
        if( choice != 'y')
        {
            break;
        }
        int data;
        printf("Enter data to input: ");
        scanf("%d",&data);
        getchar();
        push(data);
    }
    display();
    
 
    



}

void push(int data)
{
    if(top == MAX-1)
    {
        printf("stack overflow\n");
        return;
    }
    else
    {
        top++;
        st[top] = data;
        return;
    }

}

void display()
{
       for (int i = top ; i >= 0; i--)
    {
        printf("%d\n",st[i]);
    }
}