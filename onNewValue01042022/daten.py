"""
Folgende Klassen sind bereits vorhanden:
 _____________________________________________________________
|                             Value                           |
| - sensor_id: Integer                                        |
| - value: Double                                             |
| - time: Long                                                |
| ____________________________________________________________|
| + Konstruktor(sensor_id: Integer, value: Double, time: Long)|
| + getId() : Integer                                         |
| + getValue(): Double                                        |
| + getTime(): Long											  |
|_____________________________________________________________|
 ____________________________________________
|                 TempList                   |
|+ setValue(value: Value)                    |
|+ getValue(sensor_id, pos: Integer) : Value |
|+ getSize(sensor_id: Integer) : Integer     |
|____________________________________________|
"""


class Value(object):
    def __init__(self, sensor_id = 0, value = 0, time = 0):
        self._data = [sensor_id, value, time]
       # self._sensor_id = sensor_id
       # self._value = value
       # self._time = time

    def getId(self):
        return self._data[0]
        #return self._sensor_id
    
    def getValue(self):
        return self._data[1]
        #return self._value

    def getTime(self):
        return self._data[2]
        #return self._time

    def printValue(self):
        print("Value = " + str(self._data[0]) + ", " + str(self._data[1])+ ", " + str(self._data[2]))

    def stringValue(self):
        stringValue = "Value = " + str(self._data[0]) + ", " + str(self._data[1])+ ", " + str(self._data[2])
        return stringValue



class TempList(Value):
    def __init__(self):
        self._data = []

    def setValue(self, value):
        self._data.append(value)

    def getValue(self, sensor_id, pos):
        tempPos = 0
        for elem in self._data:
            if pos != 0 and elem._data[0] == sensor_id:
                tempPos += 1
                if tempPos == pos:
                    return elem
            elif pos == 0 and elem._data[0] == sensor_id:
                return elem
            
            

    def getSize(self, sensor_id):
        anzahl = 0
        for elem in self._data:
            if elem._data[0] == sensor_id:
                anzahl += 1
        return anzahl


temperaturwerte = [
    [20, 22, 23, 21, 19, 18, 20, 22, 23, 23, 24, 22, 21],
    [20, 22, 23, 21, 19, 18, 22, 22, 21, 23, 24, 22, 21],
    [20, 22, 20, 21, 19, 18, 22],
    [20, 20, 20, 21, 19, 18]
]

ergebnisse = [5,3,1,0]