# include <stdlib.h>
# include <stdio.h>

float func(float x)
{
  return x*x-3*x+4;
}

float fpoint()
{
  int l = 0, u = 10;
  float mid, f;

  while(l<u)
    {
      mid = (l + (u-l))/2;
      f = func(mid);
      
      if(abs(f - mid) < 1e-20)
	return mid;
      else
	{
	  if(f > mid)
	    u = mid-1;
	  else
	    l = mid+1;
	}
    }
}

int main(int argc, char **argv)
{
  printf("%f\n", fpoint());
}
