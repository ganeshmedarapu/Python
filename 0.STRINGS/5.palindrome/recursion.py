def CheckPalindrome(s):
    if len(s)==0 or len(s)==1:
        return True
    if s[0]!=s[-1]:
        return False
    return CheckPalindrome(s[1:-1])
s=input('enter anything: ')
if CheckPalindrome(s):
    print('true')
else:
    print('false')
