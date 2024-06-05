from datetime import datetime

abundant_dict = {}


def get_devisors(n):
    return [i for i in range(1, n) if n % i == 0]


def calculate_abundant(num):
    divisors = get_devisors(num)
    if sum(divisors) > num:
        return True
    return False


def is_abundant(num):
    if num in abundant_dict:
        return abundant_dict[num]

    res = calculate_abundant(num)
    abundant_dict[num] = res
    return res


def is_sum_of_abundants(num):
    for i in range(1, int((num / 2) + 1)):
        if is_abundant(i) and is_abundant(num - i):
            return True
    return False


start_time = datetime.now()
sum_of_non_sum_of_abundants = 0
for num in range(0, 28123):
    sum_of_abundant = is_sum_of_abundants(num)
    if not sum_of_abundant:
        sum_of_non_sum_of_abundants += num
    # print(f"{num} is_sum_of_abundant: {sum_of_abundant}")
print(sum_of_non_sum_of_abundants)


print(datetime.now() - start_time)
