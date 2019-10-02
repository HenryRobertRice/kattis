#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>

int dist(int sx, int sy, int house_coords[][2], int h) {
  int min = INT_MAX;
  int temp;
  for (int i = 0; i < h; i++) {
    temp = abs(sx - house_coords[i][0]) + abs(sy - house_coords[i][1]);
    if (temp < min) {
      min = temp;
    }
  }
  return min;
}

int main() {
  int n;
  int s = 0, h = 0;
  scanf("%d", &n);
  int spy_coords[(int)pow(n, 2)][2];
  int house_coords[(int)pow(n, 2)][2];
  char row[n];
  for (int i = 0; i < n; i++) {
    scanf("%s", row);
    for (int j = 0; j < n; j++) {
      if (row[j] == 'H') {
        house_coords[h][0] = i;
        house_coords[h][1] = j;
        h++;
      }
      if (row[j] == 'S') {
        spy_coords[s][0] = i;
        spy_coords[s][1] = j;
        s++;
      }
    }
  }
  int max = 0;
  int temp;
  for (int i = 0; i < s; i++) {
    temp = dist(spy_coords[i][0], spy_coords[i][1], house_coords, h);
    if (temp > max) {
      max = temp;
    }
  }
  printf("%d\n", max);
}
