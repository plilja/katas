from threading import Timer
import time


def _add_to_res(res, n):
    res += [n]


def sleepsort(nums):
    res = []
    for n in nums:
        Timer(n, _add_to_res, (res, n)).start()
    time.sleep(max(nums + [0]) + 1)
    return res


if __name__ == "__main__":
    assert [1,2,3] == sleepsort([2, 1, 3])
    assert [1,2,3] == sleepsort([3, 2, 1])
    assert [3] == sleepsort([3])
    assert [1,2,3,4] == sleepsort([3,4,1,2])
    assert [] == sleepsort([])

