"""
堆排序：
    时间复杂度：O(nlogn)
"""
def insertsort(arr_num,n):
    for i in range(1,n):
        key = arr_num[i]
        j = i-1
        while j>=0 and key < arr_num[j]:
            arr_num[j+1] = arr_num[j]
            j -= 1
        arr_num[j+1] = key
    return arr_num

if __name__ == "__main__":
    arr = [1,2,3,5,3,65,76,32,34,54,13]
    arr = insertsort(arr,len(arr))
    print(arr)