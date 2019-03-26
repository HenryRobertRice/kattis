d, m = [int(x) for x in input().split()]
cal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
total = 0
for i in range(m - 1):
    total += cal[i]
total += d
days = {1: "Thursday", 2: "Friday", 3: "Saturday", 4: "Sunday", 5: "Monday", 6: "Tuesday", 0: "Wednesday"}
print(days[total % 7])
