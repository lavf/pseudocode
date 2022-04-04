"""
Routen
Route 	Strecken
0 		B- HH; HH- K
1 		B-K
2 		B - L; L - F; F - K

Route-Objekts 2
Strecke 	Start 	Ziel 	Preis
0 			B		L 		1.10
1 			L 		F 		1.60
2 			F 		K 		0.90

"""

routen = [
    ['BK','B - HH','HH - K'],
    ['BK','B - K'],
    ['BK','B - L', 'L - F', 'F - K']
]

strecken0 = [
    ['B - HH', 2.10],
    ['HH - K', 2.90]
]

strecken1 = [
    ['B - K', 6.10]
]

strecken2 = [
    ['B - L', 1.10],
    ['L - F', 1.60],
    ['F - K', 0.90]
]

def erstelleAngebot(startZielAbkuerzung):
    i = 0
    
    subSumme = 0
    pos = 0
    while i < len(routen):
        if routen[i][0] == startZielAbkuerzung:
            j = 0
            tempSumme = 0
            if routen[i][1] == strecken0[0][0]:
                while j < len(strecken0):                
                    tempSumme += strecken0[j][1]
                    j += 1
            elif routen[i][1] == strecken1[0][0]:
                while j < len(strecken1):                
                    tempSumme += strecken1[j][1]
                    j += 1
            elif routen[i][1] == strecken2[0][0]:
                while j < len(strecken2):                
                    tempSumme += strecken2[j][1]
                    j += 1
            if subSumme == 0:
                subSumme = tempSumme
                pos = i
            if subSumme > tempSumme:
                subSumme = tempSumme
                pos = i
        i += 1
        

    print('Index = ' + str(pos) + ', niedrigste Summe = ' + str(subSumme))

erstelleAngebot('BK')