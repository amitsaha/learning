# include <stdio.h>

int count = 0;
void f() {
  printf("Called %d\n", count++);
  f();
}


int main() {
  f();
}
