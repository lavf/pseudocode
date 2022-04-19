/*

Routen = [
	['A','B'],
	['A','C','B'],
	['A','D','E','B'],
]

Funktionen zur Verfügung

holeStreckeGewicht(SB: String, SE: String) : Integer
holeStreckePreis(SB: String, SE: String) : Double

Strecken Beginn = SB
Strecken Ende = SE

*/

findeRoute(Gewicht : Integer) : Integer {
	Integer i := 0
	Double summeGewicht := 0
	Double summeFrachtKosten := 0
	Double summeAktFracht := 0
	Double summeAktGewicht := 0
	Integer index := 0
	Integer aktIndex := 0
	Integer indexErgebnis := 0

	solange i < laenge(Route)
		j := 0
		Double subFracht := 0
		Double subGewicht := 0
		solange j < laenge(Route[i]) - 1
			Double subGewicht := holeStreckeGewicht(Route[i][j], Route[i][j+1]) + subGewicht			
			Double subFracht := holeStreckePreis(Route[i][j], Route[i][j+1]) + subFracht			
			j:= j + 1
		ende solange

		wenn i = 0 dann
			summeGewicht := subGewicht
			summeFrachtKosten := subFracht
			index := i
		sonst
			summeAktGewicht := subGewicht
		    summeAktFracht:= subFracht
			aktIndex := i
		ende wenn

		wenn i <> 0
			wenn summeGewicht <= Gewicht und summeAktGewicht <= Gewicht dann
				wenn summeAktFracht > summeFrachtKosten dann
					indexErgebnis := index
				sonst
					indexErgebnis := aktIndex
				ende wenn			
			sonst wenn summeGewicht > Gewicht und summeAktGewicht <= Gewicht
				indexErgebnis := aktIndex
			sonst wenn summeGewicht <= Gewicht und summeAktGewicht > Gewicht
				indexErgebnis := index
			sonst
				indexErgebnis := index
			
			summeGewicht := summeAktGewicht
			summeFrachtKosten := summeAktFracht
			index := aktIndex 
			ende wenn
		ende wenn
		
		
		i := i + 1
	ende solange

	rueckgabe indexErgebnis
ende von Funktion findeRoute
}