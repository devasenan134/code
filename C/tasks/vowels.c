// Online C compiler to run C program online
#include <stdio.h>
#include<string.h>

int count_v(char str[100])
{
    int i, sumv = 0;
    char c;
    for(i=0;i<strlen(str);i++)
    {   
        c = tolower(str[i]);
        if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
            sumv++;
    }
    return sumv;
}

int count_c(char str[100])
{
    int i, sumc = 0;
    char c;
    for(i=0;i<strlen(str);i++)
    {   
        c = tolower(str[i]);
        if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
            ;
        else
        sumc++;
    }
    return sumc;
}

void main()
{
    char str[100];
    printf("Enter a string: \n");
    gets(str);
    printf("The number of vowels in the string is: %d.\n",count_v(str));
    printf("The number of consonants in the string is: %d.\n",count_c(str));
}