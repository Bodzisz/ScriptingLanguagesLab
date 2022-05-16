import record
from logger import log_warn

def read_records(path):
    records = []
    countries = set()
    with open(path, 'r', encoding="utf-8") as file:
            for i, line in enumerate(file.readlines()[1:]):
                line_data = line.split()
                if len(line_data) == 12:
                    records.append(record.Record(
                        line_data[0],
                        line_data[1],
                        line_data[2],
                        line_data[3],
                        line_data[4],
                        line_data[5],
                        line_data[6],
                        line_data[7],
                        line_data[8],
                        line_data[9],
                        line_data[10],
                        line_data[11]
                        ))
                    countries.add(line_data[6])
                else:
                    log_warn("INVALID RECORD IN LINE " + str(i))
    return (records, countries)