import re

file = input('Enter filename to process:')
file = open(file)
sum = 0
for line in file:
  num = re.findall('[0-9]+', line)
  for each in num:
    x = int(each)
    sum = x + sum
print(sum)
