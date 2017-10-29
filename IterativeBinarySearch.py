def binary_search(key, a):
    
    lo = 0
    hi = len(a) - 1
    found = False

    while lo <= hi and not found:
        mid = lo + (hi - lo) / 2
        if key == a[mid]:
            found = True
        if key < a[mid]:
            hi = mid - 1
        if key > a[mid]:
            lo = mid + 1

    return found


array = [x for x in range(0, 101)]
print array
print binary_search(37, array)
