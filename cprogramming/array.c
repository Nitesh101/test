/*#include<stdio.h>
int main()
{
	int i;
	char array[6] = {'h','e','l','l','o','\0'};
	for(i=0;i<10;i++)
	{
		printf("%c\t",array[i]);
		printf("%p\n",&array[i]);
	}
	return 0;
}
*/
#include<stdio.h>
int main()
{
	int i,arr[6];
	printf("enter a elements : ");
	for(i=0;i<6;i++)
	{
		scanf("%d",&arr[i]);
	}
	for(i=0;i<6;i++)
	{
		printf("%d\t",arr[i]);
	}
	return 0;
}
