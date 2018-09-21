#include <stdio.h>

int v=0;

void get_address()
{
	printf("Address of v=%p",&v);
}

void set_value(int val)
{
	v=val;
}

