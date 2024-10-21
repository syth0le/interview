package main

import (
	"fmt"
	"math"
)

// Дан несортированный массив целых чисел nums
// Найти три числа с максимальным произведением,
// вернуть это максимальное произведение.
//
// ограничения:
// 3 <= nums.length <= 10^4
// -1000 <= nums[i] <= 1000
//
// Примеры:
// nums = [1,2,3,4]
// output 24

// Комментарий: в целом можно отсортировать и взять три последних числа
// но тогда сложность будет O(NlogN), а надо O(N)

func main() {
	fmt.Println(maxProductOf3([]int{1, 2, 3, 4}))       // 3*2*4 = 24
	fmt.Println(maxProductOf3([]int{5, 6, 3, 2, 4, 9})) // 9*6*5 = 270
}

// returns max product of three digits
func maxProductOf3(nums []int) int {
	if len(nums) < 3 {
		return 0
	}

	// Инициализируем максимальные числа как наименьшее возможное значение
	max1 := int(math.Inf(-1))
	max2 := int(math.Inf(-1))
	max3 := int(math.Inf(-1))

	// Инициализируем минимальные числа как наибольшее возможное значение
	min1 := int(math.Inf(1))
	min2 := int(math.Inf(1))

	for _, num := range nums {
		// Находим три максимальных числа
		if num > max1 {
			max3 = max2
			max2 = max1
			max1 = num
		} else if num > max2 {
			max3 = max2
			max2 = num
		} else if num > max3 {
			max3 = num
		}

		// Находим два минимальных числа
		if num < min1 {
			min2 = min1
			min1 = num
		} else if num < min2 {
			min2 = num
		}
	}

	resWithMax := max1 * max2 * max3
	resWithMin := min1 * min2 * max3
	if resWithMax > resWithMin {
		return resWithMax
	}

	return resWithMin
}
