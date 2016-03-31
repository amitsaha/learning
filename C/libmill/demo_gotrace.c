# include <stdio.h>
# include <libmill.h>
# include <string.h>
# include <stdlib.h>
# include <string.h>

coroutine void f(int index, char *text)
{
  msleep(now() + rand() % 50 );
  printf("Worker: %d, Message: %s\n", index, text);
}


int main(int argc, char **argv)
{
  char str[10];
  gotrace(1);
  for(int i=1;i<=10; i++) {
    memset(str, 0, 10);
    sprintf(str, "Text %d", i);
    go(f(i, str));
  }
  msleep(now() + 60);
  return 0;
}
