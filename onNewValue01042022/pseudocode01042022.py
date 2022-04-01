from daten import temperaturwerte, Value

def onNewValue(sensor_id, value, time, tempListObj):
    valueObj = Value(sensor_id, value, time)
    tempListObj.setValue(valueObj)


def maxPeriod(sensor_id, mindestwert):
    i = 0
    hoechstesPeriod = 0

    while i < len(temperaturwerte[sensor_id]):
        period = 0
        while i < len(temperaturwerte[sensor_id]) and temperaturwerte[sensor_id][i] >= mindestwert:
            period = period + 1
            i = i + 1

        if period > hoechstesPeriod:
            hoechstesPeriod = period
        
        i = i + 1

    return hoechstesPeriod



