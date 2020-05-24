'''Traversing is possible only forward in singly linked list'''


class node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class singly_linked_list(object):
    def __init__(self):
        self.head = None

    def append_at_end(self, data):
        cur = self.head
        new_node = node(data)
        if cur == None:
            self.head = new_node

        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def append_at_beginning(self, data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node
        

    def display(self):
        cur = self.head
        elem = []
        while cur != None:
            elem.append(cur.data)
            cur = cur.next
        print(elem)
        
    def length(self):
        cnt = 0
        cur = self.head
        while cur != None:
            cnt = cnt+1
            cur = cur.next
        return cnt
        
    def append_at_middle(self, index, data):
        if index >= self.length() or index < 0:
            return self.append_at_end(data)
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
    
    def delete_node(self, index):
        if index <= self.length() or index < 0:
            print("ERROR: 'Get' Index out of range!")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node = cur_node
                return
            cur_idx += 1
        


if __name__ == '__main__':
    ll = singly_linked_list()
    ''' create a new node from head '''
    ll.head = node("Mon")
    ''' creating single nodes without any connection '''
    e2 = node("Tue")
    e3 = node("Wed")

    ''' Linking each node and pointing it to other node'''
    ll.head.next = e2
    e2.next = e3
    ll.display()
    ll.append_at_end("Thurs")
    ll.append_at_end("Fri")
    ll.display()
    ll.append_at_beginning("Sun")
    ll.display()
    ll.append_at_middle(10,"Sat")
    ll.display()
    ll.delete_node(1)
    ll.display()
