/*

Methoden zur Verfügung:

getElementsByTagName(String) : NodeList     // Methode der Klasse Node
getLength() : Integer			 			// Methode der Klasse NodeList
item(integer) : Node			 			// Methode der Klasse NodeList
getAttributes() : NamedNodeMap	 			// Methode der Klasse Node
item(integer) : Node			 			// Methode der Klasse NamedNodeMap
getNodeValue() : String  		 			// Methode der Klasse Node
getNodeName() : String			 			// Methode der Klasse Node
getChildNodes() : NodeList		 			// Methode der Klasse Node
getFirstChild() : Node			 			// Methode der Klasse Node

*/

nebenkosten(root : Element) : void
{
	Integer i := 0

	NodeList hausliste := root.getElementsByTagName("Haus")

	solange i < hausliste.getLength()
		Node haus := hausliste.item(i)
		Ausgabe "Haus: " haus.getAttributes().item(0).getNodeValue()
		
		Double gesamtkosten := 0
		NodeList hausattrib := haus.getChildNodes()
		Integer j := 0

		solange j < hausattrib.getLength()
			attrib := hausattrib.item(i)
			gesamtkosten := gesamtkosten + float-Wert vom attrib.getFirstChild().getNodevalue()
			Ausgabe attrib.getNodeName() & ": " & attrib.getFirstChild().getNodeValue()
			j := j + 1
		Ausgabe "Haus-Gesamtkosten:" & String-Wer vom gesamtkosten & "\n"
		i := i + 1
	
}