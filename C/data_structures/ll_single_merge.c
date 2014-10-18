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
	  printf("%d   ", trav->data);
	  trav = trav->next;
	}
      printf("\n");
    }
}


struct List* merge(struct List l1, struct List l2)
{
  struct node *merged_head, *merged_trav, *trav_remain;
  struct node *l1_ref, *l2_ref;
  int flag;

  l1_ref = l1.HEAD;
  l2_ref = l2.HEAD;

  /* choose the head of the merged list*/
  if(l1_ref->data>=l2_ref->data)
    {
      merged_head = l2_ref;
      l2_ref = l2_ref->next;
      flag = 2;
    }
  else
    {
      merged_head = l1_ref;
      l1_ref = l1_ref->next;
      flag = 1;
    }

  merged_trav = merged_head;
  while(l1_ref != NULL && l2_ref != NULL)
    {
      if (flag==1)
	{
	  if(l1_ref->data > l2_ref->data)
	    {
	      merged_trav->next = l2_ref;
	      l2_ref = l2_ref->next;
	      flag = 2;
	    }
	  else
	    {
	      l1_ref = l1_ref->next;
	      flag = 1;
	    }
	}
      else{
	  if(l2_ref->data > l1_ref->data)
	    {
	      merged_trav->next = l1_ref;
	      l1_ref = l1_ref->next;
	      flag = 1;
	    }
	  else
	    {
	      l2_ref = l2_ref->next;
	      flag = 2;
	    }
      }
      merged_trav = merged_trav->next;
    }

  if(l1_ref == NULL)
    trav_remain = l2_ref;
  else
    trav_remain = l1_ref;

  merged_trav->next = trav_remain;
  
  printf("Merged\n");
  traverse(merged_head);
}

int main(int argc, char **argv)
{
  int i;

  /* create the first list*/
  struct List l1;
  l1.HEAD = NULL;

  /* Insertions at the end*/
  for(i=1;i<=20;i+=2){
    insert_end(&l1.HEAD, i);
  }

  /* create the second list*/
  struct List l2;
  l2.HEAD = NULL;

  /* Insertions at the end*/
  for(i=2;i<20;i+=4){
    insert_end(&l2.HEAD, i);
  }

  /* Traverse*/
  printf("List 1\n");
  traverse(l1.HEAD);
  
  printf("List 2\n");
  traverse(l2.HEAD);

  merge(l1, l2);

  return 0;
}
