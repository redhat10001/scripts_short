print('*' * 25)
s = ['Hristophor', 'Ademar', 'Tey', 'Andrey', 'Aleksandr']

value = filter(lambda name: name.startswith('A'), s)
print(*value)
