#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float dist(float x1, float y1, float x2, float y2) {
  return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
}

int gopher_escapes(float gx, float gy, float dx, float dy, float hx, float hy) {
  return (dist(gx, gy, hx, hy) * 2 <= dist(dx, dy, hx, hy)) ? 1 : 0;
}

int main() {
  float gx, gy, dx, dy;
  scanf("%f %f %f %f", &gx, &gy, &dx, &dy);
  float holes[1000][2];
  float x, y;
  int h = 0;
  while (scanf("%f %f", &x, &y) == 2) {
    holes[h][0] = x;
    holes[h][1] = y;
    h++;
  }
  for (int i = 0; i < h; i++) {
    if (gopher_escapes(gx, gy, dx, dy, holes[i][0], holes[i][1]) == 1) {
      printf("The gopher can escape through the hole at (%.3f,%.3f).\n", holes[i][0], holes[i][1]);
      return 0;
    }
  }
  printf("The gopher cannot escape.\n");
}
