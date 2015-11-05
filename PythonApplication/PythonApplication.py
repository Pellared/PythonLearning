import re

file = open('regex_sum_172402.txt')
numbers = []
for line in file:
    numbers += re.findall('[0-9]+', line)
print sum([int(x) for x in numbers])