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


def C3(n,k):
    return Fact(n)/(Fact(k) * Fact(n - k))
for i in range(n + 1):
    lst.append(int(C3(n, i)))


def Rozklad3(v):
    Divider = 2
    Degree = 0
    d = {}
    w = v
    while v > 1:
        if v % Divider == 0:
            Degree += 1
            v = v / Divider
            if v == 1 and Degree != 0:
                d[Divider] = Degree
                k = Divider
            continue
        else:
            if Degree != 0:
                d[Divider] = Degree
            Divider += 1
            Degree = 0
    p = ""
    for i in d.keys():
        if i == k:
            p = p + '(' + str(i) + ' ^ ' + str(d[i]) + ')'
        else:
            p = p + '(' + str(i) + ' ^ ' + str(d[i]) + ')' + '  *  '
    return str(w)+ ' = '+ p
