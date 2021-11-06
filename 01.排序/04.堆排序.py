"""
堆排序：
    时间复杂度：O(nlogn)
"""
def heapify(tree,n,i):
    c1 = 2*i + 1
    c2 = 2*i + 2
    max_index = i
    if (c1 < n and tree[max_index] < tree[c1]):
        max_index = c1
    if (c2 < n and tree[max_index] < tree[c2]):
        max_index = c2
    if (i != max_index):
        tree[max_index],tree[i] = tree[i],tree[max_index]
        heapify(tree,n,max_index)

def build_heap(tree,n): # 重构树
    last_node = n-1
    parent = int((last_node - 1) / 2)
    for i in range(parent,-1,-1):
        heapify(tree,n,i)
    return tree

def heap_sort(tree,n):
    build_heap(tree,n)
    for i in range(n-1,-1,-1):
        tree[i],tree[0] = tree[0],tree[i]
        heapify(tree,i,0)
    return tree

if __name__ == "__main__":
    tree = [1,2,3,5,65,76,32,34,54,13]
    tree = heap_sort(tree,len(tree))
    print(tree)