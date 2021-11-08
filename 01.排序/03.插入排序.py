"""
插入排序： 稳定排序
    时间复杂度：O(n^2)
"""
def insert_sort(arr):
    n = len(arr) # 数组长度
    for i in range(1,n): # 随机选择一个元素 开始往前插入，这里从下标1开始
        key = arr[i] # 定义插入的元素值
        j = i - 1 # 插入元素下标的 前一个下标
        while j >= 0 and arr[j] > key: # 必须j>=0 同时，前面的值大于要插入的值
            arr[j+1] = arr[j] # 将前面的值 后移一位
            j -= 1 # 继续往前一位
        arr[j+1] = key # 在不满足条件后，将值 插入到 不满足条件的值 的 后一位

if __name__ == "__main__":
    arr = [1, 2, 3, 5, 6, 65, 76, 32, 34, 54, 13]
    insert_sort(arr)
    print(arr)