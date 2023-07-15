def Tower_hanoi(n,a,b,c):
    if n==1:
        print('Move 1st disk from',a,'to',c)
        return
    Tower_hanoi(n-1,a,c,b)
    print('Move',n,'th disk from',a,'to',c)
    Tower_hanoi(n-1,b,a,c)
Tower_hanoi(3,'Source','Helper','Destination')