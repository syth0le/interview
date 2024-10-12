package main

import (
	"context"
	"fmt"
	"time"
)

// Вводные:
// Функция executeTask может зависнуть.
// В ней не предусмотрен механизм отмены.
// Она не принимает Context или канал с событием отмены как аргумент.

func main() {
	// Задача:
	// Для функции executeTask написать обертку executeTaskWithTimeout.
	// Функция executeTaskWithTimeout принимает аргументом тайм-аут,
	// через который функция executeTask будет отменена.
	// Если executeTask была отменена по тайм-ауту, нужно вернуть ошибку

	executeTask()

	// //////////////////////////////////////////////////////////////////
	ctx := context.Background()
	duration := time.Second * 2

	err := executeTaskWithTimeout(ctx, duration)
	if err != nil {
		fmt.Printf("%v", err)
	}
}

func executeTask() {
	time.Sleep(4 * time.Second)
}

// https://habr.com/ru/companies/pt/articles/764850/

func executeTaskWithTimeout(ctx context.Context, timeout time.Duration) error {
	ctx, cancel := context.WithTimeout(ctx, timeout)
	defer cancel()

	ch := make(chan struct{})

	go func() {
		defer close(ch)

		executeTask()
		ch <- struct{}{}
	}()

	select {
	case <-ch:
		return nil
	case <-ctx.Done():
		return ctx.Err()
	}
}
