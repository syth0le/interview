# когда есть какая-то последовательность запросов, которая упорядочена по времени и надо написать структуру,
# которая может обрабатывать такие запросы


class Structure:
    def __init__(self, queries, cursor=0):
        self._queries = queries
        self._cursor = cursor - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._cursor < len(self._queries) - 1:
            self._cursor += 1
            current = self._queries[self._cursor]
            return self.the_most_important_method(current)
        else:
            raise StopIteration

    def the_most_important_method(self, query):
        # do smth
        _ = self._queries
        return query
