cases = input()
for i in range(cases):
  days_in_year, months_in_year = [int(x) for x in raw_input().split()]
  months = [int(x) for x in raw_input().split()]
  #friday % 7 = 6
  #start on sunday
  day_of_year = 0
  fri_13 = 0
  for month in months:
    day_of_month = 0
    for day in range(month):
      day_of_year += 1
      day_of_month += 1
      if day_of_month == 13 and day_of_year % 7 == 6:
        fri_13 += 1
  print(fri_13)
