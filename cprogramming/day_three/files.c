
//1. writing charecters into file
#ifdef PROGRAM1
#include<stdio.h>
#include<stdlib.h>
int main()
{
	FILE *fptr;
	int ch;
	if((fptr=fopen("sample.txt","w"))==NULL)
	{
		printf("Error in opening file\n");
		exit(1);
	}
	printf("Enter text :\n");
	while((ch=getchar())!=EOF)
		fputc(ch,fptr);
	fclose(fptr);
	return 0;
}
#endif
//2. reading files ====> 
#ifdef PROGRAM2
#include<stdio.h>
#include<stdlib.h>
int main()
{
        FILE *p;
        int ch;
        if((p=fopen("sample.txt","r"))==NULL)
        {
                printf("Error in opening file\n");
                exit(1);
        }
        while((ch=fgetc(p))!=EOF)
                printf("%c",ch);
        fclose(p);
        return 0;
}
#endif

#ifdef PROGRAM3
#include<stdio.h>
#include<string.h>
struct employee
{
	int empid;
	char name[10];
	char emploc[12];
};
int main()
{
	struct employee emp;
	printf("Enter a employee details: ");
	strcpy(emp.name,"nitesh");
	emp.empid=879;
	strcpy(emp.emploc,"banjara");
	printf("Employee name is %s\t Address is %p\n",emp.name,&emp.name);
	printf("Employee id %d\t Address is %p\n",emp.empid,&emp.empid);
	printf("Employee loc is %s\t Address is %p\n",emp.emploc,&emp.emploc);
	return 0;
}
#endif
