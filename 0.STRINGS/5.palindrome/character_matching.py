s=input('Enter a word: ')
def isPalindrome(s):
    for i in range(len(s)):
        if s[i]!=s[len(s)-i-1]:
            return False
    return True
#isPalindrome(s)
print('P' if isPalindrome(s) else 'N')

