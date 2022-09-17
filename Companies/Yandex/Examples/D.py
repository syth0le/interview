# написать функцию getAnagrams(['нос', 'сон', 'днесь', 'снедь'])
# [['нос', 'сон'], ['днесь', 'снедь']]

def getAnagrams(lst):
    hashmap = {}
    for item in lst:
        temp = tuple(sorted(item))
        if temp in hashmap:
            hashmap[temp].append(item)
        else:
            hashmap[temp] = [item]
    return list(hashmap.values())


print(getAnagrams(['нос', 'сон', 'днесь', 'снедь']))
