class node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class singly_linked_list(object):
    def __init__(self, head=None):
        self.head = head

    def append_at_end(self, data):
        new_node = node(data)
        cur_node = self.head
        if cur_node == None:
            self.head = new_node
            print(self.head.data)
        while cur_node != None:
            self.head.next = new_node
            cur_node = cur_node.next
            
    def display(self):
        cur_node = self.head
        elem = []
        while cur_node != None:
            elem.append(cur_node.data)
            cur_node = cur_node.next
        print(elem)
        
    def is_palindrome(self):
        '''Method 1: '''
        s = ""
        cur_node = self.head
        while cur_node:
            s +=cur_node.data
            cur_node = cur_node.next
        return s == s[::-1] 
            
            
ll = singly_linked_list()
ll.append_at_end("H")
ll.append_at_end("H")
ll.append_at_end("H")
ll.display()
lb = singly_linked_list()
lb.append_at_end("A")
lb.append_at_end("B")
lb.append_at_end("C")
lb.append_at_end("D")
lb.display
print(ll.is_palindrome())
print(lb.is_palindrome())
            