"""
堆排序： 不稳定排序
    时间复杂度：O(nlogn)
    堆是一个完全二叉树
"""
def heapify(tree,n,i):
    # 对 i 结点进行 重构堆
    c1 = 2*i + 1 # 子节点1
    c2 = 2*i + 2 # 子节点2
    max_index = i # 假设根节点 的值 最大
    while c1 < n and tree[max_index] < tree[c1]:
        max_index = c1
    while c2 < n and tree[max_index] < tree[c2]:
        max_index = c2

    if i != max_index:
        arr[i],arr[max_index] = arr[max_index],arr[i]
        heapify(tree,n,max_index) # 继续递归

def build_heap(tree,n):
    # 重构树，从最后一个父节点开始
    last_node = n - 1
    parent = int((last_node - 1) / 2)
    for i in range(parent,-1,-1):
        heapify(tree,n,i)

def heap_sort(tree,n):
    build_heap(tree,n)
    for i in range(n-1,-1,-1):
        # 将 最后一个结点 与 第一个结点的值 交换，然后 对第一个节点，重构堆
        tree[i],tree[0] = tree[0],tree[i]
        heapify(tree,i,0)

if __name__ == "__main__":
    arr = [1, 2, 3, 5, 6, 65, 76, 32, 34, 54, 13]
    heap_sort(arr,len(arr))
    print(arr)