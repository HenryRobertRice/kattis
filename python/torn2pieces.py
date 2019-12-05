from collections import deque
from sys import exit

class Node():
    def __init__(self, name):
        self.name = name
        self.adj = []
        self.prev = None
        self.visited = False

def main():
    n = int(input())
    nodes = dict()
    for _ in range(n):
        temp_nodes = input().split()
        for node in temp_nodes:
            if node not in nodes:
                nodes[node] = Node(node)
        for i in range(1, len(temp_nodes)):
            nodes[temp_nodes[0]].adj.append(nodes[temp_nodes[i]])
            nodes[temp_nodes[i]].adj.append(nodes[temp_nodes[0]])
    src, dst = input().split()
    if src not in nodes or dst not in nodes:
        print("no route found")
        exit()
    bfs(nodes[src], nodes[dst])
    if nodes[dst].visited:
        print(path(nodes[dst]))
    else:
        print("no route found")

def path(node):
    names = [node.name]
    while node.prev:
        node = node.prev
        names.append(node.name)
    return " ".join(names[::-1])

def bfs(src, dst):
    src.visited = True
    q = deque([src])
    while q:
        n = q.popleft() 
        if n.name == dst.name:
            return
        for a in n.adj:
            if not a.visited:
                a.visited = True
                a.prev = n
                q.append(a)

if __name__ == "__main__":
    main()
