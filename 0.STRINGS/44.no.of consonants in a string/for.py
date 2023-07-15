S=input('Enter a string: ')
S=S.lower()
count=0
for i in S:
    if i!='a' and i!='e' and i!='i' and i!='o' and i!='u':
        count+=1
print(count)