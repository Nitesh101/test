#include<stdio.h>
void myfun();
int main()
{
	void(*funcptr);
	funcptr = myfun;
	funcptr();
	(*funcptr)(); 
	return o;
}
void myfun()
{
	printf("In myFunc()\n");
	return;
}
