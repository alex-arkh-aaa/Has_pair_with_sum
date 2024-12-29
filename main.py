def has_pair_with_sum(arr, target):
    my_set = set()
    for i in arr:
        if target - i in my_set:
            return True
        else:
            my_set.add(i)
    return False

arr =  [10, 15, 3, 7]
target = 20


print(has_pair_with_sum(arr, target))  # Вывод: True (10 + 7 = 17)