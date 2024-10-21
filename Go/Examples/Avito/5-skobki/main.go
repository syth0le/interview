package main

import (
	"fmt"
)

// # Условие задачи
// Напишите функцию генерирующую все возможные правильные скобочные последовательности из n пар скобок.

// # Входные параметры
// Целое число n - количество пар скобок в последовательности.
// # Вывод
// Список строк, представляющих собой правильные скобочные последовательности
// из n пар скобок.

// # Пример
// Ввод: 3
// Вывод:
// [
//     "((()))",
//     "(()())",
//     "(())()",
//     "()(())",
//     "()()()"
// ]

func main() {
	fmt.Println(generateParentheses(3))
}

func generateParentheses(target int) []string {
	var res []string

	var dfs func(left, right int, s string)
	dfs = func(left, right int, s string) {
		if len(s) == target*2 {
			res = append(res, s)
			return
		}

		if left < target {
			dfs(left+1, right, s+"(")
		}

		if right < target && left > right {
			dfs(left, right+1, s+")")
		}
	}

	dfs(0, 0, "")
	return res
}
