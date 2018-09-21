#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#ifdef PROGRAM1
//charecter using fputc

int main()
{
	FILE *p;
	int ch;
	if((p=fopen("sample.txt","w"))==NULL)
	{
		printf("Error opening file");
		exit(1);
	}
	printf("enter a text: ");
	while((ch=getchar())!=EOF)
		fputc(ch,p);
	fclose(p);
	return 0;
}
#endif
#ifdef PROGRAM1_1
//charecter using fgetc
int main()
{
	FILE *p;
	int ch;
	if((p=fopen("sample.txt","r"))==NULL)
	{
		printf("Error opening file \n");
		exit(1);
	}
	while((ch=fgetc(p))!=EOF)
		printf("%c",ch);
	fclose(p);
	return 0;
}
#endif
#ifdef PROGRAM1_2
//string using files
int main()
{
	FILE *p;
	char str[80];
	if((p=fopen("sample.txt","r"))==NULL)
	{
		printf("Error opening file: \n");
		exit(1);
	}
	while(fgets(str,80,p)!=NULL)
		puts(str);
	fclose(p);
	return 0;
}
#endif
#ifdef PROGRAM2
//formated I/O
//fprintf()
int main()
{
	FILE *fp;
	char name[10];
	int age;
	if((fp=fopen("simple.txt","w"))==NULL)
	{
		printf("Error while opening");
		exit(1);
	}
	printf("enter a  text: \n");
	scanf("%s %d",name,&age);
	fprintf(fp,"My name is %s and age is %d",name,age);
	fclose(fp);
	return 0;
}
#endif
#ifdef PROGRAM2_1
struct student
{
	char name[20];
	float marks;
}stu;
int main()
{
	FILE *fp;
	int i,n;
	if((fp=fopen("simple.txt","w"))==NULL)
	{
		printf("Error while opeimg");
		exit(1);
	}
	printf("NAME\tmarks\n");
	while(fscanf(fp,"%s %f",stu.name,&stu.marks)!=EOF)
		printf("%s\t%f\n",stu.name,stu.marks);
	fclose(fp);
	return 0;
}
#endif
#ifdef PROGRAM2_2
//block read/write
struct record
{
	char name[20];
	int roll;
	int marks;
}student;
int main()
{
	int i,n;
	FILE *fp;
	if((fp=fopen("simple.txt","wb"))==NULL)
	{
		printf("Error while opening");
		exit(1);
	}
	printf("Enter a number of records: ");
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		printf("Enter a name : ");
		scanf("%s",student.name);
		printf("Enter a roll no : ");
		scanf("%d",&student.roll);
		printf("Enter a marks : ");
		scanf("%d",&student.marks);
		fwrite(&student,sizeof(student),1,fp);
	}
	fclose(fp);
	return 0;
}
#endif
#ifdef PROGRAM4
struct employee
{
	int empid;
	char empname[10];
	char emploc[10];
};
int main()
{
	struct employee emp;
	printf("enter a employee details : \n");
	strcpy(emp.empname,"nitesh");
	emp.empid=876;
	strcpy(emp.emploc,"banjara");
	printf("Employee name is %s\t Address %p\t\n",emp.empname,&emp.empname);
	printf("Employee loc is %s\t Address %p\t\n",emp.emploc,&emp.emploc);
	printf("Employee id  %d\t Address %p\t\n",emp.empid,&emp.empid);
	return 0;
}
	
#endif
#ifdef PROGRAM5
struct employee
{
	int empid;
	char empname[10];
	char emploc[10];
	union grade
	{
	int marks;
	char rank[4];
	}empgrade;
};
int main()
{
	struct employee emp;
	printf("Enter employee details: ");
	scanf("%s %d %s",emp.empname,&emp.empid,emp.emploc);
	printf("Enter  agrade: ");
	scanf("%d",&emp.empgrade.marks);
	printf("Employee loc is %s\t Address %p\t\n",emp.emploc,&emp.emploc);
	printf("Eyee name is %s\t Address %p\t\n",emp.empname,&emp.empname);
        printf("Employee id  %d\t Address %p\t\n",emp.empid,&emp.empid);
	printf("Employee status : %d",emp.empgrade.marks);
        return 0;

}
#endif


#ifdef PROGRAM6
#include<stdio.h>
int main()
{
	unsigned int i = 4321;
	char *c =(char*)&i;
	if(*c)
		printf("Little endian:");
	else
		printf("Big endian");
	getchar();
	return 0;
}
#endif

#ifdef PROGRAM7
#include<stdio.h>
#include<stdlib.h>

int main(int argc, char * argv[])
{
	int i,sum = 0;
	if(argc==0)
	{
		printf("you have forget to type numbers \n");
		exit(1);
	}
	printf("The sum is: ");
	for(i=0;i<argc;i++)
		sum+=atoi(argv[i]);
	printf("%d\n",sum);
	return 0;
}
#endif










