/* Demo of channels and coroutines */

# include <stdio.h>
# include <libmill.h>

coroutine void f(int index, chan ch)
{
  printf("Worker %d, Message in channel: %s\n", index, chr(ch, char*));
}

int main(int argc, char **argv)
{
  char str[10];
  /* Create an unbuffered channel */
  chan ch = chmake(char*, 0);
  for(int i=1;i<=100000; i++) {
    sprintf(str, "Hello %d", i);
    /* "spawn" a goroutine */
    go(f(i, ch));
    /* Send some data */
    chs(ch, char*, str);
  }

  /* Close channel */
  chclose(ch);
  return 0;
}
