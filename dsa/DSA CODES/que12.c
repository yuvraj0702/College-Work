//prime or not #include ‹stdio.h>
int main() K
int n,
i,flag = 9；
printf("Enter a positive integer: ");
scanf ("%d", &n);
// 0 and 1 are not prime numbers
/ change flag to 1 for non-prime number
if（n ==OlIn ==1）
flag = 1;
for (i = 2; i ‹= n / 2; ++i) {
if (n % i == 0) {
flag = 1;
break;
｝
}
/ flag is 0 for prime numbers if (flag == 0)
printf("%d is a prime number.", n);
else
printf("%d is not a prime number.", n);
return 0;
}