def main():
    nums = [list(map(int, input().split()))[1::]]
    last = nums[-1]
    degree = 0
    while True:
        nums.append(new_row(nums[-1]))
        if len(set(nums[-1])) == 1:
            break
    degree = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        nums[i].append(nums[i][-1] + nums[i + 1][-1])
    print(str(degree) + " " + str(nums[0][-1]))

def new_row(old_row):
    new_row = [old_row[i] - old_row[i - 1] for i in range(1, len(old_row))]
    return new_row

if __name__ == "__main__":
    main()
