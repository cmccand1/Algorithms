def selection_sort(a):
    for i in range(0, len(a) - 1):
        _min = i
        for j in range(i + 1, len(a)):
            if a[j] < a[_min]:
                _min = j
        a[_min], a[i] = a[i], a[_min]
    return a


a = [x for x in range(10, -1, -1)]
print a
print selection_sort(a)
