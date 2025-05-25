def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# تجربة الفرز
numbers = [33, 10, 68, 19, 27, 5]
sorted_numbers = quick_sort(numbers)
print("القائمة بعد الفرز:", sorted_numbers)
