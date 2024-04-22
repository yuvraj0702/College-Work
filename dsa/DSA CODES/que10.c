//overtime pay
#include ‹stdio.h>
v int main()
int o=0, t, count=1;
while（count<=10）
printf("Enter the time(in hours) worked by 10 employees respectively: In", count);
scanf("%d", &t);
1f（t＞40）
{
0 = 0+(t-40);
printf("Employee %d has worked for %d hours\n", count, t);
printf("Overtime pay is Rs.%d\n", 0*120);
else
printf("Since number of hours worked is %d, which is less than 40, therefore no overtime pay for employee %d\n",
count++;
printf("Overtime pay is Rs.%d", 0*120);
return 0;