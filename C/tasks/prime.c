// Online C compiler to run C program online
#include <stdio.h>

void find_prime(int num1, int num2)
{
    int i, j, prime;
    for(i=num1;i<=num2;i++)
    {   
        prime = 1;
        if(i == 1)
        {   printf("1 is prime\n");
            continue;
        }
        for(j=2;j<i;j++)
        {
            if(i%j == 0)
            {   
                prime = 0;
                break;
            }
        }
        if(prime == 0)
            printf("%d is not prime\n", i);
        else
            printf("%d is prime\n", i);
    }
}

void main()
{
    int n1, n2;
    printf("Enter a starting number to find prime numbers: \n");
    scanf("%d", &n1);
    printf("Enter a end number to find prime numbers: \n");
    scanf("%d", &n2);
    find_prime(n1, n2);
}
