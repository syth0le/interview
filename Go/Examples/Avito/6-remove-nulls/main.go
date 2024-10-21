package main

import (
	"fmt"
)

func main() {
	fmt.Println(moveZeroes([]int{7, 3, 0, 0, 0, 2, 4, 0, 5, 19})) // [7, 3, 2, 4, 5, 19, 0, 0, 0, 0]
	fmt.Println(moveZeroes([]int{7, 3, 2, 4, 0, 0, 0, 0, 5, 19})) // [7, 3, 2, 4, 5, 19, 0, 0, 0, 0]
}

func moveZeroes(nums []int) []int {
	lastNonZeroFoundAt := 0

	for i := 0; i < len(nums); i++ {
		if nums[i] != 0 {
			nums[i], nums[lastNonZeroFoundAt] = nums[lastNonZeroFoundAt], nums[i]
			lastNonZeroFoundAt++
		}
	}

	return nums
}
