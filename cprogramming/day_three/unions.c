#include<stdio.h>
#include<string.h>
struct employee
{
	int empid;
	char loc[8];
	char name[10];
	union grade 

	{
	int marks;
	char rank[4];
	}
};
int main()
{
	struct employee emp;
	printf("Enter employee details : ");
	scanf("%d %s %s",&emp.empid,emp.loc,emp.name);
	printf("Employee name : %s\t Address : %p\n",emp.name,&emp.name);
	return 0;
}
