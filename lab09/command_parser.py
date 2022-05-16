import records_reader
import records_processor
import os.path
from logger import log_info, log_error

records = []
total = False
death_or_cases = 'cases'
months = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
continents = ["Asia", "Europe", "Africa", "America", "Oceania"]
countries = set()

def set_records(path):
    global records
    global countries
    if os.path.isfile(path):
        records, countries = records_reader.read_records(path)
    else:
        error_text = "File is invalid!"
        log_error(error_text)
        raise Exception(error_text)

def process(command):
    log_info("Process command: {}".format(command))
    if command == 'exit':
        exit()
    else:
        if records != []:
            records_instance = records_processor.Records_processor(records.copy())
            command = command.split()
            if command[0].capitalize() == 'Set' and command[1] == 'total':
                global total
                if command[2] == 'on':
                    total = True
                elif command[2] == 'off':
                    total = False
            elif command[0].capitalize() == 'Show':
                if len(command) > 1:
                    global death_or_cases
                    if command[1] == 'deaths':
                        death_or_cases = 'deaths'
                    elif command[1] == 'cases':
                        death_or_cases = 'cases'
                    
                    global months, countries, continents
                    for index in range(1, len(command)):
                        if command[index] == 'in':
                            if index + 1 < len(command):
                                index += 1
                                in_what = command[index].capitalize()
                                if in_what in months:
                                    records_instance.filter_month(in_what)
                                elif in_what in continents:
                                    records_instance.filter_continent(in_what)
                                elif in_what in countries:
                                    records_instance.filter_country(in_what)
                                else:
                                    raise Exception("Wrong command") 
                            else:
                                raise Exception("Wrong command")
                        elif command[index] == 'from':
                            if index + 2 < len(command):
                                index += 2
                                from_month = command[index-1].capitalize()
                                from_day = int(command[index])
                                if from_month in months and from_day > 0 and from_day < 32:
                                    records_instance.filter_date_from(from_day, from_month)
                                else:
                                    raise Exception("Wrong command")
                        elif command[index] == 'till':
                            if index + 2 < len(command):
                                index += 2
                                till_month = command[index-1].capitalize()
                                till_day = int(command[index])
                                if till_month in months and till_day > 0 and till_day < 32:
                                    records_instance.filter_date_till(till_day, till_month)
                                else:
                                    raise Exception("Wrong command")  

                return handle_outcome(records_instance.records)
        else:
            error_text = "No data found!"
            log_error(error_text)
            raise Exception(error_text)


def handle_outcome(outcome_records):
    result = ""
    if death_or_cases == 'deaths':
        if total:
            total_value = 0
            for record in outcome_records:
                total_value += record.deaths
            result = "Total deaths: " + str(total_value)
        else:
            for record in outcome_records:
                result += '{0:25s} {1:15s} {2:20s} {3:6d} \n'.format(str(record.date), record.continentExp, record.country, record.deaths)
    elif death_or_cases == 'cases':
        if total:
            total_value = 0
            for record in outcome_records:
                total_value += record.deaths
            result = "Total cases: " + str(total_value)
        else:
            for record in outcome_records:
                result += '{0:25s} {1:15s} {2:20s} {3:6d} \n'.format(str(record.date), record.continentExp, record.country, record.cases)
    return result