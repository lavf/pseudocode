erstelleFluege(Datum : Date, Plaetze : Integer) : Flug[]
    Flug Auswahl_Fluege := new Flug [Laenge von Linien_Fluege]
    Integer i, j

    // Linien_Fluege-Array einlesen
    von i := 0 solange i < Laenge von Linien_Fluege
        Flug flug := Linien_Fluege[i]

        // Wenn Bedingungen erfüllt sind
        wenn flug.getFlugDatum() = Datum und flug.getFreiePlaetze() >= Plaetze
            Integer temp := 0

            // Aufsteigende Sortierung in Bezug auf Preis
            solange (Auswahl_Fluege[temp] nicht leer und Auswahl_Fluege[temp].getPreis() < flug.getPreis())
                temp := temp + 1
            ende solange
            
            // Rückgang: Positionsveränderung beim Array wenn aktueller Preis im Auswahl_Fluege niedriger ist
            von j := Laenge von Auswahl_Fluege - 1 solange j > temp
                Auswahl_Fluege[j] := Auswahl_Fluege[j - 1]
            ende von

            Auswahl_Fluege[temp] := flug

        ende wenn

    ende von

Rueckgabe Auswahl_Fluege

ende von erstelleFluege