first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))
print(list(first_result))

second_result = (len(first[el]) == len(second[el]) for el in range(0, len(first)))
print(list(second_result))

# sec_result = (len(x) == len(y) for x, y in zip(first, second))
# print(list(sec_result))
# решение с zip