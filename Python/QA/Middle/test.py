import timeit


class GFG(object):
    __slots__ = 'foo'


class Usual(object):
    pass


def get_set_delete_fn(obj):
    def get_set_delete():
        obj.foo = 'foo'
        obj.foo
        del obj.foo
    return get_set_delete


if __name__ == "__main__":
    instance = GFG()
    instance_2 = Usual()
    instance_2.new = "new"
    print(instance_2.new)
    instance.new = "new"
    print(instance.new)
    print(min(timeit.repeat(get_set_delete_fn(instance))))
    print(min(timeit.repeat(get_set_delete_fn(instance_2))))

