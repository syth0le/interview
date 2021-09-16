def counter(arr, k):
    counter = 0
    for elem in arr:
        for i in arr:
            if elem - i == k:
                counter += 1

    return counter


def counter2(arr, k):
    count = 0
    n = len(arr)
    # Pick all elements one by one
    for i in range(0, n):

        # See if there is a pair of this picked element
        for j in range(i + 1, n):

            if arr[i] - arr[j] == k or arr[j] - arr[i] == k:
                count += 1

    return count


if __name__ == "__main__":
    arr = [8, 12, 16, 4, 0, 20]
    k = 4
    print(counter(arr, k))
    print(counter2(arr, k))
