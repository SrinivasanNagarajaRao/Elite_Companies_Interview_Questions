"""Question 2: 2)	Write a program to find largest sequence in a given list of numbers
                    INPUT = [1,2,3,2,4,5,6,7,8,1,0,4,5,6]
                    Expected Result: [4, 5, 6, 7, 8] """


from itertools import groupby
from operator import itemgetter

data = [1,2,3,2,4,5,6,7,8,1,0,4,5,6]
new_list = []

for a, b in groupby(enumerate(data), lambda x: x[0] - x[1]):
    print(a, b)
    new_list.append(list(map(itemgetter(1), b)))

print(max(new_list, key=lambda x: len(x)))

