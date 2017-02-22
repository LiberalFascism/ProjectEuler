n = 1
x = 2

while x <= 20:
    if n%x !=0:
        n+=1
        x=2
    else:
        x+=1
print(n)