"""
归并排序： 稳定排序
    时间复杂度：O(nlogn)
"""
def merge(arr,l,m,r):
    # 将 序列arr，分成左右两个子序列，左序列包括m
    left_arr = []
    right_arr = []
    for i in range(l,m+1):
        left_arr.append(arr[i])
    for j in range(m+1,r+1):
        right_arr.append(arr[j])

    # 分别比较左序列和右序列的值，将其排好序（前提是左序列和右序列已经排好序）
    i,j,k = 0,0,l
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

def merge_sort(arr,l,r):
    # 分而治之的思想，将序列拆包，然后再归并
    if l < r:
        m = int((l + r) / 2)
        merge_sort(arr,l,m)
        merge_sort(arr,m+1,r)
        merge(arr,l,m,r)

if __name__ == "__main__":
    arr = [1, 2, 3, 5, 6, 65, 76, 32, 34, 54, 13]
    merge_sort(arr,0,len(arr)-1)
    print(arr)