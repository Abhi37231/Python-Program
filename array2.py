import array as array

# Signed char
a = array.array('b', [1, -2, 3])
print("b:", a)

# Unsigned char       
a = array.array('B', [1, 2, 255])
print("B:", a)

# Unicode characters
a = array.array('u', 'hello')
print("u:", a)

# Signed short
a = array.array('h', [1000, -2000])
print("h:", a)

# Unsigned short
a = array.array('H', [1000, 65000])
print("H:", a)

# Signed int
a = array.array('i', [10, -20, 30])
print("i:", a)

# Unsigned int
a = array.array('I', [10, 20, 40000])
print("I:", a)

# Signed long
a = array.array('l', [100000, -200000])
print("l:", a)

# Unsigned long
a = array.array('L', [100000, 200000])
print("L:", a)

# Signed long long
a = array.array('q', [1000000000, -2000000000])
print("q:", a)

# Unsigned long long
a = array.array('Q', [1000000000, 2000000000])
print("Q:", a)

# Float
a = array.array('f', [1.5, 2.3, -3.9])
print("f:", a)

# Double
a = array.array('d', [1.23456789, -9.87654321])
print("d:", a)
