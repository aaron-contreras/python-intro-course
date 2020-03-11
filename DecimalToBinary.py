def DecToBin(dec):
    result = "0";
    while (dec > 0):
        binNum = dec % 2
        result = result + str(binNum)
        dec = dec // 2
    return result

def BinToDec(bin):
    result = 0
    numberLen = len(str(bin))
    for i in range(0, numberLen, 1):
        
        decNum = bin % 10
        result = result + decNum * pow(2,i)
        bin = bin // 10

    return result


if __name__ == ("__main__"):
    dec = int(input("Ingrese un numero decimal: "))
    print(DecToBin(dec))
    bin = int(input("Ingrese un numero en binario: "))
    print(BinToDec(bin))
