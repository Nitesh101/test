#include<stdio.h>
int main()
{
	int v1,*iptr;
	v1 = 10;
	iptr = &v1;
	printf("%p %d\n ",&v1,v1);
	*iptr = *iptr * 2;
	printf("%p %d\n",&v1,v1);
	printf("%p %d\n",iptr,*iptr);
	return 0;
}

