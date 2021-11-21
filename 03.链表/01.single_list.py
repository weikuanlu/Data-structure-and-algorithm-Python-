# -*- coding = utf-8 -*-

class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None

class SingleList(object):
    def __init__(self, node = None):
        self.__head = node

    def is_empty(self):
        return self.__head == None

    def length(self):
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        items = []
        while cur != None:
            items.append(str(cur.item))
            cur = cur.next
        print(','.join(items))

    def add(self,item):
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self,item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        if (pos <= 0):
            self.add(item)
        elif (pos > (self.length() - 1)):
            self.append(item)
        else:
            node = Node(item)
            count = 0
            pre = self.__head
            while count < (pos - 1):
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        cur = self.__head
        pre = None
        while cur != None:
            if cur.item == item:
                if not pre:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        cur = self.__head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

if __name__ == "__main__":
    ll = SingleList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    print("length:",ll.length())
    ll.travel()
    print(ll.search(3))
    print(ll.search(5))
    ll.remove(1)
    print("length:",ll.length())
    ll.travel()
