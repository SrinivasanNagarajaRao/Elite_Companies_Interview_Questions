class stack(object):
    def __init__(self):
        self.item = []

    def push(self, data):
        self.item.append(data)

    def pop(self):
        self.item.pop()

    def get_stack(self):
        return self.item

    def is_empty(self):
        return self.item == []

    def peek(self):
        if not self.is_empty():
            return self.item[-1]

def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False


def is_paren_balanced(paren_string):
    s = stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False


if __name__ == '__main__':
    # s = stack()
    # f = "srinivasan"
    print(is_paren_balanced("(((({}))))"))
    print(is_paren_balanced("[]"))
    # print([f[i:i+3] for i in range(0, len(f), 3)])
