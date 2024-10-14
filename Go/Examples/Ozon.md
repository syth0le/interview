Что напечатает без запуска?
```go
package main

import (
    "fmt"
)

func main() {
    x := []int{} // cap 0 len 0 []
    x = append(x, 0) // cap 1 len 1 [0]
    x = append(x, 1) // cap 2 len 2 [0 1]
    x = append(x, 2) // cap 4 len 3 [0 1 2]
    y := append(x, 3) // x [0 1 2 3] y [0 1 2 3]
    z := append(x, 4) // x [0 1 2 4] y [0 1 2 3] z [0 1 2 4]
    fmt.Println(y, z) // [0 1 2 4] [0 1 2 4]
}
```
- // [0 1 2 4] [0 1 2 4]
- https://goplay.space/#k2Yn3BX22YK


Что напечатает без запуска?
```go
package main

import (
	"fmt"
)

func main() {
	timeStart := time.Now()
	_, _ = <-worker(), <-worker() // выполняются последовательно
	fmt.Println(int(time.Since(timeStart).Seconds()))
}

func worker() chan int {
	ch := make(chan int)
	go func() {
		time.Sleep(3 * time.Second)
		ch <- 1
	}()
	return ch
}
```
- 6
- https://goplay.space/#BEu-ikVTLGT

В чем здесь проблема?
```go
func main() {
    ch := make(chan int)

    go func() {
        for i := 0; i < 5; i++ {
            ch <- i
        }
        // close(ch) - это я дописал, чтобы решить
    }()

    for n := range ch {
        fmt.Println(n)
    }

    fmt.Printf("done")
}
```
- не выведет done так как нет close channel
- https://goplay.space/#fMhWnlAt2pv

Требуется реализовать функцию zip, которая соединяет элементы двух слайсов в слайс пар
```
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
```
- https://goplay.space/#x9itlhlY2-n


Требуется реализовать функцию, которая генерит int слайс уникальный рандомных чисел:
```go
package main

import (
	"fmt"
)

func main() {
	fmt.Println(uniqRandBEST(10))
    fmt.Println(uniqRandLOW(10))
}

func uniqRandBEST(n int) []int {
  out := make([]int, n)

  seen := make(map[int]struct{})
  inc := 0
  for {
    num := rand.Intn(100)
    if _, ok := seen[num]; ok {
      continue
    }
    seen[num] = struct{}{}
    out[inc] = num
    inc += 1

    if inc == len(out) {
      return out
    }
  }
}

func uniqRandLOW(n int) []int {
  out := make([]int, n)

  seen := make(map[int]struct{})

  for i := 0; i < n; i++ {
    for {
      num := rand.Intn(100)
      if _, ok := seen[num]; ok {
        continue
      }
      seen[num] = struct{}{}
      out[i] = num
      break
    }
  }

  return out
}
```

- сработает ли код?
```go
package main

import (
	"fmt"
)

func main() {
	s := "test"
	println(s[0])
	s[0] = "A"
	println(s)
}
```
- нет 
- cannot assign to s[0] (neither addressable nor a map index expression)
- Доп вопрос: как сделать, чтоб работало s[0] = “A” (через конвертирование в []rune)

Вывести уникальные комбинации пользователя и id товара для всех покупок, совершенных пользователями до того, как их забанили. Отсортировать сначала по имени пользователя, потом по SKU:
```
// user
  id | firstname | lastname | birth
  1  | Ivan      | Petrov   | 1996-05-01
  2  | Anna      | Petrova  | 1999-06-01
  3  | Anna      | Petrova  | 1990-10-02

// purchase
sku| price | user_id | date
1  | 5500  | 1      | 2021-02-15
1  | 5700  | 1       | 2021-01-15
2  | 4000  | 1       | 2021-02-14
3  | 8000  | 2       | 2021-03-01
4  | 400   | 2       | 2021-03-02

// ban_list
user_id | date_from   
1       | 2021-03-08
```

```sql
select distict u.id, p.id from user as u 
join purchase as p on p.user_id=u.id
left join ban_list as b on b.user_id=u.id
where b.date is Null or b.date_from > p.date 
```
- ОТСЮДА ВЗЯТЬ С СОБЕСА ЕЩЕ ПРИМЕР

Дана таблица “orders”:
```
+-----+-----------+------------------------+--------------+
|  id |  user_id  |             created_at |  price_total |
+-----+-----------+------------------------+--------------+
|   1 |       111 |    2024-01-01 10:00:00 |        2 000 |
|   2 |       222 |    2024-01-02 10:00:00 |          100 |
|   3 |       111 |    2024-04-01 10:00:00 |       20 000 |
|   4 |       222 |    2024-05-01 10:00:00 |        5 000 |
|   5 |       333 |    2024-05-02 10:00:00 |       10 000 |
+-----+-----------+------------------------+--------------+
```
Напишите SQL-запрос, который вернёт количество заказов по каждому пользователю с price_total больше или равным 1000 
в таком виде отсортированному по количеству заказов в обратном порядке.

```sql
select user_id, COUNT(*) AS order_count from orders
where price_total >= 1000
group by user_id
order by order_count ASC
```