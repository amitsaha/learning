# include <stdio.h>
# include <stdlib.h>
# include <string.h>

# include <editline/readline.h>

# define EXIT_PROMPT "exit"

int main(int argc, char **argv) {

  puts("Lispy Version 0.0.1");
  puts("Ctrl+C to exit");

  while (1) {
    char *input = readline("(lispy) ");
    add_history(input);

    if (strcmp(input, EXIT_PROMPT) != 0) {
      printf("%s\n", input);
      free(input);
    } else {
      free(input);
      exit(0);
    }
    
  }
  return 0;
}
