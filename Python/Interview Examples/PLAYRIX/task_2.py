# реализовать функцию partial
# from functools import partial
# basetwo = partial(int, base=2)
# basetwo('10010') -> 18


def partial(func, *args, **kwargs):
    def inner(*fargs, **fkwargs):
        new_kwargs = {**kwargs, **fkwargs}
        return func(*args, *fargs, **new_kwargs)

    inner.func = func
    inner.args = args
    inner.kwargs = kwargs
    return inner


basetwo = partial(int, base=2)
print(basetwo('10010'))

# реализация в модуле functools


def partial(func, *args, **keywords):
    def newfunc(*fargs, **fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*(args + fargs), **newkeywords)
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc
