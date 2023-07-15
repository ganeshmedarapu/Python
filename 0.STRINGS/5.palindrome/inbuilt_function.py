s=input('Enter a word: ')
def isPalindrome(s):
    rev=''.join(reversed(s))
    if s==rev:
        return True
    return False
print('P' if isPalindrome(s) else 'N')
