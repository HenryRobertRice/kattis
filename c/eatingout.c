#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
  int m, a, b, c;
  scanf("%d %d %d %d", &m, &a, &b, &c);
  printf("%s\n", (a + b + c <= 2 * m) ? "possible" : "impossible");
}
