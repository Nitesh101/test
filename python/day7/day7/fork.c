#include<stdio.h>
int val = 10;
int main()
{
	int val;
/*	val =10;*/
	fork();
	fork();
	fork();
	printf("fork printing\n");
	val++;
	printf("value is %d\n",val);
	return 0;
}
