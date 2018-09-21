#include<stdio.h>
int main(){
	char grade = 'A';
	switch(grade){
		case 'A':
			printf("Excelent\n");
			break;
		case 'B':
			printf("welldone\n");
			break;
		case 'c':
			printf("not wll\n");
			break;
		default :
			printf("Invalid grade\n");
	}
	printf("your grade is %c\n",grade);
	return 0;
}
