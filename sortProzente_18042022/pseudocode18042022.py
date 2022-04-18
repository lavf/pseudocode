import numpy as np

prozent = [38,33,30,31,25]

def sortProzente(prozent):    
    sortProzente = np.zeros((len(prozent),2),dtype=int)
    i = 0
    

    while i < len(prozent):
        sortProzente[i][0] = i
        sortProzente[i][1] = prozent[i]
        i += 1

    i = 0

    while i < len(sortProzente) - 1:
        j = 0
        while j < len(sortProzente) - i - 1:
            if sortProzente[j][1] > sortProzente[j+1][1]:
                tempProAnt = sortProzente[j][1]
                tempInd = sortProzente[j][0]
                sortProzente[j][1] = sortProzente[j+1][1]
                sortProzente[j][0] = sortProzente[j+1][0]
                sortProzente[j+1][1] = tempProAnt
                sortProzente[j+1][0] = tempInd
            j += 1
        i += 1
    
    return sortProzente

print(sortProzente(prozent))