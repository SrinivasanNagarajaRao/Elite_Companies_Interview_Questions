# 3) Write a program to print the possible combinations of any given word
# INPUT = "CAT"
# Expected Result: "CAT","CTA","ACT","ATC","TCA","TAC"

from itertools import permutations

def all_permutation(f_input):
    perm_list = permutations(f_input)
    print(list(perm_list))
    for perm in list(perm_list):
        print("".join(perm))
              
# f_input = "CAT"
f_input = 105
all_permutation(f_input)