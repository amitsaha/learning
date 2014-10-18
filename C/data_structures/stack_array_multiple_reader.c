/* An array based stack implementation
   with one writer, but multiple readers.
*/

# include <stdio.h>
# include <pthread.h>
# include <stdlib.h>

/* Stack size*/
# define SIZE 100

/* Fixed size stack*/
int stack[SIZE];

/* Stack top*/
int stack_top = -1;

/* Mutex*/
static pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

/* Function prototypes*/
void push(int item);
void pop(void *);

/* successful operation?*/
int success = 0;

/* Push an integer to the top of the stack*/
void push(int item)
{
  /* Guard against stack overflow*/
  if(stack_top < SIZE-1)
    {
      stack[++stack_top] = item;
      success = 0;
    }
  else
    success = -1;
}

/* Pop an integer off the top of the stock*/
void pop(void *params)
{
  int lock;
  int popped;

  /* Acquire lock*/
  lock = pthread_mutex_lock(&mutex);

  if(lock!=0)
    {
      perror("Error locking mutex\n");
      exit(1);
    }
  else
    {
      if(stack_top >= 0)
	{
	  success = 0;
	  popped = stack[stack_top--];
	}
      else
	success = -1;
    }

  printf("Stack top: %d\n", stack_top);

  /* Unlock mutex*/
  lock = pthread_mutex_unlock(&mutex);
  if(lock!=0)
    {
      perror("Error unlocking mutex\n");
      exit(1);
    }
  else
    {
      if (success==0)
	pthread_exit(popped);
    }
}

/* Display the stack contents, starting from the 
   top*/
void disp()
{
  int i = 0;
  for(i=stack_top; i>=0; i--)
    printf("%d\n", stack[i]);
}

int main(int argc, char **argv)
{
  int item = 1, i;
  int popped;
  pthread_t thread[5];
  int thread_status;

  /* Fill the stack*/
  while(1)
    {
      push(item++);
      if(success == -1)
	{
	  printf("Stack full. Stack top: %d\n", stack_top);
	  break;
	}
    }

  /* Pop till the stack is empty*/
  while(stack_top >= 0)
    {
      for(i=0;i<5;i++)
	{
	  thread_status = pthread_create(&thread[i], NULL, pop, NULL);
	  if(thread_status!=0)
	    {
	      perror("Error creating thread\n");
	      exit(1);
	    }
	  
	}

      /* Wait on the threads*/
      for(i=0;i<5;i++)
	{
	  pthread_join(thread[i], &popped);
	  if(success == 0)
	    {
	      printf("%d\n", popped);
	    }
	}
    }

  return 0;
}

