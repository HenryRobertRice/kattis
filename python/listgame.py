def prime_factors(n):
    pf = 0
    f = 2
    while n > 1:
        while n % f == 0:
            pf += 1
            n /= f
        f += 1
        if f * f > n:
            if n > 1:
                pf += 1
                break
    return pf
print(prime_factors(int(input())))
