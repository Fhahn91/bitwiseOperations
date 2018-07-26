# Program that performs bitwise operations.

def orFunc( num, numTwo ):

    orNum = list(map(int, str(num)))
    orNumTwo = list(map(int, str(numTwo)))
    orComplete = [0] * len(orNum)

    for i in range(len(orNum)):
        if (orNum[i] == 1) or (orNumTwo[i] == 1):
            orComplete[i] = 1
        elif (orNum[i] == 0) and (orNumTwo[i] == 0):
            orComplete[i] = 0            
    return ''.join(map(str, orComplete))


def andFunc( num, numTwo ):

    andNum = list(map(int, str(num)))
    andNumTwo = list(map(int, str(numTwo)))
    andComplete = [0] * len(andNum)

    for i in range(len(andNum)):
        if andNum[i] == 1 and andNumTwo[i] == 1:
            andComplete[i] = 1
        else:
            andComplete[i] = 0
    return ''.join(map(str, andComplete))


def shiftLeft( num, shift ):

    numList = list(map(int, str(num)))
    shiftNum = [0] * shift
    numList.extend(shiftNum)
    return int(''.join(map(str, numList)))
    

def shiftRight( num, shift ):

    numList = list(map(int, str(num)))
    shiftList = numList[:len(numList) - shift]
    return ''.join(map(str, shiftList))

def xorFunc( num, numTwo ):

    xorNum = list(map(int, str(num)))
    xorNumTwo = list(map(int, str(numTwo)))
    xorComplete = [0] * len(xorNum)
    
    
    for i in range(len(xorNum)):
        if (xorNum[i] == 1) and (xorNumTwo[i] == 1):
            xorComplete[i] = 0
        elif (xorNum[i] == 1) and (xorNumTwo[i] == 0):
            xorComplete[i] = 1
        elif (xorNum[i] == 0) and (xorNumTwo[i] == 1):
            xorComplete[i] = 1
        elif (xorNum[i] == 0) and (xorNumTwo[i] == 0):
            xorComplete[i] = 0 
    return ''.join(map(str, xorComplete))

def main():

    # TODO make program more interactive.
    # TODO add hexidecimal and true/false support
    print("-----------Bitwise Operators-----------")
    print("[X]OR")
    print("[O]R")
    print("[A]ND")
    print("Shift [L]eft")
    print("Shift [R]ight")
    print("EXIT - To Quit")
    choice = input("\nPlease enter your decision: ")


    if choice == "X":
        binNum = int(input("\nPlease enter the first binary number you would like to XOR: "))
        binNumTwo = int(input("Please enter the second binary number you would like to XOR: "))
        print(xorFunc( binNum, binNumTwo ))
    elif choice == "O":
        binNum = int(input("\nPlease enter the first binary number you would like to OR: "))
        binNumTwo = int(input("Please enter the second binary number you would like to OR: "))
        print(orFunc(binNum, binNumTwo))
    elif choice == "A":
        binNum = int(input("\nPlease enter the first binary number you would like to AND: "))
        binNumTwo = int(input("Please enter the second binary number you would like to AND: "))
        print(andFunc(binNum, binNumTwo))
    elif choice == "L":
        binNum = int(input("\nPlease enter the binary number you would like to shift left: "))
        shifty = int(input("Please enter the amount you would like to shift: "))
        print(shiftLeft(binNum, shifty))
    elif choice == "R":
        binNum = int(input("\nPlease enter the binary number you would like to shift right: "))
        shifty = int(input("Please enter the amount you would like to shift: "))
        print(shiftRight(binNum, shifty))
    elif choice == "EXIT":
        return print("Cya later, aligator.")
       
    return print("Cya later, aligator")


main()
    
        
