from math import *
def fibonacciSeries(exp,n):
    for i in range(0,n):
        result=round(pow(exp,i)/sqrt(5))
        print(result,end=" ")
num=5
exp=(1+sqrt(5))/2
fibonacciSeries(exp,num)
