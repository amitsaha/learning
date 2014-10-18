/* An array based stack implementation*/

# include <stdio.h>

/* Stack size*/
# define SIZE 100

/* Fixed size stack*/
int stack[SIZE];

/* Stack top*/
int stack_top = -1;

/* Function prototypes*/
void push(int item);
int pop();

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
int pop()
{
  if(stack_top >= 0)
    {
    success = 0;
    return stack[stack_top--];
    }
  else
    success = -1;
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
  int item = 1;

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
  while(1)
    {
      item = pop();
      if(success == 0)
  	  printf("%d\n", item);
      else
  	{
  	  printf("Stack empty. Stack top: %d\n", stack_top);
  	  break;
  	}
    }
  return 0;
}

