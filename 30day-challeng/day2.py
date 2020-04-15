#/bin/python3
def isHappy(n):
    print(n)
    while( n >= 10 ):
        lists = list(map(int,' '.join(str(n)).split()))
        #print(sqar(lists))
        n = sqar(lists)

    if n == 1 or n == 7:
        print(str(n)+ ' is happy')
        return True;
    else: 
        print(str(n)+ ' is not happy')
        return False;     


def sqar(lists):
    sum = 0
    for i in lists:
        sum += i*i
    return sum


isHappy(2)
isHappy(7)
isHappy(19)