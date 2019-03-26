class Node:
    def __init__(self, num):
        self.num = num
        self.squawk = 0
        self.tosend = 0
        self.adj = []
    def transmit(self):
        for a in self.adj:
            a.squawk += self.tosend

def tick(nodes):
    for node in nodes:
        self.tosend = self.squawk
    for node in nodes:
        self.transmit()

def connect(x, y, nodes):
    nodes[x].adj.append(nodes[y])
    nodes[y].adj.append(nodes[x])

nodes = []
users, links, initial, minutes = [int(x) for x in input().split()]
for i in range(users):
    nodes.append(Node(i))
for i in range(links):
    x, y = [int(x) for x in input().split()]
    connect(x, y, nodes)
nodes[initial].squawk = 1
for i in range(minutes):
    for node in nodes:
        node.tosend = node.squawk
        node.squawk = 0
    for node in nodes:
        node.transmit()
print(str(sum([node.squawk for node in nodes])))
