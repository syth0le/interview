# реализовать функцию enumerate
# может принимать как iterable объект, так и генератор.

def enumerate_func(obj):
    i = 0
    for item in obj:
        yield i, item
        i += 1
