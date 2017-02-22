value = 0#stores multiple of 3 and 5

for num in range(1000):
    if (num % 3 == 0) or (num % 5 == 0):
        value = value + num
        
print(value)
