class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.adj = []
        self.visited = False

def main():
    for _ in range(int(input())):
        n = int(input())
        nodes = []
        for i in range(n + 2):
            x, y = map(int, input().split())
            nodes.append(Node(x, y))
        for i in range(n + 2):
            for j in range(i + 1, n + 2):
                if dist(nodes[i], nodes[j]) <= 1000:
                    nodes[i].adj.append(nodes[j])
                    nodes[j].adj.append(nodes[i])
        search(nodes[0])
        if nodes[-1].visited:
            print("happy")
        else:
            print("sad")

def search(node):
    node.visited = True
    for n in node.adj:
        if not n.visited:
            search(n)

def dist(n1, n2):
    return abs(n1.x - n2.x) + abs(n1.y - n2.y)

if __name__ == "__main__":
    main()
