# include <stdio.h>
# include <stdlib.h>

/* A node in a linked list*/
struct node{
  int data;
  struct node *next;
};

/*A linked list*/
struct List {
  struct node *HEAD;
  int (*length)(struct node*);
};

/* This function creates a new node
   and returns a pointer pointing to the node
*/
struct node* create_node(int number)
{
  struct node *new;
  new = malloc(sizeof(struct node));
  new->data = number;
  new->next = NULL;

  return new;
}

/* Insert a node at the end of the list pointed to by HEAD
 */
void insert_end(struct node **HEAD, int number)
{
  struct node *trav, *new;

  new = create_node(number);

  if(*HEAD == NULL)
    *HEAD = new;
  else
    {
      trav = *HEAD;
      while(trav->next != NULL)
	trav = trav->next;
      trav->next = new;
    }
}


/* Insert a node at the beginning of the list pointed to by HEAD 
 */
void insert_beg(struct node **HEAD, int number)
{
  struct node *new;
  new = create_node(number);
  
  if (*HEAD==NULL)
    *HEAD = new;
  else
    {
      new->next = *HEAD;
      *HEAD = new;
    }
}


/* Traverse a list starting at HEAD*/
void traverse(struct node *HEAD)
{
  struct node *trav;

  if(HEAD==NULL)
    return;
  else
    {
      trav = HEAD;
      while(trav != NULL)
	{
	  printf("%d \n", trav->data);
	  trav = trav->next;
	}
    }
}

/* Number of nodes in the list starting at HEAD*/
int length(struct node *HEAD)
{
  int count = 0;
  struct node *trav;

  if(HEAD==NULL)
    return;
  else
    {
      trav = HEAD;
      while(trav != NULL)
	{
	  count++;
	  trav = trav->next;
	}
    }
  return count;
}

int main(int argc, char **argv)
{
  int i;

  /* initialize a list object*/
  struct List l1;
  l1.HEAD = NULL;
  l1.length = length;

  /* Insertions at the end*/
  for(i=1;i<=10;i++){
    insert_end(&l1.HEAD, i);
    insert_beg(&l1.HEAD, -i);
  }

  /* Traverse*/
  traverse(l1.HEAD);

  /* print the number of elements*/
  printf("Number of nodes in the list %d\n", l1.length(l1.HEAD));

  return 0;
}
