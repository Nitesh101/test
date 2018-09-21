#include<stdio.h>
/*
void fun();
int main()
{
	fun();
	fun();
	fun();
	return 0;
}
void fun()
{
	static int v1 = 4,v2 = 6;
	printf("%d %d\n",v1,v2);
	v1++;
	v2++;
}
*/

void fun();
extern int globalval;
int main()
{
	int val;
	val = 10;
	printf("In main, Before call : %d\n",globalval);
	fun(val);
	printf("In main, After call : %d\n",globalval);
	return 0;
}
