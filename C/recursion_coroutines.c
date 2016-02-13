# include <stdio.h>
# include <libmill.h>

int count = 0;
coroutine void f() {
  printf("Called %d\n", count++);
  go(f());
}


int main() {
  go(f());
}
