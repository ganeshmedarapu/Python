n=int(input('Enter a number: '))
def print_1_to_n(n):
    if n==0:
        return 
    print_1_to_n(n-1) 
    print(n)
    
print_1_to_n(n)

print('***********************')

def print_n_to_1(n):
    if n==0:
        return 
    print(n)
    print_n_to_1(n-1) 
    
    
print_n_to_1(n)