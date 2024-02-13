def Fact3(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * Fact(n - 1)



from math import ceil
def prost3(n):
    i = 2
    while i <= ceil(n ** (1 / 2)):
        if n % i == 0:
            return "не просте"
        i = i + 1
    return "просте"

def FiveDegree3(x):
    if x == 1:
        return "Число є степенем п'ятірки"
    if x != int(x):
        return "Число не є степенем п'ятірки"
    else:
        return FiveDegree3(x / 5)
