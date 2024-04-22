//total expense
#include‹stdio.h>
int main(){
int quan, dis;
float pri, tot;
printf("Enter quantity and price per item: ");
scanf ("%d%f", &quan, &pri);
if (quan>1000)
dis = 10;
else
dis = 0;
tot = (quan*pri) - ((quan*pri)*dis/100);
printf("The total expense is: %f", tot);
return 0;
}