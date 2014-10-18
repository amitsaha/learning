# include <stdio.h>
# include <stdlib.h>

/* List of neighbors of a vertex*/
struct edges{
  struct vertex *v;
  struct edges *next;
};

/* Adjacency list representation*/
struct vertex
{
  int data;
  struct edges *neighbors;
};

/* List of all vertices*/
struct vertices
{
  struct vertex *v;
  struct vertices *next;
};

struct vertex *new_vertex;
struct edges *neighbors_HEAD=NULL;
struct vertices *new_vertex_node, *vertices_HEAD=NULL;

void reset_neighborlist()
{
  neighbors_HEAD = NULL;
}

void build_neighborlist(struct vertex *v)
{
  struct edges *new_vertex, *trav; 
  new_vertex = malloc(sizeof(struct edges));
  new_vertex->v = v;
  new_vertex->next = NULL;
  
  if(neighbors_HEAD == NULL)
    neighbors_HEAD = new_vertex;
  else
    {
      trav = neighbors_HEAD;
      while(trav->next != NULL)
	trav = trav->next;
      trav->next = new_vertex;    
    }
}

struct vertex* add_vertex(int data, struct edges *neighbors)
{
  struct vertices *trav;

  new_vertex = malloc(sizeof(struct vertex));
  new_vertex->data = data;
  new_vertex->neighbors = neighbors;

  new_vertex_node = malloc(sizeof(struct vertex));
  new_vertex_node->v = new_vertex;
  new_vertex_node->next = NULL;

  if(vertices_HEAD == NULL)
    {
      vertices_HEAD = new_vertex_node;
    }
  else
    {
      trav = vertices_HEAD;
      while(trav->next != NULL)
	trav = trav->next;
      trav->next = new_vertex_node;
    }
  return new_vertex;
}  

void visit_start(struct vertex *start_vertex)
{
  struct edges *neighbors;
  printf("%d ", start_vertex->data);
  neighbors = start_vertex->neighbors;
  if(neighbors == NULL)
    return;
  else
    {
      while(neighbors != NULL)
	{
	  printf("%d ", neighbors->v->data);
	  neighbors = neighbors->next;
	}
      printf("\n");
    }
}


void visit_all()
{
  struct vertices *trav;
  trav = vertices_HEAD;
  while(trav != NULL)
    {
      printf("%d ", trav->v->data);
      trav = trav->next;
    }
}

int main(int argc, char **argv)
{
  struct vertex *vertex1, *vertex2, *vertex3;
  vertex1 = add_vertex(1, NULL);
  vertex2 = add_vertex(2, NULL);

  build_neighborlist(vertex1);
  build_neighborlist(vertex2);

  vertex3 = add_vertex(4, neighbors_HEAD);
  reset_neighborlist();

  visit_start(vertex1);
  visit_start(vertex2);
  visit_start(vertex3);

  visit_all();
}
