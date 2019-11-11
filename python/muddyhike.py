from sys import stdin, exit
from heapq import heappush, heappop

def main():
    r, c = map(int, input().split())
    graph = [list(stdin.readline().rstrip().split()) for _ in range(r)]
    visited = [[0] * c for _ in range(r)]
    q = []
    max_seen = -1
    for i in range(r):
        heappush(q, [int(graph[i][0]), i, 0])
        visited[i][0] = 1
    while q:
        current = heappop(q)
        i, j = current[1], current[2]
        depth = current[0]
        if depth > max_seen:
            max_seen = depth
        if j + 1 == c:
            print(max_seen)
            exit()
        #enqueue all neighbors
        #up
        if i > 0 and visited[i - 1][j] == 0:
            visited[i - 1][j] = 1
            heappush(q, [int(graph[i - 1][j]), i - 1, j])
        #down
        if i < r - 1 and visited[i + 1][j] == 0:
            visited[i + 1][j] = 1
            heappush(q, [int(graph[i + 1][j]), i + 1, j])
        #left
        if j > 0 and visited[i][j - 1] == 0:
            visited[i][j - 1] = 1
            heappush(q, [int(graph[i][j - 1]), i, j - 1])
        #right
        if j < c - 1 and visited[i][j + 1] == 0:
            visited[i][j + 1] = 1
            heappush(q, [int(graph[i][j + 1]), i, j + 1])

if __name__ == "__main__":
    main()
