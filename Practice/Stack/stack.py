class stack(object):
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        self.items.pop()

    def get_stack(self):
        return self.items

    def is_empty(self):
        self.items == []
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]


if __name__ == '__main__':
    s = stack()
    s.push("A")
    s.push("B")
    s.push("C")
    s.push("D")
    s.push("E")
    print(s.get_stack())
    s.pop()
    print(s.get_stack())
    print(s.peek())
