string: str = 'pasta'
rev = ''
for j in range (len(string)-1, -1, -1):
    rev+= string[j]
print(rev)
