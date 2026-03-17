#Name: Section7.26Problem9
#Purpose: Iteration
#Author: KamdynHagerty
#Created: 3/16/26


def print_triangular_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
        print(i, total)
print_triangular_numbers(5)
