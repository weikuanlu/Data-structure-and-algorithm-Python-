def max_search(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        if arr[0] > max_search(arr[1:]):
            return arr[0]
        else:
            return max_search(arr[1:])

if __name__ == "__main__":
    arr = [1,23,43,12,44]
    result = max_search(arr)
    print(result)