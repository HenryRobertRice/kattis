from collections import deque
from itertools import cycle


class Node():
    def __init__(self, char):
        self.char = char
        self.adj = []
        self.visited = False


def main():
    w, h = map(int, input().split())
    input()
    nodes = []
    for _ in range(h - 2):
        nodes.append([Node(c) for c in input()[1: w - 1]])
    input()
    dirs = [
        [-1, 0],
        [1, 0],
        [0, 1],
        [0, -1]
    ]
    id_ = [0, 0]
    for i1 in range(h - 2):
        for j1 in range(w - 2):
            if nodes[i1][j1].char == "P":
                ip = i1
                jp = j1
            for d in dirs:
                i2 = i1 + d[0]
                j2 = j1 + d[1]
                if in_grid(i2, j2, h, w):
                    nodes[i1][j1].adj.append(nodes[i2][j2])
    print(bfs(nodes[ip][jp]))


def bfs(node):
    gold = 0
    q = deque([node])
    while q:
        visiting = q.popleft()
        visiting.visited = True
        if visiting.char == "G":
            gold += 1
        if is_safe(visiting):
            for a in visiting.adj:
                if not a.visited and is_traversable(a):
                    q.append(a)
                    a.visited = True
    return gold


def is_safe(node):
    return not "T" in [a.char for a in node.adj]


def in_grid(i, j, h, w):
    return i >= 0 and i < h - 2 and j >= 0 and j < w - 2


def is_traversable(node):
    return node.char not in ["T", "#"]


if __name__ == "__main__":
    main()
