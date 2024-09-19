numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
i = 0
j = 0
for i in range(len(numbers)):
    if i == 0:
        continue
    else:
        a = False
        for j in range(len(numbers)):
            if j == 0 or j >= i:
                continue
            else:
                if numbers[i] % numbers [j] == 0:
                    a = True
        if a == False:
            primes.append(numbers[i])
        else:
            not_primes.append(numbers[i])
print("Primes: ", primes)
print("Not Primes: ", not_primes)