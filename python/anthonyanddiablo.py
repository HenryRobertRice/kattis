from math import sqrt, pi
area, fence = [float(x) for x in raw_input().split()]
#circle is most efficient
perimiter = 2 * pi * sqrt(area / pi)
if fence > perimiter:
  print("Diablo is happy!")
else:
  print("Need more materials!")
