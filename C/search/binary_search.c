/* Binary search in an array*/

# include <stdio.h>
# include <assert.h>

/* Recursive Binary search function that will return
   the position of the item if found in arr,
   else return -1
*/

int r_bsearch(int *arr, int start, int end, int item)
{
  int middle;
  int middle_item;

  if(start>=end)
    return -1;

  middle = (start + end)/2;
  middle_item = *(arr+middle);
  
  if(middle_item == item)
    return middle;
  else
    if(middle_item > item)
      return r_bsearch(arr, start, middle-1, item);
    else
      return r_bsearch(arr, middle+1, end, item);
}

/* Iterative Binary search function that will return
   the position of the item if found in arr,
   else return -1
*/

int bsearch(int *arr, int size, int item)
{
  int middle_item;
  int start = 0, end = size-1;
  int middle;
 
  while(start < end)
    {
      middle = (start + end)/2;   
      printf("Start %d Middle %d End %d\n", start, middle, end);

      middle_item = *(arr+middle);

      if (middle_item == item)
	return middle;
      else
	{
	  if (middle_item > item)
	  {
	    end = middle-1;
	  } 
	  else 
	    start = middle+1;
	}
    }
  return -1;
}
int main(int argc, char **argv)
{
  /* Set up an integer array*/
  int arr[] = {1, 2, 100, 200, 250, 500};

  printf("First search\n");
  assert(bsearch(arr, sizeof(arr)/sizeof(int), 100) == 3);
  printf("Second search\n");
  assert(bsearch(arr, sizeof(arr)/sizeof(int), 1) == 0);
  printf("Third search\n");
  assert(bsearch(arr, sizeof(arr)/sizeof(int), 1000) == -1);

  printf("First search\n");
  assert(r_bsearch(arr, 0, sizeof(arr)/sizeof(int)-1, 100) == 2);
  printf("Second search\n");
  assert(r_bsearch(arr, 0, sizeof(arr)/sizeof(int)-1, 1) == 0);
  printf("Third search\n");
  assert(r_bsearch(arr, 0, sizeof(arr)/sizeof(int)-1, 1000) == -1);
  
  return 0;
}
