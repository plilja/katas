def dropsort(li):
    if not li:
        return li
    r = [li[0]]
    for t in li[1:]:
        if t >= r[-1]:
            r += [t]
    return r
    

if __name__ == "__main__":
    assert [2,3] == dropsort([2, 1, 3])
    assert [20] == dropsort([20, 5, 1])
    assert [20] == dropsort([20])
    assert [3,4,5] == dropsort([3,4,1,2,5])
