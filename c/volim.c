#include <stdio.h>

int main() {
  int k;
  scanf("%d\n", &k);
  int n;
  scanf("%d\n", &n);
  int time = 0;
  int question;
  char answer;
  //210
  for (int i = 0; i < n; i++) {
    scanf("%d %c\n", &question, &answer);
    time += question;
    if (time >= 210) {
      if (k % 8 == 0) {
        printf("8");
      }
      else {
        printf("%d\n", k % 8);
      }
      break;
    }
    if (answer == 'T') {
      k++;
    }
  }
}
