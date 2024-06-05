with open("ProjectEuler/Python/names.txt") as f:
    raw_text = f.readline()
names = [n.replace('"', "") for n in raw_text.split(",")]
names.sort()


print(ord("A"))
total = 0
for x in range(0, len(names)):
    name = names[x]
    sum_of_numbers = 0
    for chr in name:
        sum_of_numbers += ord(chr) - 64
    total_count = (x + 1) * sum_of_numbers
    # if name == "COLIN":
    #     print(total_count)
    total += total_count
print(total)
