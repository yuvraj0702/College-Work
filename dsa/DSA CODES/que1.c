
#include ‹stdio.h>

int main(){
4

5
char ch;
6
printf("\nEnter a character from the keyboard: ");
7
scanf("%c", &ch);
8
if(ch>=65 && ch<= 90)
9
printf("The character
is an upercase letter\n");
10
if（ch>=97 && ch=122）
11
printf("The character is a lowercase letter\n");
12
if(ch>=48 && ch<=57)
13
printf("The character is a digit\n");
14
if((ch>=0 && ch<48)|| (ch>57 && ch<65)| (ch>90 && ch<97)||ch>122)
15
printf("The character is a special symbol\n");
16
return 0;
//Determine the character