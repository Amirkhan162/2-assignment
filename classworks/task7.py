n = int(input())

d1 = n // 1000
d2 = (n // 100) % 10
d3 = (n // 10) % 10
d4 = n % 10

sum_powers = d1**4 + d2**4 + d3**4 + d4**4

if sum_powers == n:
    print("Armstrong number")
else:
    print("Not Armstrong number")