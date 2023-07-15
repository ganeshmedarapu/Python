from math import pow,sqrt
a,b,c = list(map(int,input('Enter the values of a,b and c:').split()))
root1 = (-b+sqrt(pow(b,2)-4*a*c))/2*a
root2 = (-b-sqrt(pow(b,2)-4*a*c))/2*a
if pow(b,2)-4*a*c ==0:
    print('Roots are equal')
    print('root1 == root2 ==',root1)
elif pow(b,2)-4*a*c >0:
    print('Roots are real and distinct and rational')
else:
    print('Roots are imaginary')
