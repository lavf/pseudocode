matches = [
    [85,93334,2],
    [80,48774,1],
    [98,56446,2],
    [71,33961,10],
    [21,73447,2],
    [81,49982,2]
]

def auswertung(matches, schwelle, finger):
    i = 0

    while i < len(matches):
        if (matches[i][2] != finger and finger != 0) or matches[i][0] < schwelle:
            # Lösche
            matches.remove(matches[i])
        else:
            i += 1

    j = len(matches) - 1

    # Bubblesort
    while j > 0:
        z = 0   
        while z < j:
            if matches[z][0] < matches[z+1][0]:
                temp = matches[z+1]
                matches[z+1] = matches[z]
                matches[z] = temp
            z += 1
        j -= 1

    return matches


print(auswertung(matches, 80, 2))  

# Ergebnis:  [[98, 56446, 2], [85, 93334, 2], [81, 49982, 2]]
