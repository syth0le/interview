#Есть сообщения из соцсети, например:
#"Я работаю в Гугле :-)))"
#"везет :-) а я туда собеседование завалил:-(("
#"лол:)"
#"Ааааа!!!!! :-))(())"
#Хочется удалить из них смайлики, подпадающие под регулярку ":-\)+|:-\(+" за линейное время. То есть, сделать так:
#"Я работаю в Гугле "
#"везет  а я туда собеседование завалил"
#"лол:)"
#"Ааааа!!!!! (())"
#Удалять вложенные смайлики не требуется (как в :-:-)))((( ).


# :-:-)))(((
# :-(((

# jsgsbh4282 -> jsgsbh4282
# jsgsbh4282))) -> jsgsbh4282)))
# test:-:-))) -> test:-
# test:-)( -> test(
# test:)( -> test:)(

# test:-)- -> test-

# test:-): -> test:
# test

def cleaner(s: str) -> str:
    res = ''
    temp = 0
    stack = []
    for i in range(0, len(s)):
        curr = s[i]
        if curr == ':':
            if s[stack[-1]] == ')' or s[stack[-1]] == '(':
                res += s[temp:stack[0]]
                temp = stack[-1] + 1
            stack = [i]
            continue
        if curr == '-' and stack:
            if s[stack[-1]] == ':':
                stack.append(i)
            elif s[stack[-1]] == ')' or s[stack[-1]] == '(':
                res += s[temp:stack[0]]
                temp = stack[-1] + 1
                stack = []
                continue
            else:
                stack = []
        if (curr == ')' or curr='(') and stack:
            if s[stack[-1]] == '-' or s[stack[-1]] == curr:
                stack.append(i)
            else:
                if s[stack[-1]] != ':':
                    res += s[temp:stack[0]]
                    temp = stack[-1] + 1
                stack = []

    res += s[temp:]
    return res
