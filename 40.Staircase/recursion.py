'''A child is running up a staircase with N steps, and can hop either 1 step, 2 steps or 3 steps at a time. 
Implement a method to count how many possible ways the child can run up to the stairs. You need to return number of possible ways'''

def Staircase(n):
    if n==1 or n==2:
        return n
    if n<=0:
        return 0
    x=Staircase(n-1)
    y=Staircase(n-2)
    z=Staircase(n-3)   
    return x+y+z
print(Staircase(1))
print(Staircase(2))
print(Staircase(3))
print(Staircase(4))
print(Staircase(5))
