from daten import arrays, absatz, absatz1, absatz2

def ermittlePruefziffer(array):
    pruefziffer = 0
    i = 0

    while i < len(array):
        if i % 2 == 0:
            pruefziffer = array[i] * 1 + pruefziffer
        else:
            pruefziffer = array[i] * 3 + pruefziffer
        
        i = i + 1

    pruefziffer = pruefziffer % 10

    return pruefziffer

def sucheTopseller(kriterium, vorgabewert, absatz):
    i = 0
    absatzStk = 0
    pruefziffer = ""

    while i < len(absatz):
        if absatz[i][kriterium] == vorgabewert:
            if absatz[i][4] > absatzStk:
                absatzStk = absatz[i][4]
                pruefziffer = str(absatz[i][0]) + str(absatz[i][1]) + str(absatz[i][2]) + str(absatz[i][3])
           
        i = i + 1
    
    if pruefziffer == "":
         pruefziffer = "Das Kriterium {:0} mit Vorgabewert {:1} hatte keinen Absatz".format(kriterium, vorgabewert)

    return pruefziffer

print(sucheTopseller(0,123, absatz))