
#include <stdio.h>

void left_arrow(int n)
{
    int i,j,k;
    
    for(i=1;i<=n;i++)
    {
        for(j=1;j<=n-i;j++)
            printf(" ");
        for(k=1;k<=i;k++)
            printf("*");
        printf("\n");
    }
    for(i=n-1;i>0;i--)
    {
        for(j=1;j<=n-i;j++)
            printf(" ");
        for(k=1;k<=i;k++)
            printf("*");
        printf("\n");
    }
}

void alphabets(int n)
{
    int i,j,k=5;
    char alpha[26] = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
    
   for(j=n;j>0;j--)
    {
        for(k=j;k<=n;k++)
            printf("%c", alpha[k-1]);
        printf("\n");
    }
}

void box(int n)
{
    int i,j;
    
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
            if(i==0 || j==0 || i==(n-1) || j==(n-1))
                printf("1");
            else
                printf("0");
        printf("\n");
    }
}

void even_odd(int n)
{
    int i,j;
    
    for(i=n;i>=0;i--)
    {
        for(j=1;j<=i;j++)
            if(i%2 == 0)
                printf("0");
            else
                printf("1");
        printf("\n");
    }
}

void numbers(int n)
{
    int i,j,k, num=1;
    
    for(i=1;i<=n;i++)
    {   
        for(k=1;k<=(n-i);k++)
            printf("   ");
        for(j=1;j<=i;j++)
            {printf("%2d ", num);
            num++;}
            
        printf("\n");
    }
}

void mirrored_right_triangle(int n)
{
    int i,j,k;
    for(i=1;i<=n;i++)
    {
        for(j=1;j<=n-i;j++)
            printf(" ");
        for(k=1;k<=i;k++)
            printf("*");
        printf("\n");
    }
}

void pyramid(int n)
{
    int i,j,k;
    for(i=1;i<=n;i++)
    {
        for(j=1;j<=n-i;j++)
            printf(" ");
        for(k=1;k<=i;k++)
            printf("* ");
        printf("\n");
    }
}

void inverted_pyramid(int n)
{
    int i,j,k;
    for(i=n;i>=0;i--)
    {
        for(j=1;j<=n-i;j++)
            printf(" ");
        for(k=1;k<=i;k++)
            printf("* ");
        printf("\n");
    }
}

void main()
{
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("\n");
    left_arrow(n);
    printf("\n");
    alphabets(n);
    printf("\n");
    box(n);
    printf("\n");
    even_odd(n);
    printf("\n");
    numbers(n);
    printf("\n\nMirrored right triangle pattern:\n\n");
    mirrored_right_triangle(n);
    printf("\n\nPyramid star pattern:\n\n");
    pyramid(n);
    printf("\n\nInverted pyramid star pattern:\n\n");
    inverted_pyramid(n);
}
