#include"struct.h"
int structure()
{
	struct emp employ;
	struct emp employ2;
	struct emp employ1={124,"sateesh","gachibowi"};
	employ.empid=123;
	strcpy(employ.name,"arjun");
	strcpy(employ.loc,"hitech-city");
	printf("enter employ2 deatails empid:name:loc:\n");
	scanf("%d %s %s",&employ2.empid,employ2.name,employ2.loc);
	printf("sizeof structure=%ld\n",sizeof(employ));
	printf("sizeof structure=%ld\n",sizeof(employ1));
	printf("%d %s %s\n",employ.empid,employ.name,employ.loc);
	printf("%d %s %s\n",employ1.empid,employ1.name,employ1.loc);
	printf("%p %p %p\n",&employ.empid,&employ.name,&employ.loc);
	printf("%d %s %s\n",employ2.empid,employ2.name,employ2.loc);
	return 0;
}
