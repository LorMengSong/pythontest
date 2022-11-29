def printDec(number):
    print("Decimal : ",int(number))
def printBin(number):
    print("Binary: ",bin(number))
def printHexa(number):
    print("Hexa: ",hex(number))
def option():
    print("[1]. decimal")
    print("[2]. binary")
    print("[3]. Hexa")
print("use function convert decimal to bin,dec,hex")
number = int(input("Input Number: "))
option()
opt=int(input("Choose 1,2,3: "))
if(opt==1):
    printDec(number)
elif(opt==2):
    printBin(number)
else : 
    printHexa(number)    
