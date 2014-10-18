# include <stdio.h>
# include <stdlib.h>
# include <string.h>

char *binary;
void getbin(int d)
{
  int dig=0;
  while(d > 0)
    {
      *(binary + dig++) = (d%2) + (int)'0';
      d = d/2;
    }
}

void powerset(char *set)
{
  int n, i, n_pset, j;
  n = strlen(set);
  n_pset = 1<<n;
  binary = malloc(n+1);
  *(binary+n) = '\0';
  
  for(i=0; i<n_pset; i++)
    {
      getbin(i);
      for(j=0;j<n;j++)
	if(binary[j] == '1')
	  printf("%c", set[j]);
      printf("\n");
    }
  
  free(binary);
}

int main(int argc, char **argv)
{
  powerset("abracadabra");
  return 0;
}
