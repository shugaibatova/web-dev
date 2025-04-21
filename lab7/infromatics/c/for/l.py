num = input()
bin_number = 0
power = 1

for i in range(len(num) - 1, -1, -1):
    bin_number += int(num[i]) * power
    power *= 2

print(bin_number)
