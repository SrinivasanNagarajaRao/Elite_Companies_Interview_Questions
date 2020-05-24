# class walmart(object):
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next
#
#
# class list_stack(object):
#     def stack(self):
#         self.head = None
#
#     def append(self, data):
#         while head != None:
#             head = walmart(data)
#
#
# list = []
# stack = []
#
#
# def lifo(data):
#     list.append(data)
#     return list


l = [2, 4, 4, 5]
s = [1, 3, 5, 7]
k = 8

result = []
r = []
def sortsample(array_sample):
    d = []
    for i in range(0, len(array_sample)) :
        t = []
        d = array_sample[i] + array_sample[i + 1]
        t.append(array_sample[i])
        t.append(array_sample[i + 1])
        if d == k:
           result.append("True Set")
           print(array_sample[i], array_sample[i + 1])
           return result

def binary(array_sample):
    lenght = len(array_sample) % 2
    print(lenght)
    for i in range(0, len(array_sample)) :
        t = []
        d = array_sample[i] + array_sample[i + 1]
        t.append(array_sample[i])
        t.append(array_sample[i + 1])
        if d == k:
            result.append("True Set")
            print(array_sample[i], array_sample[i + 1])
            return result

print("Successful Combination " + str(len(sortsample(s))))
print("Successful Combination " + str(len(sortsample(l))))

gh = "madam"

def palindrome(input):
    if (gh == gh[::-1]):
        return "Is Palindrome"
    else:
        return "Not Palindrome"

print(palindrome(gh))

# if __name__ == '__main__':
#     lifo(10)
#     lifo(20)
#     lifo(30)
#     # print(lifo(40))
