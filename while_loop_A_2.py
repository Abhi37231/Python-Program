no = int(input("Enter the number: "))

i = 1
sum = 0

while i<= no:
    if i % 2 == 0:
        sum += i
    i+=1
print ("Sum of even No are : ",sum)
        