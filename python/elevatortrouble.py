from collections import deque
from sys import exit

def main():
    f, s, g, u, d = map(int, input().split())
    q = deque()
    q.append([s, 0])
    visited = set()
    visited.add(s)
    while q:
        current = q.popleft()
        floor = current[0]
        presses = current[1]
        if floor == g:
            print(presses)
            exit()
        up = floor + u
        if up <= f and up not in visited:
            visited.add(up)
            q.append([up, presses + 1])
        down = floor - d
        if down >= 0 and down not in visited:
            visited.add(down)
            q.append([down, presses + 1])
    print("use the stairs")

if __name__ == "__main__":
    main()
