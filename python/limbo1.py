for _ in range(int(input())):
    l, r = [int(x) for x in input().split()]
    factor = 1
    layer = 1
    # descend left
    factor += l * (l + 1) // 2
    layer += l
    # descend right, knowing what layer we're on
    factor += layer * r + r * (r + 1) // 2
    print(str(factor))
