from unicodedata import name


n=int(input('Enter a number: '))
def isOdd(n):
    return n&1
if __name__=="__main__":
    if isOdd(n):
        print('O')
    else:
        print('E')