package main

import (
	"fmt"
)

// Мы хотим складывать очень большие числа, которые превышают емкость базовых типов, поэтому мы храним их в виде массива неотрицательных чисел.
// Нужно написать функцию, которая примет на вход два таких массива, вычислит сумму чисел, представленных массивами, и вернет результат в виде такого же массива.

// # Пример 1
// # ввод
// arr1 = [1, 2, 3] # число 123
// arr2 = [4, 5, 6] # число 456
// # вывод
// res = [5, 7, 9] # число 579.
// Допустим ответ с первым незначимым нулем [0, 5, 7, 9]
//
// # Пример 2
// # ввод
// arr1 = [5, 4, 4] # число 544
// arr2 = [4, 5, 6] # число 456
// # вывод
// res = [1, 0, 0, 0] # число 1000
//
// # Пример 3
// # ввод
// arr1 = [8] # число 8
// arr2 = [7] # число 7
// # вывод
// res = [1, 5] # число 15

func main() {
	fmt.Println(sumNumbers([]int{1, 2, 3}, []int{4, 5, 6}))
	fmt.Println(sumNumbers([]int{5, 4, 4}, []int{4, 5, 6}))
	fmt.Println(sumNumbers([]int{8}, []int{7}))
	fmt.Println(sumNumbers([]int{7, 3, 4, 5, 6}, []int{8, 5}))
}

func sumNumbers(arr1, arr2 []int) []int {
	if len(arr1) < len(arr2) {
		arr1, arr2 = arr2, arr1
	}
	res := make([]int, len(arr1)+1)

	carry := 0
	for i := 0; i < len(arr1)+1; i++ {
		currSum := 0
		currSum += carry

		if i < len(arr1) {
			currSum += arr1[len(arr1)-1-i]
		}

		if i < len(arr2) {
			currSum += arr2[len(arr2)-1-i]
		}

		res[len(arr1)-i] = currSum % 10
		carry = currSum / 10
	}

	return res
}
