/* An array based queue implementation*/

# include <stdio.h>
# include <stdlib.h>

# define SIZE 100

int queue[SIZE];

void put(int item);
int get();
void disp();

/* Uninitialized */
int HEAD = -1;
int TAIL = -1;

int success = 0;

void put(int item)
{
  if(TAIL < SIZE-1)
    {
      queue[++TAIL] = item;
      success = 0;

      if (HEAD == -1)
	HEAD = 0;
    }
  else
    success = -1;
}

int get()
{
  int i, removed;
  /* Uninitialized case (HEAD=-1)
     Empty queue (TAIL=-1)
  */
  if(HEAD == -1 || TAIL == -1)
    success = -1;
  else
    {
      removed = queue[HEAD];
      for(i=HEAD; i<=TAIL; i++)
	queue[i] = queue[i+1];

      /* move back the tail*/
      TAIL--;
      success = 0;
      return removed;
    }
}

void disp()
{
  int i;
  for(i=HEAD; i<=TAIL; i++)
    printf("%d\n", queue[i]);
}

int main(int argc, char **argv)
{
  int item = 0;

  /* Keep inserting till the queue is full*/
  while(1)
    {
      put(item++);
      
      if(success == -1)
	{
	  printf("Queue full. Head: %d Tail: %d\n", HEAD, TAIL);
	  break;
	}
    }

  /* Keep removing items from the queue till it is empty*/
  while(1)
    {
      item = get();
      if(success == 0)
	printf("%d\n", item);
      else
	{
	  printf("Queue empty. Head: %d Tail: %d\n", HEAD, TAIL);
	  break;
	}
    }


  /* Display the queue*/
  disp();

  return 0;
}
