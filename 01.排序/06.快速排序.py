"""
快速排序： 不稳定排序
    时间复杂度：O(nlogn)
"""
def partition(arr,low,high):
    # 在序列中，找一个基础值，小于基准值的放在左边，大于基准值的放在右边
    # 返回基准值 下标
    i = low - 1
    pivot = arr[high]
    for j in range(low,high):
        if arr[j] < pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

def quick_sort(arr,low,high):
    # 分而治之的思想
    if low < high:
        mid = partition(arr,low,high)
        quick_sort(arr,low,mid-1)
        quick_sort(arr,mid+1,high)

if __name__ == "__main__":
    arr = [1, 2, 3, 5, 6, 65, 76, 32, 34, 54, 13]
    quick_sort(arr,0,len(arr)-1)
    print(arr)