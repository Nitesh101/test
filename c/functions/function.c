#include<stdio.h>
void Addition();
void main()
{
	printf("\n..........\n");
	Addition();
}
void Addition()
{
	int sum, a = 10, b = 20;
	sum = a+b;
	printf("\n sum of a = %d and b = %d is = %d", a,b,sum);
}
