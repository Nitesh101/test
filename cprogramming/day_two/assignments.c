
#include<stdio.h>
// 1
int main(void)
{
	int num,arr[15],i,j;
	printf("enter a decimal value: ");
	scanf("%d",&num);
	i = 0;
	while (num>0)
	{
		arr[i] = num%2;
		num/=2;
		i++;
	}
	printf("Binary number us : ");
	for(j=i-1; j>=0;j--)
		printf("%d",arr[j]);
	printf("\n");
	return 0;
}
/*
//2.
//2.1 string length
#include<stdio.h>
#include<string.h>
int main()
{
	char str[20];
	printf("enter a string value: ");
       	fgets(str);
	printf("lenth of string: %u\n",strlen(str));
	return 0;
}


//2.2 strin cmp,cpy
int main()
{
	char str1[10],str[20];
	printf("please enter a strings: ");
	fgets(str1);
	fgets(str2);
	if((strcmp(str1,str2))==0);
		printf("strins are same");
	else
		print ("string is not same");
	strcpy(str2,"Hyderabad");
		printf("str1:%s\t\tstr2:%s\n")
}

//2.3 string char
#include<stdio.h>
#include<string.h>
int main()
{
	char str1[10];
	printf("enter a string ");
	(str1);
	//puts(str1);
	return 0;
}
*/

