# Задача 1. Рассмотрим простой алгоритм сжатия строки. Если в строке есть несколько подряд идущих одинаковых подстрок,
# можно заменить их на группу. Например, строку aabaabaab можно записать как 3(aab). Можно алгоритм применить к
# сжатой строке, получив вложенные группы: 3(2ab). Дана сжатая строка, требуется её распаковать. Например,
# для строки a2(a2(bc))3db ответ будет aabcbcabcbcdddb.

string = 'a2(a2(bc))3db'


# string = '3(aab)'
# string = '3db'


def unpack_string(s: str) -> string:
    stack = []
    curNumber = 0
    curString = ''
    for i in range(len(s)):
        item = s[i]
        if item == '(':
            stack.append(curString)
            stack.append(curNumber)
            curString = ''
            curNumber = 0
        elif item == ')':
            num = stack.pop()
            string = stack.pop()
            curString = string + num * curString
        elif item.isdigit():
            curNumber = curNumber * 10 + int(item)
            if s[i+1] != '(':
                curString += s[i+1] * (curNumber - 1)
        else:
            curString += item

    return curString


def unpack_string_recursion(s: str) -> string:

    def _unpack(s, position):
        temp = ''
        i = position
        num = 0
        while i < len(s):
            item = s[i]
            if item.isdigit():
                num = num * 10 + int(item)
                if s[i + 1] != '(':
                    temp += s[i + 1] * (num - 1)
            elif item == '(':
                local, pos = _unpack(s, i+1)
                temp += local*num
                i = pos
                num = 0
            elif item == ')':
                return temp, i
            else:
                temp += item
            i += 1

        return temp, i

    return _unpack(s, 0)[0]


print(unpack_string(string))
print(unpack_string_recursion(string))
