n = int(input())
nums = list(map(int, input().split()))
target = int(input())


def find_two_sum(n, nums, target):
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return ' '.join([i, hashmap[complement]])
        hashmap[nums[i]] = i


print(find_two_sum(n, nums, target))