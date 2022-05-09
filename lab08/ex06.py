import ex05
import sys

class bcolors:
    OK = "\033[97m"
    FAIL = "\033[95m"
    ENDC = "\033[0m"


class PersonTester:

    def run_tests():
        with open(r"lab08\ex06_data.txt", 'r', encoding="utf-8") as file:
            for line in file:
                try:
                    ex05.Person.fromString(line)
                    print('{0:50s}           {1:30s}'.format(line[:len(line) - 1], bcolors.OK + "        OK" + bcolors.ENDC))
                except Exception as e:
                    print('{0:50s}           {1:30s}          {2:30s}'.format(line[:len(line) - 1], bcolors.FAIL + "        FAILED       " + bcolors.ENDC, str(e)))


PersonTester.run_tests()
