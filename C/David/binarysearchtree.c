#include <stdio.h>
#include <stdlib.h>

// represents a node
typedef struct node
{
    int number;
    struct node *left;
    struct node *right;
}
node;