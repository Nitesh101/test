#include<stdio.h>
#include<string.h>
struct employee
{
	int empid;
	char empname[10];
	char loc[10];
};
int main()
{
	struct employee emp;
	printf("Enter employee details: \n");
	scanf("%s %d %s",emp.empname,&emp.empid,emp.loc);
//	strcpy(emp.empname,"nitesh");
//	emp.empid=876;
//	strcpy(emp.loc,"Banjlls");
	printf("Employee name: %s\t Address : %p\t\n",emp.empname,&emp.empname);
	printf("Employee id %d\t Address : %p\t\n",emp.empid,&emp.empid);
	printf("Employee loc %s\t Address : %p\t\n",emp.loc,&emp.loc);
	return 0;
}
	
