value = 0
n = 2
value = int(input('Enter a value::'))

while True:
    
    if value % n == 0:
        value = value // n
        print(n)
    else:
        n+=1
    if value > 1:
        continue
    else:
        break
