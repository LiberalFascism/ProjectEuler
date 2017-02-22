
def pal(n):
    
    pallin = 0
    value= n
    while n > 0:
        s = n % 10
        n = n // 10

        pallin = int(str(pallin) + str(s))

    if pallin == value:
        print('The given number ' +str(pallin) + ' is  pallindrome:')
    


for i in range(100 , 999):
    for j in range(100, 999):
        
        n = i*j
        n = pal(n)
