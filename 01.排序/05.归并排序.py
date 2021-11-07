def merge(arr, l, m, r):
    # 归并 -- 将两个排好序的序列 合并成一个按顺序排放的序列
    left_arr = []
    right_arr = []
    for i in range(l, m + 1):
        left_arr.append(arr[i])
    for j in range(m + 1, r+1):
        right_arr.append(arr[j])

    i, j, k = 0, 0, l
    n1 = len(left_arr)
    n2 = len(right_arr)
    while i < n1 and j < n2:
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = right_arr[j]
        j += 1
        k += 1

def mergesort(arr, l, r):
    if l < r:
        m = int((l + r) / 2)
        mergesort(arr, l, m)
        mergesort(arr, m + 1, r)
        merge(arr, l, m, r)

if __name__ == "__main__":
    arr = [1, 13, 11, 6, 9, 8, 7]
    l = 0
    n = len(arr)  # 7
    mergesort(arr, l, n - 1)
    print(arr)