def linear_search(a, value):
    found = False
    i = 0

    while i < len(a) and not found:
        if a[i] == value:
            found = True
        else:
            i += 1
    return found


a = [x for x in range(100)]
print linear_search(a, 99)
