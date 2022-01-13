#include <stdio.h>
#include <cs50.h>

void hash(i)
{
    for(int k = 1; k <= i; k++)
        printf("#");
}

int main(void)
{
    int h;
    do
    {
        h = get_int("Height: ");
    }
    while(h < 0 || h > 8);

    for(int i = 1; i <= h; i++)
    {
        for(int j = 1; j <= h - i; j++)
            printf(" ");
        hash(i);
        printf("  ");
        hash(i);
    printf("\n");
    }
}
