```go
// что выведет программа?

type Person struct {
    Name string
    Age int
}

func (p *Person) Set(age int) {
    p.Age = age
}

func SetAge(p *Person, age int) {
    p = &Person{
        Name: p.Name,
        Age: age,
    }
}

func main() {
    p := &Person{Name: "John"} //[0xA]
    p.Set(27)
    // SetAge(p, 27)
    
    fmt.Printf("Name: %s, Age: %d\n", p.Name, p.Age)
}
```

```go

[2]int{43, 34}


// что выведет программа
type Person struct {
    Name string
    Age int
}

func SetAge(p *Person, age int) {
    p.Age = age
}

func main() {
    people := make(map[string]*Person)
    people["John"] = &Person{Name: "John"} // John 0
    //people["John"] = Person{Name: "John", Age: 27}
    SetAge(people["John"], 27) // 
    fmt.Printf("Name: %s, Age: %d\n", people["John"].Name, people["John"].Age)
}
```

```go
//Даны n каналов типа chan int. Надо написать функцию, которая смерджит все данные из этих каналов в один и вернет его.

// Мы хотим, чтобы результат работы функции выглядел примерно так:

for num := range joinChannels(a, b, c) {

       fmt.Println(num)
}


func joinChannels(channels ...chan int) chan int {
    outCh := make(chan int)
    
    wg := &sync.WaitGroup{}
    
    wg.Add(len(channels)))
    for _, ch := range channels {
        go func(inCh chan int) {
            defer wg.Done()
            loop:
                for {
                    select {
                       case val, ok := <- inCh:
                           if !ok {
                               break loop
                           }
                           outCh <- val
                    }
                }
        }(ch)
    }
    
    
    go func(){
        wg.Wait()
        defer close(outCh)
    }()
    
    return outCh  
}
```

```go
// Условие задачи 
// Необходимо реализовать конкурентный поиск документов на серверах. Для этого у нас есть сторонняя библиотека с функцией которая осуществляет поиск документов на указанном сервере по указанному запросу.
// 
// search.Search(server string, query string) ([]string, error) 
// 
// У нас есть 3 идентичных сервера (реплики) и задача состоит в том, чтобы конкурентно вызвать эту функцию для всех серверов и вернуть первый успешный ответ от любого из серверов не дожидаясь ответов от других серверов.
// 
// Если какой-то сервер возвращает ошибку, то мы ее игнорируем, дожидаясь успешного ответа от других, но если все сервера ответили ошибкой, то наша функция должна вернуть ошибку, что поиск не удался.

func SearchOnNodes(servers []string, query string) ([]string, error) {
    errChan := make(chan error, len(servers))
    resultChan := make(chan []string)
    defer close(errChan)
    defer close(resultChan)
    
    for _, server := range servers {
        go func(server, query string) {
            result, err := search.Search(server string, query string) ([]string, error)
            if err != nil {
                if _, ok := <- errChan; !ok {
                    errChan <- err
                }
                
                return
            }
            
            if _, ok := <- resultChan; !ok {
                resultChan <- result
            }
            
        }(server, query)
    }
    
    errCounter := 0
    for {
        select {
        case err := <- errChan:
            errCounter++
            if errCounter == len(servers) {
                return nil, fmt.Errorf("search err: %w", err)
            }
        case val := <- resultChan:
            return val, nil
    }
}
    
    
}
```