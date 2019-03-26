total = 0.0
for i in range(input()):
  q, t = [float(x) for x in raw_input().split()]
  total += q * t
print(total)
