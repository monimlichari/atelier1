Decimal = 987

def ConvertBinToDic(Decimal):
    Binary = []
    while Decimal >= 0:
        Binary.append(Decimal % 2)
        Decimal = Decimal // 2
        if Decimal == 0:
            break
    Binary.reverse()
    return Binary

print(ConvertBinToDic(Decimal))
'''
Decimal = int(input("Entrez le nombre décimal: "))
Binary = []


while Decimal >= 0:
    Binary.append(Decimal % 2)
    Decimal = Decimal // 2
    if Decimal == 0:
        break

Binary.reverse()
for i in Binary:
    print(i, end=" ")

'''

'''
decimal = int(input("Enter the decimal number:"))

def convertDecToBin(decimal):
    if decimal > 1:
        convertDecToBin(decimal//2)
    print(decimal%2, end="")

print(convertDecToBin(decimal))

'''


