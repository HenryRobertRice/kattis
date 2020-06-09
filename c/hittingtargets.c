#include <stdio.h>
#include <math.h>
#include <string.h>

double dist(int x1, int y1, int x2, int y2) {
  return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
}

int hits_rectangle(int x, int y, int x1, int y1, int x2, int y2) {
  return x1 <= x && x <= x2 && y1 <= y && y <= y2;
}

int hits_circle(int x, int y, int x1, int y1, int r) {
  return dist(x, y, x1, y1) <= r;
}

int main() {
  int m;
  int rectangles[120];
  int circles[90];
  int r = 0;
  int c = 0;
  char shape[10];
  scanf("%d\n", &m);
  for (int i = 0; i < m; i++) {
    scanf("%s", shape);
    if (strcmp(shape, "rectangle") == 0) {
      scanf("%d %d %d %d\n", &rectangles[r * 4], &rectangles[r * 4 + 1], &rectangles[r * 4 + 2], &rectangles[r * 4 + 3]);
      r++;
    }
    else {
      scanf("%d %d %d\n", &circles[c * 3], &circles[c * 3 + 1], &circles[c * 3 + 2]);
      c++;
    }
  }
  int n, x, y, output;
  scanf("%d\n", &n);
  for (int i = 0; i < n; i++) {
    output = 0;
    scanf("%d %d\n", &x, &y);
    for (int j = 0; j < r; j++) {
      if (hits_rectangle(x, y, rectangles[j * 4], rectangles[j * 4 + 1], rectangles[j * 4 + 2], rectangles[j * 4 + 3])) {
        output++;
      }
    }
    for (int j = 0; j < c; j++) {
      if (hits_circle(x, y, circles[j * 3], circles[j * 3 + 1], circles[j * 3 + 2])) {
        output++;
      }
    }
    printf("%d\n", output);
  }
}
