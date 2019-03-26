class Node:
    def __init__(self, num):
        self.num = num
        self.adj = []
        self.sect = 0
    def connect(self, other):
        self.adj.append(other)
        other.adj.append(self)
    def sectorize(self, secnum):
        self.sect = secnum
        for node in self.adj:
            if node.sect == 0:
                node.sectorize(secnum)
for i in range(int(input())):
    nodes = []
    for j in range(int(input())):
            nodes.append(Node(j))
    for j in range(int(input())):
        p1, p2 = [int(x) for x in input().split()]
        nodes[p1].connect(nodes[p2])
    #mark sectors
    secnum = 1
    for node in nodes:
        if node.sect == 0:
            node.sectorize(secnum)
            secnum += 1
    print(str(secnum - 2))
