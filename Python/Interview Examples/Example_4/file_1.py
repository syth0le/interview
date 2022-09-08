# что выведет в консоль и почему?
foo = [1, 2, 3, 4]
bar = foo
bar.append(5)
print(foo)

# что сделать чтобы не добавлялась 5 в foo?
foo = [1, 2, 3, 4]
bar = foo.copy()
bar.append(5)
print(foo)
