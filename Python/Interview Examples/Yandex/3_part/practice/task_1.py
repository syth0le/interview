# надо напечатать элементы из 1 последовательности, которых нет во 2 последовательности
# Find the Difference of Two Arrays (Может быть усложнена тем что придется отдавать сразу для двух массивов)
# M - Длина 1го массива, N - Длина 2го массива
# cложность: O(M) + O(N) + O(N) - because 'in' operation is O(1) in python3

def findDifference(nums1: list[int], nums2: list[int]) -> list[int]:
    def count(nums):
        counter = {}
        for item in nums:
            if item not in counter:
                counter[item] = 1
                continue
            counter[item] += 1
        return counter

    cn1 = count(nums1)
    cn2 = count(nums2)

    res1 = [item for item in cn1 if item not in cn2]
    # res2 = [item for item in cn2 if item not in cn1]
    return res1

