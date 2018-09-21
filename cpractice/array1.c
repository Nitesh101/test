//input values into array
#ifdef PROGRAM1
#include<stdio.h>
int main()
{
	int arr[5],i;
	for(i=0;i<5;i++)
	{
		printf("Enter a value for arr[%d] : ",i);
		scanf("%d",&arr[i]);
	}
	printf("The array elements are : \n");
	for(i=0;i<5;i++)
		printf("%d\t",arr[i]);
	printf("\n");
	return 0;
}
#endif
#ifdef PROGRAM2
#include<stdio.h>
int main()
{
	int arr[10],i,sum=0;
	for(i=0;i<10;i++)
	{
		printf("Enter a value for arr[%d]: ",i);
		scanf("%d",&arr[i]);
		sum+=arr[i];
	}
	printf("sum=%d\n",sum);
	printf("%s\t%s\t%s\t%d\t\n",__TIME__,__DATE__,__FILE__,__LINE__);
	
//	printf("%s\n",__DATE__);

//	printf("%s\n",__FILE__);
//
//	printf("%d\n",__LINE__);
	return 0;
}
#endif


