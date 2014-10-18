/* Linear search over an array*/

# include <stdio.h>
# include <assert.h>

/* Linear searching function that will return
   the position of the item if found in arr,
   else return -1
*/

int lsearch(int *arr, int size, int item)
{
  int i;
  for(i=0; i<size; i++)
    if(*(arr+i) == item)
      return i;

  return -1;
}
int main(int argc, char **argv)
{
  /* Set up an integer array*/
  int arr[] = {1, 2, -100, 100, 200, 500};

  assert(lsearch(arr, sizeof(arr)/sizeof(int), 100) == 3);
  assert(lsearch(arr, sizeof(arr)/sizeof(int), 1) == 0);
  assert(lsearch(arr, sizeof(arr)/sizeof(int), 1000) == -1);
  
  return 0;
}
