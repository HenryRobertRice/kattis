def main():
    for _ in range(int(input())):
        input()
        len_g, len_m = map(int, input().split())
        g_army = list(map(int, input().split()))
        g_army.sort()
        g_index = 0
        m_army = list(map(int, input().split()))
        m_army.sort()
        m_index = 0
        while g_index < len_g and m_index < len_m:
            if m_army[m_index] > g_army[g_index]:
                g_index += 1
            else:
                m_index += 1
        if g_index == len_g:
            print("MechaGodzilla")
        else:
            print("Godzilla")


if __name__ == "__main__":
    main()
