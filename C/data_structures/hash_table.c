# include <stdio.h>
# include <stdlib.h>
# include <string.h>

# define NUM_WORDS 9
# define HASH_NUM_ITEMS 100
# define HASH_SIZE 10000

/* A node in the chained list*/
struct word {
  char key[20];
  int value;

  struct node *next;
};

/* Hash table*/
struct word* table[HASH_SIZE] = {NULL};


/* something picked up
   from http://stackoverflow.com/questions/2624192/good-hash-function-for-strings?lq=1*/

int get_hash(char *string)
{
  int i, hash=7;
  for (i=0; i < strlen(string); i++) {
    hash = hash*31+string[i];
  }
  return hash%HASH_SIZE;

}

int main(int argc, char **argv)
{
  int i, pos;
  struct word *entry, *cur_entry;

  /* Word database*/
  char *words[] = {"hello",
                   "world",
                   "hello",
                   "earth",
                   "hello",
                   "space",
                   "space",
                   "is",
                   "peaceful"};

  /* initialize the hash table.
     Initially set all to NULL
  */
  for(i=0;i<HASH_SIZE;i++)
    table[i] = NULL;

  /*
    Here we will use the hash table to count
    the frequency of words, so the "value"
    corresponds to the count
  */

  for(i=0; i<NUM_WORDS; i++){
    pos = get_hash(words[i]);
    cur_entry = table[pos];
    if(cur_entry == NULL)
      {
        /* New word*/
        entry = malloc(sizeof(struct word));
        strcpy(entry->key, words[i]);
        entry->value = 1;
        entry->next = NULL;
        table[pos] = entry;
      }
    else
      {
        /* Existing word; so increment the counter by 1*/
        cur_entry->value +=1;
      }
  }

  /* print the word counts*/
  for(i=0; i<NUM_WORDS; i++){
    cur_entry = table[get_hash(words[i])];
    printf("%s%d\n", cur_entry->key, cur_entry->value);
  }
  return 0;
}
