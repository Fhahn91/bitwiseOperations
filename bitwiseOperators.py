# Program that performs bitwise operators.

# TODO OR operation

# TODO AND operation

# TODO SHIFT LEFT operation

# TODO SHIFT RIGHT operation

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

    binNum = int(input("Please enter the first binary number you would like to operator on: "))
    binNumTwo = int(input("Please enter the second binary number you would like to operator on: "))

    print(xorFunc( binNum, binNumTwo ))
       
    return


main()
    
        
