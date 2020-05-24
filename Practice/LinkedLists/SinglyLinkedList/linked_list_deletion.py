class node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class singly_linked_list(object):
    def __init__(self):
        self.head = None

    def display(self):
        cur = self.head
        elem = []
        while cur != None:
            elem.append(cur.data)
            cur = cur.next
        print(elem)

    def append_at_end(self, data):
        new_node = node(data)
        cur = self.head
        if cur == None:
            self.head = new_node
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def append_at_beginning(self, data):
        new_node = node(data)
        cur = self.head
        if cur == None:
            self.head = new_node
        new_node.next = self.head
        self.head = new_node

    def length(self):
        cur = self.head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def delete_by_pos(self, pos):
        cur_node = self.head
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return

        prev_node = None
        count = 0
        while cur_node and count != pos:
            prev_node = cur_node
            print(prev_node.data)
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            return

        prev_node.next = cur_node.next
        cur_node = None

    def delete_by_node(self, data):
        cur_node = self.head

        if cur_node and cur_node.data == data:
            self.head = cur_node.next
            cur_node = None
            return

        prev_node = None
        count = 0
        while cur_node and cur_node.data != data:
            prev_node = cur_node
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            return
        prev_node.next = cur_node.next
        cur_node = None
        if count != length()
        return "1 Node Deleted"


if __name__ == '__main__':
    ll = singly_linked_list()
    ll.head = node("Monday")
    e2 = node("Tuesday")
    e3 = node("Wednesday")
    ll.head.next = e2
    e2.next = e3
    ll.display()
    ll.append_at_end("Thursday")
    ll.append_at_end("Friday")
    ll.append_at_beginning("Sunday")
    ll.display()
    ll.delete_by_pos(2)
    ll.display()
    ll.delete_by_node("Sunday")
    ll.delete_by_node("Monday")
    ll.display()
