def binary_search(key, a, lo, hi):
        mid = lo + (hi - lo) / 2
        if lo > hi:
            return -1
        if key == a[mid]:
            return True
        if key < a[mid]:
            return binary_search(key, a, lo, mid - 1)
        if key > a[mid]:
            return binary_search(key, a, mid + 1, hi)


a = [x for x in range(0, 99999999)]
print binary_search(99999998, a, 0, len(a)-1)
