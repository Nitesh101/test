#include<stdio.h>
#define EXPR1(v1,v2) v1*v2
#define EXPR2(v1,v2) (v1)*(v2)
#define EXPR3(v1,v2) ((v1)*(v2))
int main()
{
	int res;
	res = EXPR1(3,4);
	printf("%d\n",res);
	res = EXPR2(100,20)/EXPR2(5+5,2);
	printf("%d\n",res);
	res = EXPR3(100,20)/EXPR3(5+5,2);
	printf("%d\n",res);
	return 0;
}
