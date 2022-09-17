# написать функцию, проверяющую правильность расставленных скобок
# check('(){}[()]') // true
# check('([]}') // false


def check(s):
    temp = s
    while s != '':
        s = s.replace('()', '').replace('{}', '').replace('[]', '')
        if s == temp:
            return False
        temp = s

    return True


print(check('(){}[()]'))
print(check('([]}'))
