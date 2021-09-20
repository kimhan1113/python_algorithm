
strings = input()

sum = 0

only_str = []

for string in strings:
    if string.isdigit():
        sum += int(string)
    else:
        only_str.append(string)

only_str.sort()

print(''.join(only_str) + str(sum))
