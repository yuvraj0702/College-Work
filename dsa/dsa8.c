#include<stdio.h>
int main(){
int arr[]={1,2,3,4,5,6,4,8,9,2};
int temp = 0;
for(int i=0;i<10;i++)
{

for(int j=i+1;j<10;j++)
{

temp =arr[i];
if(temp == arr[j])
{
    printf("%d\n",arr[i]);
}

}
}

    return 0;
}