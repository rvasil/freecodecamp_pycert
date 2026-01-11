def selection_sort(items: list):
    print("with", items)
    n = len(items)

    # until last 2 elements
    for i in range(n - 1):
        mmin = min(items[i:])
        current = items[i]
        if current > mmin:
            items[i] = mmin  # current to mmin
            # search rest
            for j in range(i + 1, n):
                if items[j] == mmin:
                    items[j] = current
            print(current, mmin, items)
    return items


print(selection_sort([33, 1, 89, 2, 67, 245, -10, -99]))
print(
    selection_sort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92])
)
