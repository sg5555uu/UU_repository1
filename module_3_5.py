def get_multiplied_digits(number):
    str_number = str(number)
    str_no_zeroes = str_number.replace('0', '')
    if str_no_zeroes == '':
        return 0
    else:
        first = int(str_no_zeroes[0])
        if len(str_no_zeroes) < 2:
            return first
        else:
            return first * get_multiplied_digits(int(str_no_zeroes[1:]))


result = get_multiplied_digits(40203)
result1 = get_multiplied_digits(420)
result2 = get_multiplied_digits(0)
print(result)
print(result1)
print(result2)
