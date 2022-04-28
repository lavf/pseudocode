import xml.etree.ElementTree as ET

tree = ET.parse('nebenkosten_28042022/nebenkosten.xml')
root = tree.getroot()

#for child in root:
#    print(child.tag, child.attrib)

def nebenkosten(root):
    i = 0 

    while i < len(root):
        print(root[i].tag + ": H" +  root[i].attrib['ID'])
        j = 0
        gesamtkosten = 0.0
        while j < len(root[i]):
            gesamtkosten += float(root[i][j].text)
            print(root[i][j].tag + ": " + root[i][j].text)
            j += 1
        print("Haus-Gesamtkosten: " + str(gesamtkosten) + "\n")
        i += 1

nebenkosten(root)
