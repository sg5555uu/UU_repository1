calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    info = len(string), string.upper(), string.lower()
    count_calls()
    return info


def is_contains(string, list_to_search):
    n = 0
    contain = False
    while n < len(list_to_search):
        if list_to_search[n].lower() != string.lower():
            n += 1
            continue
        else:
            contain = True
            break
    count_calls()
    return contain


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
