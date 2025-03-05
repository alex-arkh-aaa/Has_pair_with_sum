def has_pair_with_sum(arr, target):
    my_set = set()
    for i in arr:
        if target - i in my_set:
            return True
        else:
            my_set.add(i)
    return False

