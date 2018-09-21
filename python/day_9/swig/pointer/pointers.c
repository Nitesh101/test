#include <stdio.h>
#include"pointers.h"
int multiplay_array(int b, int n)
{
	int i,a[n];
	for(i = 0; i< n;i++)
		a[i] = a[i] * 2;
	return a[0];
	
}
