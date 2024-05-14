def get_devisors(n):
    return [i for i in range(1, n) if n % i == 0]


def get_sum_of_devisors(n):
    return sum(get_devisors(n))


sum_of_amacable = 0

for num in range(0, 10000):
    sum_of_num_devisors = get_sum_of_devisors(num)
    if (
        sum_of_num_devisors < 10000
        and num != sum_of_num_devisors
        and get_sum_of_devisors(sum_of_num_devisors) == num
    ):
        print(f"{num} and {sum_of_num_devisors} are amicable numbers")
        sum_of_amacable += num
print(sum_of_amacable)
