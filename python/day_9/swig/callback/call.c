#include<stdio.h>
int func(int, int);
int main(void)
{
    int result;
    /* calling a function named func */
    result = func(10,20);       
    printf("result = %d\n",result);
    return 0;
}
 
/* func definition goes here */
int func(int x, int y)             
{
return x+y;
}
