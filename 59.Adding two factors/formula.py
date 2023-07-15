from fractions import Fraction
x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
result=Fraction(x1,y1)+Fraction(x2,y2)
print(result)