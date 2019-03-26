import sys
def update(rank):
  if rank >= 21: return 2
  if rank >= 16: return 3
  if rank >= 11: return 4
  return 5
seq = raw_input()
rank = 25
stars = 0
limit = 2
consecutive = 0
for match in seq:
  if match == "W":
    consecutive += 1
    if consecutive >= 3 and rank >= 6:
      stars += 2
    else:
      stars += 1
    if stars > limit:
      stars -= limit
      rank -= 1
      if rank == 0:
        print("Legend")
        sys.exit()
      limit = update(rank)
  else:
    consecutive = 0
    if rank < 20 or (rank == 20 and stars > 0):
      if stars == 0:
        rank += 1
        limit = update(rank)
        stars = limit - 1
      else:
        stars -= 1
print(str(rank))
