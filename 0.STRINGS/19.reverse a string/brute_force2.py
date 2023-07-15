s='Hello'
output=''
for i in range(len(s)-1,0,-1):
    output+=s[i]
output+=s[i-1]
print(output)
