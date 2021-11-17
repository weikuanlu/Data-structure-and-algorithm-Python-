"""
选择排序：不稳定排序
    时间复杂度：O(n^2)
"""
def select_sort(arr):
    n = len(arr) # 数组长度
    for i in range(n-1): # 选择前n-1个元素
        min_index = i # 假设为最小元素
        for j in range(i+1,n): # 依次选择后面的元素，与其比较
            if arr[min_index] > arr[j]: # 如果最小元素大于 后面的元素
                min_index = j # 更新最小值 下标

        if i != min_index: # 将实际最小元素 与 最初假设的最小元素 交换
            arr[min_index],arr[i] = arr[i],arr[min_index]

if __name__ == "__main__":
    arr = [1, 2, 3, 5, 6, 65, 76, 32, 34, 54, 13]
    select_sort(arr)
    print(arr)