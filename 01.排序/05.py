def insertsort(arr):
    n = len(arr)
    for i in range(n):
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

if __name__ == "__main__":
    arr = [1,2,3,5,65,76,32,34,54,13]
    print(insertsort(arr))