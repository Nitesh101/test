#include<stdio.h>
int main()
{
	int myints[] = {10,20,30,40,50,60,70,80,90,100};
	int *iptr;
	int index;
	for (index = 0;index<10;index++)
		printf("\t%d:\t%d\n",myints[index],myints[index]);
	iptr = myints;
	iptr = iptr+4;
	printf("%p %d\n",iptr,*iptr);
	return 0;
}
