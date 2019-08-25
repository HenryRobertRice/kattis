def main():
    for _ in range(int(input())):
        n, m, l = [int(x) for x in input().split()]
        dominoes = [Domino() for i in range(n)]
        for i in range(m):
            n1, n2 = [int(x) for x in input().split()]
            dominoes[n1 - 1].adj.append(dominoes[n2 - 1])
        for i in range(l):
            dominoes[int(input()) - 1].topple()
        toppled = 0
        for d in dominoes:
            if d.visited:
                toppled += 1
        print(toppled)

class Domino:
    def __init__(self):
        self.adj = []
        self.visited = False
    def topple(self):
        self.visited = True
        for d in self.adj:
            if not d.visited:
                d.topple()

if __name__ == "__main__":
    main()
