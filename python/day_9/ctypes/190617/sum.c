#include <stdio.h>

int sum(int*,int);

int sum(int* a,int len)
{
        int res=0,i=0;
        //int s=sizeof(a);
        //printf("%d\n",s);
        for(i=0;i<len;i++)
        {
                res+=a[i];
        }
        return res;
}

