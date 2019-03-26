log = {}
n = input()
for i in range(n):
  act, name = raw_input().split()
  if not name in log and act == "entry":
    log[name] = "in"
    print(name + " entered")
  elif not name in log:
    log[name] = "out"
    print(name + " exited (ANOMALY)")
  elif act == "entry" and log[name] == "in":
    print(name + " entered (ANOMALY)")
  elif act == "entry":
    print(name + " entered")
    log[name] = "in"
  elif log[name] == "out":
    print(name + " exited (ANOMALY)")
  else:
    print(name + " exited")
    log[name] = "out"
