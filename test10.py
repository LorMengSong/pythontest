
#PrintHex()
print("================PrintHEX=====================")
number = 435
print(number, 'in hex =', hex(number))

number = 0
print(number, 'in hex =', hex(number))

number = -34
print(number, 'in hex =', hex(number))

returnType = type(hex(number))
print('Return type from hex() is', returnType)

#PrintBIN()
print("================PrintBIN=====================")
x = 10
print("Original number: ",x)
y = bin(x)
print("Binary string:")
print (y)
x = -10
print("\nOriginal number: ",x)
y = bin(x)
print("Binary string:")
print (y)

#PrintDec()
print("================PrintDec=====================")

a = 8
print("The number is", a)
# OR
b = 8
print("The number is " + str(b))

# Float
f = 14.08
print("The number is " + str(f))