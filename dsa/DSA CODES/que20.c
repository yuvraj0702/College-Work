//Positive, negative & zero #include ‹stdio.h> int main()
int n, num, pos = 0, neg = 0, zero = 0;
printf("How many numbers do you want to enter:- \n");
scanf ("%d", &n) ;
int i = 1;
while （1<=n）
{
printf("Enter an integer(to end enter end'): - In");
scanf ("%d", &num);
if (num >= 1)
pos = pos + 1;
if
（num == 0）
zero = zero + 1;
if
（num ＜= 1）
neg = neg + 1;
エ++；
}
printf("Count of Positive numbers = %d\n", pos);
printf("Count of Negative numbers = %d\n", neg);
printf("Count of Zeros = %d\n", zero);