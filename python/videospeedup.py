n, p, k = map(int , input().split())
latest_timestamp = 0
timestamps = list(map(int, input().split()))
timestamps.append(k)
output = 0.0
factor = 0
for t in timestamps:
    output += (t - latest_timestamp) * (100 + p * factor) / 100
    factor += 1
    latest_timestamp = t
print(output)
