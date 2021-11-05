"""
选择排序：
    时间复杂度：O(n^2)
"""
def sellectsort(arr_num,n):
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if arr_num[min_index] > arr_num[j]:
                min_index = j
        arr_num[min_index], arr_num[i] = arr_num[i], arr_num[min_index]
    return arr_num

if __name__ == "__main__":
    arr = [1,2,3,5,3,65,76,32,34,54,13]
    arr = sellectsort(arr,len(arr))
    print(arr)