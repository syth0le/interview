def get_first_matching_object(predicate, objects=[]):
    for item in objects:
        if predicate(item):
            return item
