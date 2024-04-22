// gross salary
#include ‹ stdio.h>
int main()
float bs, da, hra, gs;
printf("Enter basic salary: ");
scanf ("%f", &bs);
if (bs<1500)
hra = (10/100)*bs;
da = (90/100) *bs;
}
if (bs>=1500)
hra = 500;
da = （98/100） *bss
}
gs = bs+hra+da;
printf("Gross Salary = %f", gs);
return 0;