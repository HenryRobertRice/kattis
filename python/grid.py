from collections import deque
from sys import stdin

class Node:
    def __init__(self, num):
        self.num = num
        self.adj = []
        self.visited = False
        self.prev = None

def main():
    n, m = [int(x) for x in stdin.readline().split()]
    nodes = [[Node(int(x)) for x in list(input())] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if i - nodes[i][j].num > -1:
                nodes[i][j].adj.append(nodes[i - nodes[i][j].num][j])
            if i + nodes[i][j].num < n:
                nodes[i][j].adj.append(nodes[i + nodes[i][j].num][j])
            if j - nodes[i][j].num > -1:
                nodes[i][j].adj.append(nodes[i][j - nodes[i][j].num])
            if j + nodes[i][j].num < m:
                nodes[i][j].adj.append(nodes[i][j + nodes[i][j].num])
    bfs(nodes[0][0], nodes[n - 1][m - 1])
    if nodes[n - 1][m - 1].visited:
        steps = -1
        current = nodes[n - 1][m - 1]
        while current is not None:
            steps += 1
            current = current.prev
        print(steps)
    else:
        print(-1)

def bfs(start, goal):
    q = deque()
    start.visited = True
    q.append(start)
    while q:
        current = q.popleft()
        if current == goal:
            return
        for a in current.adj:
            if not a.visited:
                a.visited = True
                a.prev = current
                q.append(a)

if __name__ == "__main__":
    main()
