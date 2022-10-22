# You are given an array of strings names, and an array heights that consists of distinct positive integers.
# Both arrays are of length n.
# For each index i, names[i] and heights[i] denote the name and height of the ith person.
# Return names sorted in descending order by the people's heights.

# Input: names = ["Mary","John","Emma"], heights = [180,165,170]
# Output: ["Mary","Emma","John"]
# Explanation: Mary is the tallest, followed by Emma and John.


def sortPeople(names: list[str], heights: list[int]) -> list[str]:
    def quicksort(h):
        length = len(h)
        if length < 2:
            return h
        mid = h[length // 2][1]
        left = []
        right = []
        middle = []
        for i in range(0, length):
            if h[i][1] < mid:
                left.append(h[i])
            elif h[i][1] > mid:
                right.append(h[i])
            else:
                middle.append(h[i])

        return quicksort(right) + middle + quicksort(left)

    data = list(zip(names, heights))
    res = quicksort(data)

    return [item[0] for item in res]
