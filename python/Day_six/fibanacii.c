#include<stdio.h>
#include"fact"
int main()
{
	int nterms,i;
	printf("enter a number : ");
	scanf("%d",&nterms);
	for(i=0;i<nterms;i++)
		printf("%d",fib(i));
	printf("\n");
	return 0;
}
