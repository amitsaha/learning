# include <stdio.h>
# include <stdlib.h>
# include <string.h>

void reverse(char *str)
{
  int front = 0, tail;
  char temp;
  tail = strlen(str)-1;
  while (front < tail)
    {
      temp = str[tail];
      str[tail] = str[front];
      str[front] = temp;
      front++;
      tail--;
    }
  printf("%s\n", str);
}

int main(int argc, char **argv)
{
  char str[] = "abba";
  reverse(str);
  
  strcpy(str, "madam");
  reverse(str);
  return 0;
}
