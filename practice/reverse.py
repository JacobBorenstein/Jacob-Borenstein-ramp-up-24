def reverse(string:str):
    reversed = ''
    vowels = "AEIOUaeiou"
    vowelsCount = 0

    for letter in string[::-1]:
        if letter in vowels:
            vowelsCount += 1
        reversed += letter
    
    return vowelsCount,reversed


