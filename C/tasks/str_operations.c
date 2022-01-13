
#include <stdio.h>
int length(char str[100])
{
    int i=0;
    while(str[i] != '\0')
        i++;
    return i;
}

void copy(char str[100])
{
    int i, l = length(str);
    char cpy[l+1];
    
    for(i=0;i<=l;i++)
        cpy[i] = str[i];
    printf("The duplicated string is: %s", cpy);
}

void com(char str1[100], char str2[100])
{
    int i, val=0;
    i = 0;
    while (str1[i] != '\0' || str2[i] !='\0')
    {
	    if(str1[i] > str2[i])
   	    	val+=1;
	    else  if(str1[i] < str2[i])
   		    val-=1;
   		else if(str1[i] == str2[i])
   		    val=0;
   		i++;
    }
    if(val==0)
        printf("The two strings are equal\n");
    else if(val>0)
        printf("The string 1 is greater than\n");
    else if(val<0)
        printf("The string 2 is greater than\n");
}

void rev(char str[100])
{
    int i,j,l = length(str);
    char rev[l];
    j=0;
    for(i=l-1;i>=0;i--)
    {
        rev[j] = str[i];
        j++;
    }
    rev[j] = '\0';
    printf("The reverse of string is: %s", rev);
}

void concat(char str1[100], char str2[100])
{
    int i,j, l1, l2;
    l1 = length(str1);
    l2 = length(str2);
    char str3[l1+l2];
    for(i=0;i<l1;i++)
        str3[i] = str1[i];
    for(j=0;j<=l2;j++)
        str3[i+j] = str2[j];
    printf("The concatinated string is: %s", str3);
}
void substr(char str[100], int n1, int n2)
{
    char sub[n2-n1];
    int i, j=0, l=length(str);
    if(n2>l||n1>l)
        {
            printf("Invalid limit");
            return;
        }
    for(i=n1-1;i<n2;i++)
    {
        sub[j] = str[i];
        j++;
    }
    printf("The substring is: %s", sub);
}

void main()
{
    int opt, n1, n2, cont=0;
    char str1[100], str2[100];
    do{
    printf("Choose a option: \n1.String copy\n2.String compare\n3.String reverse\n4.String concatenation\n5.Find Substring\n");
    scanf("%d", &opt);
    switch(opt)
    {
        case 1:
            printf("\nEnter a string: ");
            scanf("%s", str1);
            copy(str1);
            break;
        case 2:
            printf("\nEnter the first string: ");
            scanf("%s", str1);
            printf("Enter the second string: ");
            scanf("%s", str2);
            com(str1, str2);
            break;
        case 3:
            printf("\nEnter a string: ");
            scanf("%s", str1);
            rev(str1);
            break;
        case 4:
            printf("\nEnter the first string: ");
            scanf("%s", str1);
            printf("Enter the second string: ");
            scanf("%s", str2);
            concat(str1, str2);
            break;
        case 5:
            printf("\nEnter the a string: ");
            scanf("%s", str1);
            printf("Enter two numbers: ");
            scanf("%d\n%d", &n1, &n2);
            substr(str1, n1, n2);
            break;
        default:
            printf("\nInvalid option\n");
    }
    printf("\nWant to continue(0/1): ");
    scanf("%d", &cont);
    }while(cont);
}
