#include <stdio.h>

int palindrome(char arr[], int n)
{
    int i, j=0, flag=0;
    char rev[n];
    for(int i=n-1;i>=0;i--)
    {
        rev[j] = arr[i];
        printf("%c", rev[j]);
        printf(".\n");
        printf("%c", arr[i]);
        printf(".\n");
        j++;
    }
    for(i=0;i<n-1;i++)
        if(rev[i] == arr[i])
            flag=1;
        else
            flag=0;
    if(flag==1)
    return 1;
    else
    return 0;
}

void main()
{
    char arr[100];
    int n,i;
    printf("Enter the number of elements in the array: \n");
    scanf("%d", &n);
    n++;
    printf("Enter the elements of the array: \n");
    for(i=0;i<n;i++)
        arr[i] = getchar();
    printf("\n%d",palindrome(arr, n));
}