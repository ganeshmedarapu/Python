# ASCII value of 0 is 48 and 1 is 49
def String_Integer(s):
    if len(s)==1:
        return ord(s[0])-ord('0')
    recursive_output=String_Integer(s[0:len(s)-1])
    last_digit=ord(s[-1])-ord('0')
    return recursive_output*10+last_digit
print(String_Integer('123456'))