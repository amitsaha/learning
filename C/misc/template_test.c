# include <stdio.h>

char *template =
  "Hello %s\n"
  "This is a second line\n";

size_t generate(char *name, char *dest, size_t dest_len) {
  return snprintf(dest, dest_len, template, name);
}

int main(int argc, char **argv) {
  char dest[100];
  generate(argv[1], dest, 100);
  printf("%s", dest);
}
