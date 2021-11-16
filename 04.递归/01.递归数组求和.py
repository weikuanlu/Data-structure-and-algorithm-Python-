def sum_digui(arr):
    if len(arr) == 0:
        return 0
    sum = arr.pop()
    return sum + sum_digui(arr)

if __name__ == "__main__":
    arr = list(range(10))
    result = sum_digui(arr)
    print(result)