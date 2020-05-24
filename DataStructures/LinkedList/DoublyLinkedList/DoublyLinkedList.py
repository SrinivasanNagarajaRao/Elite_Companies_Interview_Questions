class node(object):
    def __init__(self, data=None, next=None, prev_next=None):
        self.data = data
        self.next = next
        self.prev_next = prev_next


class doubly_linked_list(object):
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        current = new_node.next = self.head
        while current != None:
            self.head.prev_next = new_node
            current = current.next
        self.head = new_node

    def insert(self, prev_node, data):
        prev_node
        if prev_node is None:
            return
        new_node = node(data)
        new_node.next = prev_node.next

    def insert(self, index, data):
        if index >= self.length() or index < 0:
            return self.append(data)
        cur_node = self.head
        prior_node = self.head
        cur_idx = 0
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                new_node = node(data)
                prior_node.next = new_node
                new_node.next = cur_node
                return
            prior_node = cur_node
            cur_idx += 1


    def display(self):
        current_node = self.head
        elem = []
        while current_node.next != None:
            elem.append(current_node.data)
            current_node = current_node.next
        print(elem)

if __name__ == '__main__':
    dll = doubly_linked_list()
    dll.append("hi")
    dll.append("bye")
    dll.append("bye1")
    dll.append("bye2")
    dll.display()
