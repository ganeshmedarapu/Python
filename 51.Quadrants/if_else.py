x=int(input('Enter x coordinate:'))
y=int(input('Enter y coordinate:'))
def Quadrant(x,y):
    if x>0 and y>0:
        print('This point lies in first quadrant.')
    elif x>0 and y<0:
        print('This point lies in fourth quadrant.')
    elif x<0 and y>0:
        print('This point lies in second quadrant.')
    else:
        print('This point lies in third quadrant.')
Quadrant(x,y)
