package main

import (
	"fmt"
	"sort"
)

// Написать метод (класс и импорты не нужны) на вход которого приходит список слов.
// На выходе надо вернуть список слов, где каждый подсписок содержит слова анаграммы (одинаковые слова слева направо и справа налево).
// ["set"] -> [["set"]]
// ["set", "get"] -> [["set"], ["get"]]
// ["set", "get", "teg"] -> [["get", "teg"], ["set"]]

func main() {
	fmt.Println(groupAnagrams([]string{"set"}))               // [["set"]]
	fmt.Println(groupAnagrams([]string{"set", "get"}))        // [["set"], ["get"]]
	fmt.Println(groupAnagrams([]string{"set", "get", "teg"})) // [["get", "teg"], ["set"]]
}

func groupAnagrams(words []string) [][]string {
	anagramsMap := make(map[string][]string)

	for _, word := range words {
		sortedWord := sortString(word)
		anagramsMap[sortedWord] = append(anagramsMap[sortedWord], word)
	}

	var result [][]string
	for _, group := range anagramsMap {
		result = append(result, group)
	}

	return result
}

func sortString(s string) string {
	// Преобразование строки в руны (символы Unicode)
	runes := []rune(s)
	// Сортировка рун
	sort.Slice(runes, func(i, j int) bool {
		return runes[i] < runes[j]
	})
	// Преобразование отсортированных рун обратно в строку
	return string(runes)
}
