
def laenge(stringArray):
    laengeInteger = len(stringArray)
    return laengeInteger

def toString(integer):
    integerToString = str(integer)
    return integerToString

def add(stringArray, string):
    stringArray.append(string)
    return stringArray


ergebnisse = [
    ['Z','Z','Z','Z','%','10','7','M','%','5','P','H','H'],
    ['Z','Z','Z','Z','M','%','5','P','F','F','F','H','V'],
    ['Z','Z','Z','Z','M','%','5','P'],
    ['I','8','8','8','8'],
    ['%','5','G'],
    ['%','5','G','%','10','7'],
    ['%','5','Z'],
    ['1']
]

unkomprimiert = [
    ['Z','Z','Z','Z','7','7','7','7','7','7','7','7','7','7','M','P','P','P','P','P','H','H'],
    ['Z','Z','Z','Z','M','P','P','P','P','P','F','F','F','H','V'],                
    ['Z','Z','Z','Z','M','P','P','P','P','P'],
    ['I','8','8','8','8'],
    ['G','G','G','G','G'],
    ['G','G','G','G','G','7','7','7','7','7','7','7','7','7','7'],
    'ZZZZZ',
    ['1']
]