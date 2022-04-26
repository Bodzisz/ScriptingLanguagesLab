from io import open
import time

all_cases = []
by_date = {}
by_country = {}


def load_dict(key, value, dest):
    if key in dest:
        dest[key] = dest[key] + [value]
    else:
        dest[key] = [value]


def load_content(path):
    with open(path, 'r', encoding='utf-8') as file:
        next(file)
        for line in file.readlines():
            data = line.split()
            all_cases.append((data[6], int(data[3]), int(data[2]), int(data[1]), int(data[5]), int(data[4])))
            load_dict((int(data[3]), int(data[2]), int(data[1])), (data[6], int(data[5]), int(data[4])), by_date)
            load_dict(data[6], (int(data[3]), int(data[2]), int(data[1]), int(data[5]), int(data[4])), by_country)


load_content("Covid.txt")


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.4f ms' % (method.__name__, (te - ts) * 1000))
            print(result)
        return result
    return timed


# 2
@timeit
def for_date_a(year, month, day):
    deaths = 0
    cases = 0
    for record in all_cases:
        if record[1] == year and record[2] == month and record[3] == day:
            deaths += record[4]
            cases += record[5]
    return deaths, cases

@timeit
def for_date_b(year, month, day):
    deaths = 0
    cases = 0
    for record in by_date[(year, month, day)]:
        deaths += record[1]
        cases += record[2]
    return deaths, cases

@timeit
def for_date_c(year, month, day):
    deaths = 0
    cases = 0
    for records in by_country.values():
        for record in records:
            if record[0] == year and record[1] == month and record[2] == day:
                deaths += record[3]
                cases += record[4]
    return deaths, cases

print("#2")
for_date_a(2020, 11, 25)
for_date_b(2020, 11, 25)
for_date_c(2020, 11, 25)

# 3
@timeit
def for_country_a(country):
    deaths = 0
    cases = 0
    for record in all_cases:
        if record[0] == country:
            deaths += record[4]
            cases += record[5]
    return deaths, cases

@timeit
def for_country_b(country):
    deaths = 0
    cases = 0
    for records in by_date.values():
        for record in records:
            if record[0] == country:
                deaths += record[1]
                cases += record[2]
    return deaths, cases

@timeit
def for_country_c(country):
    deaths = 0
    cases = 0
    for record in by_country[country]:
        deaths += record[3]
        cases += record[4]
    return deaths, cases

print("\n#3")
for_country_a('Afghanistan')
for_country_b('Afghanistan')
for_country_c('Afghanistan')

# 4
@timeit
def for_date_country_a(year, month, day, country):
    deaths = 0
    cases = 0
    for record in all_cases:
        if record[0] == country and record[1] == year and record[2] == month and record[3] == day:
            deaths += record[4]
            cases += record[5]
    return deaths, cases


@timeit
def for_date_country_b(year, month, day, country):
    deaths = 0
    cases = 0
    for record in by_date[(year, month, day)]:
        if record[0] == country:
            deaths += record[1]
            cases += record[2]
    return deaths, cases


@timeit
def for_date_country_c(year, month, day, country):
    deaths = 0
    cases = 0
    for record in by_country[country]:
        if record[0] == year and record[1] == month and record[2] == day:
            deaths += record[3]
            cases += record[4]
    return deaths, cases


print("\n#4")
for_date_country_a(2020, 11, 25, 'Afghanistan')
for_date_country_b(2020, 11, 25, 'Afghanistan')
for_date_country_c(2020, 11, 25, 'Afghanistan')
