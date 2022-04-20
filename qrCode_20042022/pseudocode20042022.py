zeichenSatz = [
    ["NULL","0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"],
    ["0010", "SP", "!", "'", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/" ],
    ["0011",  "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "?"],
    ["0100",  "@", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"],
    ["0101",  "p", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "[", "/", "]", "^", "_"],
    ["0110",  "`", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"],
    ["0111",  "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~", "NULL"]
]


def laengeZeichenkette(zeichenkette):
    return len(zeichenkette)

def zeichen(zeichenkette, i):
    return zeichenkette[i]

def qrCode(werbetext):
    ergebnisCode = "0100 "
    i = 0

    while i < laengeZeichenkette(werbetext):
        j = 1
        while j < 7:
            z = 1
            while z < 17:
                if zeichen(werbetext, i) == zeichenSatz[j][z]:
                    ergebnisCode = ergebnisCode + zeichenSatz[j][0] + zeichenSatz[0][z] + " "
                z += 1
            j += 1
        i += 1
    
    ergebnisCode = ergebnisCode + "0000"
    return ergebnisCode

print(qrCode("Gunstig!")) 

#| Kennung für Z. |     G    |     ü    |     n    |     s    |     t    |     i    |     g    |     !    | Ende-Kennung
#|     0100       | 01000111 | 11111100 | 01101110 | 01110011 | 01110100 | 01101001 | 01100111 | 00100001 | 0000

#   ErgebnisCode              (u statt ü)
#      0100         01000111   01110101   01101110   01110011   01110100   01101001   01100111   00100001   0000
    