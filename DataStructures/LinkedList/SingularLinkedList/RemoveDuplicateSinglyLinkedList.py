class node(object):
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = next


class linked_list(object):
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def display(self):
        cur = self.head
        elem = []
        while cur.next != None:
            cur = cur.next
            elem.append(cur.data)
        print(elem)

    def remove_duplicate(self):
        current = self.head
        previous = None
        elem = []
        while current != None:
            if current.data not in elem:
                elem.append(current.data)
                previous = current
                current = current.next
            else:
                current = previous.next = current.next

from collections import deque

if __name__ == '__main__':
    sll = linked_list()
    sll.append(10)
    sll.append(20)
    sll.append(30)
    sll.append(30)
    sll.append(40)
    sll.append(40)
    sll.append(50)
    sll.display()

    sll.remove_duplicate()
    sll.display()
