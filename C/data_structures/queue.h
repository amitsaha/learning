# include <stdio.h>
# include <stdlib.h>

struct node {
  int data;
  struct node *next;
};

void enqueue(int data);
int dequeue();
