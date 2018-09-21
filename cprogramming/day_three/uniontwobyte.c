#include<stdio.h>
union twobyte
{
	char ch[2];
	short int sint;
};
int main()
{
	union twobyte byte;
	byte.ch[0]=0x12;
	byte.ch[1]=0x34;
	printf("%p\t%x\n",&byte.ch[0],byte.ch[0]);
	printf("%p\t%x\n",&byte.ch[1],byte.ch[1]);
	printf("%p\t%x\n",&byte.sint,byte.sint);
	return 0;
}

