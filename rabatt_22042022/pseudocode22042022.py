rabatt1 = [
    ['A', 2.0],
    ['B', 2.5],
    ['C', 7.0],
    ['D', 6.0],
    ['E', 5.0]
    ]

artikel = [
    [1, 'Dünger','A', 7.80, 2],
    [2, 'Garteneinfassung Granit 10 X 20 X 100', 'B', 94.86, 20],
    [3, 'Rosen', 'C', 56.00, 3],
    [4, 'Werkzeugset', 'D', 87.50, 1],
    [5, 'Fliesen, Feinsteinzeug 43 X 43', 'B', 40.00, 5]
]

def rabatt():
    i = 0
    summeRabatt = 0.0

    while i < len(artikel):
        j = 0
        while j < len(rabatt1):
            if rabatt1[j][0] == artikel[i][2]:
                summeRabatt += (artikel[i][3] * artikel[i][4]) * rabatt1[j][1]/100
                break
            j += 1
        i += 1

    return summeRabatt

print(rabatt())
