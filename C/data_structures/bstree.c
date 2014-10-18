# include <stdio.h>
# include <stdlib.h>

struct node{
  int data;
  struct node *left;
  struct node *right;
};

struct node *root=NULL, *new_node;

struct node* new(int data)
{
  new_node = malloc(sizeof(struct node));
  new_node->data = data;
  new_node->left = NULL;
  new_node->right = NULL;
  
  return new_node;
}

struct node* insert(struct node* tree_root, int data)
{
  if(tree_root == NULL)
    {
      new_node = new(data);
      if(root==NULL)
	root = new_node;
      return new_node;
    }
  else
    {
      if(tree_root->data >= data)
	  tree_root->left = insert(tree_root->left, data);
      else
	  tree_root->right = insert(tree_root->right, data);
    }
  return tree_root;
}

void build_tree()
{
  int i;
  int arr [] = {5, 4, 10, 2, 15, 11, 30};
  for(i=0; i< sizeof(arr)/sizeof(int); i++)
      insert(root, arr[i]);
}

/* depth first pre-order traversal*/
void pre_trav(struct node *root)
{
  if(root == NULL)
    return;

  printf("%d\n", root->data);
  pre_trav(root->left);
  pre_trav(root->right);
}

/* depth first in-order traversal*/
void inorder_trav(struct node *root)
{
  if(root == NULL)
    return;
  
  inorder_trav(root->left);
  printf("%d\n", root->data);
  inorder_trav(root->right);
}

/* depth first post-order traversal*/
void postorder_trav(struct node *root)
{
  if(root == NULL)
    return;
  
  inorder_trav(root->left);
  inorder_trav(root->right);
  printf("%d\n", root->data);
}

/* Find a data item in the tree*/
void find(struct node* root, int item)
{
  if(root == NULL)
    {
      printf("Not found %d\n", item);
      return;
    }
  if(root->data == item)
    {
      printf("Found %d\n", item);
      return;
    }
  if(item > root->data)
    find(root->right, item);
  else
    find(root->left, item);
}

void find_parent(struct node *root, struct node *target)
{
  /* single node (?)*/
  if(root == target)
    {
      return NULL;
    }
  while(root->left != target && root->right != target)
    {
      if(root->data > target->data)
	find_parent(root->left, target);
      else
	find_parent(root->right, target);
    }
  return root;

}


struct ll_node{
  struct node* data;
  struct ll_node *next;
};
struct ll_node *front=NULL, *rear=NULL;
struct node *dequeued;

void enqueue(struct node *data)
{
  struct ll_node *new_node = malloc(sizeof(struct ll_node));
  new_node->data = data;
  new_node->next = NULL;
  if(rear == NULL)
    rear = new_node;
  if(front == NULL)
    front = new_node;
}

void dequeue()
{
  if(front == NULL)
    return NULL;

  dequeued = front;
  printf("%d ", dequeued->data);

  front = front->next;

  if(front==NULL)
    rear = NULL;

  return dequeued;
}

int queue_notempty()
{
  if(front==NULL || rear==NULL)
    return 0;
  else
    return 1;   
}

/* level traversal of a binary search tree*/
void level_traversal(struct node *root)
{
  if(root == NULL)
    return;

  /* enqueue the root*/
  enqueue(root);


  /* Level traverse all the nodes*/
  while(queue_notempty())
    {
      root = dequeue();
      if(root->left != NULL)
	enqueue(root->left);
      if(root->right != NULL)
	enqueue(root->right);
    }
}

int main(int argc, char **argv)
{
  build_tree();
  printf("Pre order traversal\n");
  pre_trav(root);
  printf("In order traversal\n");
  inorder_trav(root);
  printf("Post order traversal\n");
  postorder_trav(root);

  find(root, 2);
  find(root, 1000);
  return 0;
}


