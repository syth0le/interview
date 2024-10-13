package main

import (
	"fmt"
	"sync"
)

// Задача: есть канал int-ов, куда присылаются N значений.
// Сделать K обработчиков, которые достанут значения, сделают +1 и положат в исходящий канал.
// Потом надо прочитать значения из исходящего канала и напечатать.

func main() {
	inCh := make(chan int)
	outCh := make(chan int)
	wg := sync.WaitGroup{}
	k := 10

	wg.Add(1)
	go func() {
		defer wg.Done()
		for i := 0; i < k; i++ {
			inCh <- i
		}
	}()

	for i := 0; i < k; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			outCh <- 2 * <-inCh
		}()
	}

	go func() {
		wg.Wait()
		close(inCh)
		close(outCh)
	}()

	for val := range outCh {
		fmt.Println(val)
	}
}
