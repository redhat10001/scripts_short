print('*' * 25)


from collections import defaultdict

counts = defaultdict(int)
fruits = ['apple', 'orange', 'apple', 'banana', 'apple']

for item in fruits:
    counts[item] += 1

print(counts)
# Output: defaultdict(<class 'int'>, {'apple': 3, 'orange': 1, 'banana': 1})

