//matchsticks gamel #include < stdio.h>
int main()
{
int match = 21, pick, comp;
printf("Rules:-\n1) There are total 21 matchsticks. (n2) Pick 1,2,3 or 4 matchsticks. \n3) Then the computer will p
matchsticks: In");

printf("Total matchsticks = 21\n");

while (1)
{
printf("Pick 1, 2, 3 or 4")

scanf ("%d", &pick);



match = match - pick;



printf("matchsticks remaining = %d\n", match);



comp = 5 - pick;



printf ("Computer picked %d\n", comp);



match = match - comp;



printf("matchsticks remaining = %d\n", match);



if（match == 1）
printf ("Computer picked %d\n", comp);
match = match - comp;
printf("matchsticks remaining = %d\n", match);
if (match == 1)
{
printf("You loose\n");
break;
}
else
{
continue;
}
return o;
｝