import random


def sorted(li):
    if len(li) <= 1:
        return True
    else:
        return li[0] < li[1] and sorted(li[1:])


def bogosort(li):
    li_copy = list(li)
    while not sorted(li_copy):
        random.shuffle(li_copy)
    return li_copy
    

if __name__ == "__main__":
    assert [1,2,3] == bogosort([2, 1, 3])
    assert [1,5,20] == bogosort([20, 5, 1])
    assert [20] == bogosort([20])
    assert [1,2,3,4,5] == bogosort([3,4,1,2,5])
