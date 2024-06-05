def factorialLoop(num:int):
    factNum = 1

    
    for i in range(1,num+1):
        factNum *= i

    return factNum


def factorialRecursion(num:int):
    
    #basecase
    if num <= 1:
        return 1
    else:
        return num * factorialRecursion(num-1)
    


