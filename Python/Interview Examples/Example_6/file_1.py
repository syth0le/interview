# Задача FIZZBUZZ

# Напишите программу, которая выводит на экран числа от 1 до 100. При этом вместо чисел, кратных трем, программа должна
# выводить слово FIZZ, а вместо чисел, кратных пяти слово BUZZ. Если число кратно и 3 и 5, то выводить FIZZBUZZ

def fizz_buzz():
    for i in range(1, 101):
        res = ''
        if i % 3 == 0:
            res += 'FIZZ'
        if i % 5 == 0:
            res += 'BUZZ'
        if res != '':
            print(res)
        else:
            print(i)


fizz_buzz()
