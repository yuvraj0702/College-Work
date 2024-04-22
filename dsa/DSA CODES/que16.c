//octal value
#include ‹ stdio.h>
int main()
int i, rem = 0, 9, oct = 0;
printf ("Enter an integer:- ");
scanf("%d", &i);
q= i；
/ finding the remainder while (q
1= 0)
{
rem = (rem * 10) + q % 8;
q = 9 / 8;
}
/ finding the octal value while (rem != 0)
{
oct = oct * 10 + rem % 10;
rem = rem / 10;
｝
(char [28])"The octal value of %d is %d"
printf("The octal value of %d is %d", i, oct);