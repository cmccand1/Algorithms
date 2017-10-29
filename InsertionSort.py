def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        pos = i
        while pos > 0 and a[pos - 1] > key:
            a[pos] = a[pos - 1]
            pos -= 1
        a[pos] = key
    return a


a = [x for x in range(10, -1, -1)]
print a
print insertion_sort(a)
