"""
冒泡排序：
    时间复杂度：O(n^2)
"""

def bubblesort(arr_num,n):
    for i in range(n-1):
        for j in range(n-i-1):
            if arr_num[j] > arr_num[j+1]:
                arr_num[j],arr_num[j+1] = arr_num[j+1],arr_num[j]
    return arr_num

if __name__ == "__main__":
    arr = [1,2,3,5,3,65,76,32,34,54,13]
    arr = bubblesort(arr,len(arr))
    print(arr)