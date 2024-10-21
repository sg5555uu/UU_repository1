def get_multiplied_digits(number):
    str_number = str(number)
    str_no_zeroes = str_number.replace('0', '')
    first = int(str_no_zeroes[0])
    if len(str_no_zeroes) < 2:
        return first
    else:
        return first * get_multiplied_digits(int(str_no_zeroes[1:]))


result = get_multiplied_digits(402030)
print(result)
