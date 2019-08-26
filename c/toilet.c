#include <stdio.h>
#include <string.h>

int main() {
  char seq[1001];
  int p1 = 0, p2 = 0, p3 = 0;
  scanf("%s", &seq[0]);
  int len = 0;
  for (int i = 0; i < 1001; i++) {
    if (seq[i] == '\0') {
      break;
    }
    len++;
  }
  char seq1[len], seq2[len];
  strncpy(seq1, seq, len);
  strncpy(seq2, seq, len);
  for (int i = 1; i < 1000; i++) {
    if (seq[i] == '\0') {
      break;
    }
    if (seq[i] != seq[i - 1]) {
      p3++;
    }
    if (seq1[i] != seq1[i - 1]) {
      p1++;
    }
    if (seq2[i] != seq2[i - 1]) {
      p2++;
    }
    if (seq[i] == 'D') {
      p1++;
      seq1[i] = 'U';
    }
    if (seq[i] == 'U') {
      p2++;
      seq2[i] = 'D';
    }
  }
  printf("%d\n%d\n%d\n", p1, p2, p3);
}
