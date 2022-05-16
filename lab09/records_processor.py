import datetime

class Records_processor:
    def __init__(self, records_copy):
        self.records = records_copy
        self.months = {
            'January': 1,
            'Febuary': 2,
            'March': 3,
            'April': 4,
            'May': 5,
            'June': 6,
            'July': 7,
            'August': 8,
            'September': 9,
            'October': 10,
            'November': 11,
            'December': 12, 
            }

    def filter_country(self, country):
        filtered = []
        for record in self.records:
            if record.country == country:
                filtered.append(record)
        self.records = filtered

    def filter_continent(self, continent):
        filtered = []
        for record in self.records:
            if record.continentExp == continent:
                filtered.append(record)
        self.records = filtered

    def filter_month(self, month):
        filtered = []
        for record in self.records:
            if record.month == self.months[month]:
                filtered.append(record)
        self.records = filtered

    def filter_date(self, month, day):
        filtered = []
        for record in self.records:
            if record.month == self.months[month] and record.day == day:
                filtered.append(record)
        self.records = filtered

    def filter_date_from(self, from_day, from_month):
        filtered = []
        for record in self.records:
            from_tmp_date = datetime.datetime(record.year, self.months[from_month], from_day)
            if record.date > from_tmp_date:
                    filtered.append(record)
        self.records = filtered

    def filter_date_till(self, till_day, till_month):
        filtered = []
        for record in self.records:
            till_tmp_date = datetime.datetime(record.year, self.months[till_month], till_day)
            if record.date < till_tmp_date:
                    filtered.append(record)
        self.records = filtered