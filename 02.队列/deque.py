"""
双端队列：
    跟队列相似，其两端可以称作 首、尾两端，既可以从队首加入，也可以从队尾加入；数据集也可以从两端移除
    某种意义上：双端队列集成了栈和队列的能力
    它不具备先进先出（队列）和先进后出（栈）的内在特性
    使用的时候，需要自行遵守
"""
class Deque(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def addFront(self,value): # 从右端添加数据
        self.items.append(value)

    def addRear(self,value): # 从左端添加数据
        self.items.insert(0,value)

    def removeFront(self): # 从右端移除数据
        return self.items.pop()

    def removeRear(self): # 从左端移除数据
        return self.items.pop(0)

    def size(self):
        return len(self.items)

