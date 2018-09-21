#include<stdio.h>
void fun_mul(int arr[],num, num_elem);
int main()
{
	int i=0;
	int arr[7];
	printf("%d "num);
	scanf("%d",&num);
	while(num != 0 ){
		arr[i] = num;
		i++
		printf("Enter Number: ")
		scanf("%d",&num)
		
	}
	num_elem = i;
	printf("Before calling function: ")
	for(i=0;i<=num_elem;i++)
		printf("%p\t:\t%d\n",&arr[i],arr[i]);
	fun_mul(arr,i);	
	return 0;
}
void fun_mul(int arr[],int num_elem)
{
	int i;
	for (i=0;i<=num_elem;i++)
		arr[i] = arr[i]*2;
	
}

