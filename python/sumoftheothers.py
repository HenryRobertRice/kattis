from sys import stdin

def main():
    for line in stdin:
        process([int(x) for x in line.split()])

def process(nums):
    for i in range(len(nums)):
        if nums[i] == sum(nums, -1 * nums[i]):
            print(nums[i])
            return

if __name__ == "__main__":
    main()
