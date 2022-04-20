/*
Die dline AG will QR-Codes mit Werbebotschaften einsetzen. Zur Erstellung dieser QR-Codes soll 
eine Methode entwickelt werden.

Der Werbetext soll wie folgt codiert werden:
1. Setzen der Kennung „0100" für den Zeichensatz IS0-8859-1 an den Anfang des Codes
2. Codierung des Textes: Für jedes Zeichen des Werbetextes wird aus dem Zeichensatz IS0-8859-1 der 
entsprechende Binärcode als String ermittelt und an den Code angefügt. Der Binärcode setzt sich aus
einem Zeilenwert und einem Spaltenwert zusammen (siehe unten stehende Tabelle).
Beispiel: Das Zeichen „ G" hat den Binärcode „ 01000111" (Zeile: „ 0100", Spalte: „ 0111 ")
3. Anfügen der Ende-Kennung „0000" an das Ende des Codes
Beispiel: Code für den Werbetext „Günstig! ".

| Kennung für Z. |     G    |     ü    |     n    |     s    |     t    |     i    |     g    |     !    | Ende-Kennung
|     0100       | 01000111 | 11111100 | 01101110 | 01110011 | 01110100 | 01101001 | 01100111 | 00100001 | 0000

Die Zeichen des Zeichensatzes IS0-8859-1 und dessen Binärwerte sind in dem zweidimensionalen String-Array zeichenSatzgespeichert.
Das Array ist wie folgt aufgebaut (Zeilen- und Spaltenangaben sind nicht Teil des Arrays.):

Array zeichenSatz

Zeile  0    1     2    3    4    5    6    7 8 9 10 11 12 13 14 14 16
0          0000 0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111
1     0010  SP    !    "    #    $    %    &    '    (    )    *    +    ,    -    .    /  
2     0011  0     1    2    3    4    5    6    7    8    9    :    <    =    >    ?    '
3     0100  @     A    B    C    D    E    F    G    H    1    J    K    L    M    N    0
4     0101  p     Q    R    S    T    U    V    W    X    Y    Z    [    \    ]    "    _ 
5     0110  `     a    b    c    d    e    f    g    h    i    j    k    l    m    n    o
6     0111  p     q    r    s    t    u    v    w    x    y    z    {    1    }    ~  
7     1010 NBSP   ¡    tf   ,    t    tl   ~    §    ..   ©    a         ~   SHY   ®    1((
8     1011  0     ±    2    3    IJ   1I   1    ~]-  0    ))   11.  i    1lz  %    i    ,
9     1100  A     A    Ä    Ä    Ä    A    ff.  c    E    E    E    E    i    i    T   'j
10    1101  E>    Ñ    ö    ö    ö    0    ö    X    0    ü    ü    u    ü    y    p    ß
11    1110  ä     a    ä    Ä    ä    ä    CB   et   e    e    e    e    i    i    i   "j
12    1111  ö     ñ    6    ö    ö    ö    ö    "    u    u    ü    ü    y    p    y


laengeZeichenkette(zeichenkette : String) : int

zeichen(zeichenkette : String, stelle : int) : char

*/

qrCode(werbetext: String) {
	String ergebnisCode := "0100"
	Integer i = 0
	
	solange i < laengeZeichenkette(werbetext)
		j := 1
		solange j < 13
			z := 1
			solange z < 17
				wenn zeichen(werbetext, i) = zeichenSatz[j][z] dann
					ergebnisCode := ergebnisCode & zeichenSatz[j][0] & zeichenSatz[0][z]
				ende wenn
				z := z + 1
			ende solange
			j := j + 1
		ende solange
		i := i + 1
	ende solange
	
	ergebnisCode := ergebnisCode & "0000"

	rueckgabe ergebnisCode
}