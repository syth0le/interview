# dog dgo -> true
# dog dfo -> false
# doog ddog -> false
# написать функцию, которая возвращает true если в двух строках идентичные символы, но были перестановки


def fill_dict(s: str) -> dict:
    res = {}
    for item in s:
        if item in res:
            res[item] += 1
        else:
            res[item] = 1
    return res


def checker(str_1: str, str_2: str) -> bool:
    dict_1 = fill_dict(str_1)
    dict_2 = fill_dict(str_2)
    return dict_1 == dict_2


print(checker('dog', 'dgo'))
print(checker('dog', 'dfo'))
print(checker('doog', 'ddog'))
