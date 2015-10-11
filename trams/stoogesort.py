import random


def _stoogesort(li, a, b):
    if li[a] > li[b]:
        li[a], li[b] = li[b], li[a]

    if b - a + 1 >= 3:
        t = (b - a + 1) / 3 
        _stoogesort(li, a, b - t)
        _stoogesort(li, a + t, b)
        _stoogesort(li, a, b - t)
     

def stoogesort(li):
    r = list(li)
    _stoogesort(r, 0, len(r) - 1)
    return r


if __name__ == "__main__":
    assert [1,2,3] == stoogesort([2, 1, 3])
    assert [1,5,20] == stoogesort([20, 5, 1])
    assert [20] == stoogesort([20])
    assert [1,2,3,4,5] == stoogesort([3,4,1,2,5])
    assert [1,1,2,2,3,5,7,9,23,192] == stoogesort([5,7,1,9,23,1,2,192,3,2])
