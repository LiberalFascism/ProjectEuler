num = 2
counter = 0

while True:
    for i in range(2,num):
        if num % i ==0:
            break

    else:
        
        counter+=1

    if counter == 10001:
        break
    num+=1

print('The prime number on 6th position is',num)
