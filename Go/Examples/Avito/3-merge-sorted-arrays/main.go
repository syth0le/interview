package main

import (
	"fmt"
)

func main() {
	fmt.Println(mergeSortedArrays([]int{1, 3, 5}, []int{2, 4, 6}))    // 1 2 3 4 5 6
	fmt.Println(mergeSortedArrays([]int{5, 7, 9, 9}, []int{7, 8, 9})) // 5 7 7 8 9 9 9
}

func mergeSortedArrays(arr1, arr2 []int) []int {
	if len(arr1) == 0 {
		return arr2
	}

	if len(arr2) == 0 {
		return arr1
	}

	res := make([]int, len(arr1)+len(arr2))

	idx1 := 0
	idx2 := 0
	for i := 0; i < len(res); i++ {
		if idx1 == len(arr1) {
			res[i] = arr2[idx2]
			idx2++
			continue
		}
		if idx2 == len(arr2) {
			res[i] = arr1[idx1]
			idx1++
			continue
		}

		elem1 := arr1[idx1]
		elem2 := arr2[idx2]
		if elem1 > elem2 {
			res[i] = elem2
			idx2++
			continue
		}
		res[i] = elem1
		idx1++
	}

	return res
}
