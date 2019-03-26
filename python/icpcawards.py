teams = []
for i in range(int(input())):
    teams.append(input().split())
winners = set()
awarded = 0
for team in teams:
    if team[0] not in winners and awarded < 12:
        awarded += 1
        winners.add(team[0])
        print(team[0] + " " + team[1])
