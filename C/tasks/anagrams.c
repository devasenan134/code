#include<stdio.h>
#include<string.h>

int anagram(char arr1[], char arr2[])
{
  int char1[256] = {0}, char2[256] = {0}, i=0;
  if(strlen(arr1) != strlen(arr2))
    {
        return 0;
    }
  
  while (arr1[i] != '\0') {
    char1[arr1[i]]++;
    //printf("%d", char1[arr1[i]]);
    i++;
  }
  //printf("\n");
  i = 0;
  while (arr2[i] != '\0') {
    char2[arr2[i]]++;
    //printf("%d", char2[arr2[i]]);
    i++;
  }


  for (i = 0; i < 256; i++)
    if (char1[i] != char2[i])
      return 0;

  return 1;    
}

void main()
{
    char arr1[100], arr2[100];
    int flag = 0;
    printf("Enter the string\n");
    gets(arr1);
    printf("Enter another string\n");
    gets(arr2);
    flag = anagram(arr1, arr2);
    if (flag == 1)
        printf("%s and %s are anagrams.\n", arr1, arr2);
    else
        printf("%s and %s are not anagrams.\n", arr1, arr2);
}