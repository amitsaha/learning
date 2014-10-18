# include <stdio.h>

int main(int argc, char **argv)
{
  printf("%d %d\n", __builtin_popcount(5) == 1, (5 & 4) == 0);
  printf("%d %d\n", __builtin_popcount(1024) == 1, (1024 & 1023) == 0);
}
