# Найти K ближайших к заданному элементов в отсортированном массиве.
# Моё решение

def binarySearch(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            return mid
    return low


def findKClosestElements(nums, target, k):
    idx = binarySearch(nums, target)

    left = idx - 1
    right = idx
    while k > 0:
        if left < 0 or (right < len(nums) and abs(nums[left] - target) > abs(nums[right] - target)):
            right += 1
        else:
            left -= 1

        k -= 1
    return nums[left + 1: right]


if __name__ == '__main__':
    nums = [10, 12, 15, 17, 18, 20, 25]
    target = 16
    k = 4

    print(findKClosestElements(nums, target, k))