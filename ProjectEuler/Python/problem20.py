from math import factorial

fact_100 = str(factorial(100))
sum = 0
for i in range(len(fact_100)):
    sum += int(fact_100[i])
print(sum)
