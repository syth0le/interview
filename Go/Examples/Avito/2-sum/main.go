package main

import (
	"fmt"
)

// two sum
// nums = [2, 7, 11, 15], target=9, result=[0,1]
// nums = [3, 2, 4], target=6, result=[1, 2]

func main() {
	fmt.Println(checkTwoSum([]int{2, 7, 11, 15}, 9))
	fmt.Println(checkTwoSum([]int{3, 2, 4}, 6))
}

func checkTwoSum(arr []int, target int) []int {
	nums := make(map[int]int)
	for idx, item := range arr {
		nums[item] = idx

		searchNum := target - item
		if searchNum == item {
			continue
		}

		if val, ok := nums[searchNum]; ok {
			return []int{val, nums[item]}
		}
	}

	return nil
}
