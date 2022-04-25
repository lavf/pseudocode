

def pruefePasswort(passwort):

    pos = 0
    laenge = 0
    zaehl_Gross = 0
    zaehl_Klein = 0
    zaehl_Sonder = 0
    zaehl_Ziff = 0
    zeichen = ""

    ergebnis = ""
    laenge = len(passwort)
    erlaubteZeichen = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz§$%&/()=?*'-:;#+@1234567890"
    zaehl_Verbot = 0

    if laenge >= 8 and laenge <= 10:
        while pos < laenge:
            j = 0
            zeichen = passwort[pos]
            while j < len(erlaubteZeichen):
                if zeichen == erlaubteZeichen[j]:                    
                    if j >= 0 and j <= 25:
                        zaehl_Gross += 1
                        break
                    elif j >= 26 and j <= 52:
                        zaehl_Klein += 1
                        break
                    elif j >= 53 and j <= 68:
                        zaehl_Sonder += 1
                        break
                    elif j >= 69 and j <= 78:
                        zaehl_Ziff += 1
                        break
                elif j == 78 and zeichen != erlaubteZeichen[j]:
                    zaehl_Verbot += 1
                j += 1

            pos += 1
        
        if (zaehl_Gross * zaehl_Klein * zaehl_Sonder * zaehl_Ziff) > 0 and zaehl_Verbot == 0:
            ergebnis = "Passwort ist gültig."
        elif zaehl_Verbot != 0:
            ergebnis = "Passwort enthält ein verbotenes Zeichen"
        else:
            ergebnis = "Passwort ist nicht gültig. Es fehlt ein zwingendes Zeichen."
    else:
        ergebnis = "Länge des Passworts ist nicht gültig. Es muss vom 8 bis zum 10 zeichen haben."
    
    return ergebnis

print(pruefePasswort("Z908\9a34"))
