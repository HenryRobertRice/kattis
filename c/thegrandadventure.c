#include <stdio.h>

int main() {
  int adventures;
  scanf("%d\n", &adventures);
  for (int i = 0; i < adventures; i++ ) {
    char path[101];
    scanf("%s\n", &path[0]);
    char pack[100];
    int index = -1;
    int pass = 1;
    for (int j = 0; j < 100; j++) {
      if (path[j] == '\0') {
        break;
      }
      switch (path[j]) {
        case '$':
          index++;
          pack[index] = '$';
          break;
        case '|':
          index++;
          pack[index] = '|';
          break;
        case '*':
          index++;
          pack[index] = '*';
          break;
        case 't':
          if (index == -1) {
            pass = 0;
            break;
          }
          if (pack[index] == '|') {
            index--;
          }
          else {
            pass = 0;
          }
          break;
        case 'j':
          if (index == -1) {
            pass = 0;
            break;
          }
          if (pack[index] == '*') {
            index--;
          }
          else {
            pass = 0;
          }
          break;
        case 'b':
          if (index == -1) {
            pass = 0;
            break;
          }
          if (pack[index] == '$') {
            index--;
          }
          else {
            pass = 0;
          }
          break;
      }
    }
    if (index != -1) {
      pass = 0;
    }
    if (pass == 1) {
      printf("YES\n");
    }
    else {
      printf("NO\n");
    }
  }
}
