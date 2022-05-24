import console
import command_parser
import gui
from logger import log_info


def run(in_gui):
    if in_gui:
        log_info("Application started - GUI Version")
        gui.GUI()
    else:
        log_info("Application started - Console Version")
        command_parser.set_records("C:\\Users\\kacpe\\University\\bednar\\me\\Covid.txt")
        while True:
            console.print_menu()
            choice = console.get_integer("Choice")
            if choice == 1:
                source = console.get_string("Enter file path")
                command_parser.set_records(source)
            elif choice == 2:
                command = console.get_string("Enter command")
                try:
                    result = command_parser.process(command)
                    print(result)
                except Exception as e:
                    print(e)