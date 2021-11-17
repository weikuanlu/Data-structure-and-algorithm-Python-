"""
队列：
    新加入的数据项必须在数据集末尾等待，而等待时间最长的数据项则是队首
    性质：先进先出，队列仅有一个入口和出口，不允许数据直接插入队列中，也不允许从中间移出数据项
    举例：操作系统核心采用多个队列来对系统中同时进行的进程进行调度
"""
class Queue(object):
    """ 选用列表右端，作为队列入口；列表左端，作为队列出口 """
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self,value):
        self.items.append(value)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


