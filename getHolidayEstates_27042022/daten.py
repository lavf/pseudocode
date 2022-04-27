class Vacancy(object):
    def __init__(self, date, vacant ):
        self._vacancydata = [date, vacant]

    def __getitem__(self, item):
        return self._vacancydata[item]

    def getDate(self):
        return self._vacancydata[0]

    def getVacant(self):
        return self._vacancydata[1]
       


class Estate(object):
    def __init__(self, destination, bedroom, persons, price, vacancy):
        self._estatedata = [destination, bedroom, persons, price, vacancy]


    def __getitem__(self, item):
        return self._estatedata[item]

    def getDestination(self):
        return self._estatedata[0]

    def getBedroom(self):
        return self._estatedata[1] 

    def getPersons(self):
        return self._estatedata[2] 

    def getPrice(self):
        return self._estatedata[3]
    
    def getVacancy(self):
        return self._estatedata[4]

    def getVacancies(self, arrival, duration):
        i = 0
        ergebnis = False
        vacancies = self._estatedata[4]
        while i < len(vacancies):
            if vacancies[i].getDate() == arrival:
                if vacancies[i].getVacant() == True:
                    j = 1
                    match = 1
                    if duration + i < len(vacancies):
                        while j < duration:
                            if vacancies[j][1] == 1:
                                match += 1                
                            j += 1
                if match == duration:
                    ergebnis = True
            i += 1
        return ergebnis


class List(object):
    def __init__(self):
        self._listdata = []

    def __getitem__(self, item):
        return self._listdata[item]

    def createList(self):
        return self._listdata

    def add(self, estate):
        self._listdata.append(estate)
        return self._listdata

    def len(self):
        return len(self._listdata)  

vacancy1 = [Vacancy('01.06.22', True),
            Vacancy('02.06.22', True),
            Vacancy('03.06.22', True),
            Vacancy('04.06.22', True),
            Vacancy('05.06.22', True),
            Vacancy('06.06.22', True),
            Vacancy('07.06.22', True),
            Vacancy('08.06.22', 1),
            Vacancy('09.06.22', 1),
            Vacancy('10.06.22', 1),
            Vacancy('11.06.22', 1),
            Vacancy('12.06.22', 1),
            Vacancy('13.06.22', 1),
            Vacancy('14.06.22', 1),
            Vacancy('15.06.22', 1),
            Vacancy('16.06.22', 1),
            Vacancy('17.06.22', 1),
            Vacancy('18.06.22', 1),
            Vacancy('19.06.22', 1),
            Vacancy('20.06.22', True),
            Vacancy('21.06.22', True),
            Vacancy('22.06.22', True),
            Vacancy('23.06.22', True),
            Vacancy('24.06.22', True),
            Vacancy('25.06.22', True),
            Vacancy('26.06.22', True),
            Vacancy('27.06.22', True),
            Vacancy('28.06.22', True),
            Vacancy('29.06.22', True),
            Vacancy('30.06.22', True)            
            ]

vacancy2 = [Vacancy('01.06.22', True),
            Vacancy('02.06.22', True),
            Vacancy('03.06.22', True),
            Vacancy('04.06.22', True),
            Vacancy('05.06.22', True),
            Vacancy('06.06.22', True),
            Vacancy('07.06.22', True),
            Vacancy('08.06.22', False),
            Vacancy('09.06.22', False),
            Vacancy('10.06.22', 0),
            Vacancy('11.06.22', 0),
            Vacancy('12.06.22', 0),
            Vacancy('13.06.22', 0),
            Vacancy('14.06.22', 0),
            Vacancy('15.06.22', 0),
            Vacancy('16.06.22', 0),
            Vacancy('17.06.22', 0),
            Vacancy('18.06.22', 0),
            Vacancy('19.06.22', 0),
            Vacancy('20.06.22', True),
            Vacancy('21.06.22', True),
            Vacancy('22.06.22', True),
            Vacancy('23.06.22', True),
            Vacancy('24.06.22', True),
            Vacancy('25.06.22', True),
            Vacancy('26.06.22', True),
            Vacancy('27.06.22', True),
            Vacancy('28.06.22', True),
            Vacancy('29.06.22', True),
            Vacancy('30.06.22', True)            
            ]

estateList = [ Estate('Mallorca',   2, 4, 90.00, vacancy1),
                Estate('Kopenhagen', 1, 2, 180.00, vacancy2),
                Estate('Mallorca',   2, 5, 100.00, vacancy1),
                Estate('Kopenhagen', 1, 1, 200.00, vacancy2),
                Estate('Kopenhagen', 2, 3, 250.00, vacancy1)
            ]

def getEstates(destination):
    i = 0
    ergebnis = []

    while i < len(estateList):
        if estateList[i].getDestination() == destination:
            ergebnis.append(estateList[i])
        i += 1
    return ergebnis

