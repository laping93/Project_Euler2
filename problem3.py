# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

s = 0
max_factor = 1
i = 600851475142//2

while True:
    print(i)
    if (i % 2 != 0) and (i % 3 != 0) and (i % 5 != 0) and (i % 7 != 0):
        if 600851475143 % i == 0:
            max_factor = i
            break
    i -= 1

print('Максимальный делитель =', max_factor)

# цикл равзернуть в другую сторону
