package main

import (
	"fmt"
)

func main() {
	fmt.Println(findTopKFrequent([]int{1, 1, 1, 2, 2, 3}, 2)) // 1 2
	fmt.Println(findTopKFrequent([]int{5, 6, 7, 7, 5, 7}, 1)) // 7
}

func findTopKFrequent(arr []int, target int) []int {
	frequency := make(map[int]int)

	for _, num := range arr {
		if _, ok := frequency[num]; !ok {
			frequency[num] = 1
			continue
		}
		frequency[num] += 1
	}

	frequencyByNums := make([][]int, len(arr))
	for k, v := range frequency {
		frequencyByNums[v] = append(frequencyByNums[v], k)
	}

	var result []int
	for i := len(frequencyByNums) - 1; i >= 0; i-- {
		result = append(result, frequencyByNums[i]...)
		if len(result) >= target {
			return result[:target]
		}
	}

	return result
}
