from math import sqrt, ceil
def adj_primes(p, primes):
    #print("NUM: " + str(p))
    #generate a list of all possible 1-digit changes
    #reject all where the first digit is 0 or any digit is 10
    #reject all that aren't prime
    digits = [int(i) for i in str(p)]
    adj = []
    for i in range(len(digits)):
        for j in range(1, 10):
            new = digits.copy()
            new[i] -= j
            if -1 < new[i] < 10 and new[0] != 0:
                adj.append(new)
            new = digits.copy()
            new[i] += j
            if -1 < new[i] < 10 and new[0] != 0:
                adj.append(new)
    #print("adj: " + str(adj))
    #-1 are ruining my life. get rid of them
    #adj = [a for a in adj if a.count(-1) == 0]
    adj = [int("".join([str(i) for i in a])) for a in adj if a[0] != 0 and a.count(10) == 0 and int("".join([str(i) for i in a])) in primes]
    #print("ADJ: " + str(adj))
    #adj = [a for a in adj if a[0] != 0 and a.count(10) == 0 and a in primes]
    return adj
def is_prime(num):
    if num == 2:
        return True
    for i in range(2, int(ceil(sqrt(num))) + 1):
        if num % i == 0:
            return False
    return True
#generate all 4-digit prime numbers
primes = set()
for i in range(1000, 10000):
    if is_prime(i):
        primes.add(i)
for i in range(int(input())):
    #read nums
    #depth = 1
    #enque all adjacent primes w/ depth = 1
    #while queue not empty:
    #   deque n, d
    #   if dequed n = target, print d
    #   enque all new adjacent primes with depth = d + 1
    #fail
    skip = False
    start, end = [int(x) for x in input().split()]
    if start == end:
        print("0")
        skip = True
    visited = set()
    q = []
    adj = adj_primes(start, primes)
    if adj:
        q.extend([[p, 1] for p in adj])
        #print("Q: " + str(q))
        visited.update(adj)
    possible = False
    index = 0
    while index < len(q) - 1 and not skip:
        #n, d = deque(q)
        index += 1
        n, d = q[index]
        #print("dQ: " + str(q))
        if n == end:
            print(str(d))
            possible = True
            break
        adj = [p for p in adj_primes(n, primes) if p not in visited]
        if adj:
            visited.update(adj)
            q.extend([[p, d + 1] for p in adj])
            #print("Q: " + str(q))
    if not possible and not skip:
        print("Impossible")
