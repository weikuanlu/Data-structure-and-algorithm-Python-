"""
栈：
    一种有次序的数据项集合，在栈中，数据项的加入和移除都仅发生在同一端（栈顶），另一端叫（栈底）
    性质：先进后出（后进先出） -- 类似浏览器后退按钮，word的撤回操作
"""
class Stack(object):
    """ 选择列表右端作为：栈顶，左端作为栈顶底 """
    def __init__(self):
        # 定义一个空栈
        self.items = []

    def is_empty(self):
        # 判断栈是否为空，返回bool值
        return self.items == []

    def push(self,value):
        # 从栈顶 也就是 列表的右端 添加数据
        self.items.append(value)

    def remove(self):
        # 移除数据，从栈顶 还是 列表的右端 移除数据
        return self.items.pop()

    def peek(self):
        # 查看 栈顶的数据
        return self.items[len(self.items)-1]

    def size(self):
        # 返回栈里面数据的长度
        return len(self.items)

