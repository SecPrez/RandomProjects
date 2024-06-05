# A permutation is an ordered arrangement of objects.
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

from itertools import permutations


def interpolate(n, step_size, domain):
    # n is the number to interpolate with in the domain
    # if the number is 4 domain is [0,1,2] and step size is 2 then the result should be 1
    if len(domain) == 1:
        return domain[0]
    steps_in = (n / step_size) - 1
    return domain[int(steps_in)]


def calculate_digit(number, domain):
    size_of_domain = len(domain)
    total_permutations = factorial(size_of_domain)
    step_size = total_permutations / size_of_domain
    return interpolate(number, step_size, domain)


from math import factorial

final_num = ""
# final_num += str(interpolate(4, 2, [0, 1, 2]))
# final_num += str(interpolate(2, 1, [0, 2]))
# domain = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# index_wanted = 1000000


domain = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
index_wanted = 1000000
while len(domain) > 0:

    size_of_domain = len(domain)
    total_permutations = factorial(size_of_domain)
    step_size = total_permutations / size_of_domain
    steps_in = int((index_wanted / step_size) - 1)
    item = domain[steps_in]
    index_wanted = index_wanted % step_size
    final_num += str(item)
    domain.remove(item)
print(final_num)


# print([x for x in permutations([0, 1, 2, 3, 4], 5)])
for idx, perm in enumerate(permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10)):
    if idx == 100000:
        print(perm)
        break
