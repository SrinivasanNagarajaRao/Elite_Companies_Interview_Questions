""" Question 1: 1)	Write a program which will find numbers which are divisible by 7 but not a multiple of 5
    between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence
     on a single line."""

a = []
for i in range(2000,3200):
    if(i % 7 ==0) and (i % 5 != 0):
        a.append(str(i))
print(','.join(a))

"""Question 2: 2)	Write a program to find largest sequence in a given list of numbers
                    INPUT = [1,2,3,2,4,5,6,7,8,1,0,4,5,6]
                    Expected Result: [4, 5, 6, 7, 8] """


from itertools import groupby
from operator import itemgetter

data = [1,2,3,2,4,5,6,7,8,1,0,4,5,6]
new_list = []

for a, b in groupby(enumerate(data), lambda x: x[0] - x[1]):
    new_list.append(list(map(itemgetter(1), b)))

print(max(new_list, key=lambda x: len(x)))

"""3)	Write a program to print the possible combinations of any given word
        INPUT = "CAT"
        Expected Result:  "CAT","CTA","ACT","ATC","TCA","TAC"
        """

from itertools import permutations


def all_permutation(f_input):
    perm_list = permutations(f_input)
    for perm in list(perm_list):
        print(''.join(perm))


f_input = 'CAT'
all_permutation(f_input)

