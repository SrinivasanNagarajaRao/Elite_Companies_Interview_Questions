class node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class CircularLinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head == None:
            print(data)
            self.head = node(data)
            self.head.next = self.head
        else:
            new_node = node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = node(data)
        cur = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node

    def display(self):
        cur = self.head
        elem = []
        while cur:
            elem.append(cur.data)
            cur = cur.next
            if cur == self.head:
                print(elem)
                break


if __name__ == '__main__':
    cll = CircularLinkedList()
    cll.append(10)
    cll.append(20)
    cll.append(30)
    cll.append(40)
    cll.append(50)
    cll.append(60)
    cll.display()
