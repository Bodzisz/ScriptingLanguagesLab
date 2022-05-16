import datetime

class Record:
    def __init__(self, dateRep, day, month, year, cases, deaths, country, geoId, country_code, popData2019, continentExp, cumulative_number):
        self.dateRep = dateRep
        self.date = datetime.datetime(int(year), int(month), int(day))
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)
        self.cases = int(cases)
        self.deaths = int(deaths)
        self.country = country
        self.geoId = geoId
        self.country_code = country_code
        self.popData2019 = popData2019
        self.continentExp = continentExp
        self.cumulative_numer = cumulative_number

    def __str__(self) -> str:
        return self.dateRep + " " + self.country