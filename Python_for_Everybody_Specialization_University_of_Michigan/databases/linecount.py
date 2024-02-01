file = input('Enter a file - ')
file = open(file)
count = 0
dict = {}
for line in file:
    if not line.startswith('From: '): continue
    pieces = line.split()
    if len(pieces) < 3:
      email = pieces[1]
      email = email.split('@')
      org = email[1]
      if org not in dict:
        dict[org] =1
      else:
        dict[org] +=1
print(dict)

for line in file:
  count += 1
print(count)
file.close()
