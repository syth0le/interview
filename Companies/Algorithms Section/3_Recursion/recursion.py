
def generate(n):
    result = []

    def generate_(left_open, left_closed, accum):
        if not left_open and not left_closed:
            result.append(''.join(accum))
            return
        if left_open:
            accum.append('(')
            generate_(left_open - 1, left_closed, accum)
            accum.pop()
        if left_closed > left_open:
            accum.append(')')
            generate_(left_open, left_closed - 1, accum)
            accum.pop()

    generate_(n, n, [])
    return result

print(generate(3))