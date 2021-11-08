"""
冒泡排序： 稳定排序
    时间复杂度：O(n^2)
"""
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

if __name__ == "__main__":
    arr = [1, 2, 3, 5, 6, 65, 76, 32, 34, 54, 13]
    bubble_sort(arr)
    print(arr)