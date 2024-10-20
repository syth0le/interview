```go
// Что выведет следующая программа и почему?

package main

import "fmt"

type Person struct {
    Name string
}



func changeName(person **Person) {
    // person.Name =  "Alice"
    *person = &Person{ [0xB0]
        Name: "Alice",
    }
}

func main() {
    person := &Person{ [0xA0]
        Name: "Bob",
    }
    fmt.Println(person.Name) // Bob
    changeName(person)
    // person.Name = "fsfsdf"
    fmt.Println(person.Name) // Bob (Alice)
}
```

```go
// Что выведет следующая программа и сколько она будет выполняться по времени??

package main

import (
    "fmt"
    "time"
    "sync"
)

const numRequests = 10000

var count int

func networkRequest(mu *sync.Mutex) {
    time.Sleep(time.Millisecond) // Эмуляция сетевого запроса.

    mu.Lock()
    count++
    mu.Unlock()
}

func main() {
    var wg sync.Waitgroup
    mu := &sync.Mutex{}

    wg.Add(numRequests)
    for i := 0; i < numRequests; i++ {
        go func() {
            networkRequest(mu)
            wg.Done()
        }()
    }

    wg.Wait()
    fmt.Println(count)
}
```

```go
// ---
// Есть функция unpredictableFunc, работающая неопределённо долго и возвращающая число. Её тело нельзя изменять (представим, что внутри сетевой запрос).
// Нужно написать обёртку predictableFunc, которая будет работать с заданным фиксированным таймаутом (например, 1 секунду).

package main

import (
    "fmt"
    "math/rand"
    "time"
    "context"
    "log"
)

func init() {
    rand.Seed(time.Now().UnixNano())
}


// Есть функция, работающая неопределённо долго и возвращающая число.
// Её тело нельзя изменять (представим, что внутри сетевой запрос).
func unpredictableFunc() int64 {
    rnd := rand.Int63n(5000)
    time.Sleep(time.Duration(rnd) * time.Millisecond)

    return rnd
}

// Нужно изменить функцию обёртку, которая будет работать с заданным таймаутом (например, 1 секунду).
// Если "длинная" функция отработала за это время - отлично, возвращаем результат.
// Если нет - возвращаем ошибку. Результат работы в этом случае нам не важен.
//
// Дополнительно нужно измерить, сколько выполнялась эта функция (просто вывести в лог).
// Сигнатуру функцию обёртки менять можно.

func predictableFunc(ctx *context.Context, duration time.Duration) (int64, error) {
    startTime := time.Now()
    defer log.Infof("duration: %f", time.Now() - startTime)

    ctx, cancel := context.WithTimeout(ctx, duration)
    defer cancel()

    ch := make(chan int64)
    go func(ctx *context.Context, ch chan int64) {
        defer close(ch)

        select {
            case <- ctx.Done():
                return
            case ch <- unpredictableFunc(ctx):
                return
        }
    }(ctx, ch)

    select {
        case <- ctx.Done():
            return 0, ctx.Err()
        case val := <- ch:
            
            return val, nil
    }
}

func main() {
    fmt.Println("started")
    ctx := context.Background()

    duration := time.Second * 1
    res, err := predictableFunc(ctx, duration)
    if err != nil {
        err := fmt.Errorf("predictable func: %w", err)
        fmt.Println(err)
    }
    fmt.Println(res)
}
```