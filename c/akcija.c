#include <stdio.h>
#include <stdlib.h>

int cmp(const void *aa, const void *bb) {
  int a = *(int *)aa, b = *(int *)bb;
  if (a < b) {
    return 1;
  }
  else if (a > b) {
    return -1;
  }
  return 0;
}

int main() {
  int num_books;
  scanf("%d\n", &num_books);
  int books[num_books];
  for (int i = 0; i < num_books; i++) {
    scanf("%d\n", &books[i]);
  }
  qsort(books, num_books, sizeof(books[0]), &cmp);
  int total = 0;
  for (int i = 0; i < num_books; i++) {
    if ((i + 1) % 3 != 0) {
      total += books[i];
    }
  }
  printf("%d\n", total);
}
