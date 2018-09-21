#include<stdio.h>
int main(){
	char grade = 'B';
	switch(grade){
		case 'A':
			printf("Excellent\n");
			break;
		case 'B' :
		case 'C' :
			printf("well done\n");
			break;
		case 'D' :
			printf("you passed\n");
			break;
		case 'F' :
			printf("Better try again\n");
			break;
		default :
			printf("Invalid grade\n");
	}
	printf("your grade us %c\n",grade);
	return 0;
}
