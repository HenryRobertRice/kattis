from sys import stdin

def main():
    n = 0
    for line1 in stdin:
        line2 = stdin.readline()
        trash = stdin.readline()
        n += 1
        m = [int(x) for x in line1.split()]
        m.extend([int(x) for x in line2.split()])
        if m == []:
            break
        denom = m[0] * m[3] - m[1] * m[2]
        m_inv = [m[3], -1 * m[1], -1 * m[2], m[0]]
        m_inv = [n // denom for n in m_inv]
        print("Case " + str(n) + ":")
        print(str(m_inv[0]) + " " + str(m_inv[1]))
        print(str(m_inv[2]) + " " + str(m_inv[3]))

if __name__ == "__main__":
    main()
