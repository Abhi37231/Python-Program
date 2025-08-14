import array as arr  

a = arr.array('i', [1, 2, 3])

print("The new created array is:", end=" ")

for i in range(0, 3):
    print(a[i], end=" ")  


a.append(5)
print(a)

a.count(1)
print(a.count(1))

print(a.extend())

print(a.clear())


