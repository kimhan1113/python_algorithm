from collections import Counter

lists = ['red', 'blue', 'red', 'green', 'purple', 'yellow', 'blue', 'orange', 'gray', 'brown', 'gray']

counter = Counter(lists)

print(dict(counter))