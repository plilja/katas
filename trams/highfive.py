def high_five():
    try:
        return high_five()
    except RecursionError:
        return 5

print(high_five())
