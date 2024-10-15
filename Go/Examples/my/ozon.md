### скрининг (марсель)
стандартные вопросы по гошечке
по бд чуть чуть спросил

и задачка:
```go
/*
Напишите программу, которая:

1. Поочередно выполнит http запросы по предложенному списку ссылок
в случае получения http-кода ответа на запрос "200 OK" печатаем на экране "адрес url - ok"
в случае получения http-кода ответа на запрос отличного от "200 OK" либо в случае ошибки печатаем на экране "адрес url - not ok"
*/


package main

import (

)

func main() {
  var urls = []string{
    "http://ozon.ru",
    "https://ozon.ru",
    "http://google.com",
    "http://somesite.com",
    "http://non-existent.domain.tld",
    "https://ya.ru",
    "http://ya.ru",
    "http://ёёёё",
  }

  var wg *sync.WaitGroup
  out := make(chan string)

  for _, url := range url {
      wg.Add(1)
      go func(url string) {
            defer wg.Done()
            err := fetch(url)
            if err != nil {
                out <- "адрес url - ok"
                continue
            }
            out <- "адрес url - not ok"
      }(url)
  }

    go func () {
        wg.Wait()
        close(out)
    }()
    

  for val, _ := range out {
      fmt.Println(val)
  }
}

func fetch(url string) error {
    resp, err := http.Get(url)
    if err != nil {
        return fmt.Errorf("fetch: %w", err)
    }

    if resp.Status == http.StatusOk {
        return nil
    }

    return fmt.Errorf("status not 200: %w", err)
}
```