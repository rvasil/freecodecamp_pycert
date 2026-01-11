runs = 0


def quick_sort(numbers: list):
    global runs
    runs += 1
    print(runs, numbers)
    if len(numbers) == 0:
        return []

    pivot_value = numbers[0]

    if len(numbers) == 1:
        return [pivot_value]

    _lower = [e for e in numbers if e < pivot_value]
    _equal = [e for e in numbers if e == pivot_value]
    _greater = [e for e in numbers if e > pivot_value]

    return [*quick_sort(_lower), *_equal, *quick_sort(_greater)]


print(quick_sort([-1, 20, 3, 14, 1, 5]))
