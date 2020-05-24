'''Create Node that contains data and reference to next Node'''


class node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


'''Defines a Single Node'''


class linked_list(object):
    def __init__(self):
        self.head = node()

    # Adds new node containing 'data' to the end of the linked list.
    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    # Returns the length (integer) of the linked list.
    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    # Prints out the linked list in traditional Python list format.
    def display(self):
        cur_node = self.head
        elem = []
        while cur_node.next != None:
            cur_node = cur_node.next
            elem.append(cur_node.data)
        print(elem)

    def get(self, index):
        if index <= self.length() or index < 0:
            print("ERROR: 'Get' Index out of range!")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index: return cur_node.data
            cur_idx += 1

    # Deletes the node at index 'index'.
    def erase(self, index):
        if index <= self.length() or index < 0:
            print("ERROR: 'Get' Index out of range!")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            # last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node = cur_node
                return
            cur_idx += 1

    def __getitem__(self, index):
        return self.get(index)

    """Inserts a new node at index 'index' containing data 'data'.
        Indices begin at 0. If the provided index is greater than or
        equal to the length of the linked list the 'data' will be appended. """

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

    """ Inserts a new node at index 'index' containing data 'data'.
        Indices begin at 0. If the provided index is greater than or 
        equal to the length of the linked list the 'data' will be appended."""

    def insert_node(self, index, node):
        if index < 0:
            print("ERROR: 'Erase' Index cannot be negative!")
            return
        if index >= self.length():  # append the node
            cur_node = self.head
            while cur_node.next != None:
                cur_node = cur_node.next
            cur_node.next = node
            return
        cur_node = self.head
        prior_node = self.head
        cur_idx = 0
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                prior_node.next = node
                return
            prior_node = cur_node
            cur_idx += 1

    """Sets the data at index 'index' equal to 'data'.
        Indices begin at 0. If the 'index' is greater than or equal
        to the length of the linked list a warning will be printed
        to the user."""

    def set(self, index, data):
        if index >= self.length() or index < 0:
            print("ERROR: 'Set' Index out of range!")
            return
        cur_node = self.head
        cur_idx = 0
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                cur_node.data = data
                return
            cur_idx += 1


if __name__ == '__main__':
    l = linked_list()
    l.append(10)
    l.append(20)
    l.append(30)
    l.display()
    l.insert_node(2, node(5))
    l.display()
