#include<stdio.h>
#include"fact.h"
long int fact(int n)
{
        int i;
        long int fact=1;
        if(n==0)
                return 1;
        for(i=n; i>1; i--)
                fact*=i;
        return fact;
}
int fib(int n)
{
        if(n==0 || n==1)
                return 1;
        return(fib(n-1) + fib(n-2));
}

