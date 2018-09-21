#include<stdio.h>
#include"fact.h"
int main(void)
{
	int num;
	printf("Enter a number: ");
	scanf("%d",&num);
	if(num<0)
		printf("no factorial for negetive\n");
	else
		printf("factorial of %d is %ld\n",num,fact(num));
	return 0;
}
