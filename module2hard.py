number = int(input("Введите число из первой вставки (от 3 до 20): "))
if number > 20:
    print("Введенное число больше 20")
elif number < 3:
    print("Введенное число меньше 3")
else:
    pairs = []
    i = 1
    j = 2
    while i < number / 2:
        while j < number:
            if number % (i + j) == 0:
                pairs.append(i)
                pairs.append(j)
                j += 1
                continue
            else:
                j += 1
        i += 1
        j = i
    password = ''.join(map(str, pairs))
    print("Пароль: ", password)