package main

import (
	"fmt"
)

func main() {
	s1, s2 := []int{1, 2, 3}, []int{4, 5, 6, 7, 8}
	fmt.Println(zip(s1, s2)) // [[1 4] [2 5] [3 6]]
}

// я дописал
func zip(arr1, arr2 []int) [][]int {
	if len(arr1) < len(arr2) {
		arr1, arr2 = arr2, arr1
	}

	out := make([][]int, len(arr2))

	for i := 0; i < len(arr2); i++ {
		out[i] = []int{arr2[i], arr1[i]}
	}

	return out
}
