n = 1
s = 0
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
 
while True:
    f = fib(n)
    n+= 1
    if f>= 4000000:
        break
    elif  not f%2 == 0:
        s+=f
print(s)
