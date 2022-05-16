from tkinter import *
import tkinter.messagebox
import command_parser
from datetime import datetime

command_parser.set_records("C:\\Users\\kacpe\\University\\bednar\\me\\Covid.txt")

def makeGui():
    window = Tk()

    window.title("Covid 2020 Database")
    window.geometry('400x450')

    # 1
    frame_deaths_or_cases = Frame(window)
    frame_deaths_or_cases.grid(column=1, row=0)
    deaths_or_cases = BooleanVar()

    label1 = Label(window, text="Deaths or cases: ")
    label1.grid(column=0, row=0)
    deaths_or_cases_radio = Radiobutton(frame_deaths_or_cases, text="deaths", value=True, variable=deaths_or_cases)
    deaths_or_cases_radio.grid(column=0, row=0)
    deaths_or_cases_radio = Radiobutton(frame_deaths_or_cases, text="cases", value=False, variable=deaths_or_cases)
    deaths_or_cases_radio.grid(column=1, row=0)

    # 2
    label2 = Label(window, text="Country: ")
    label2.grid(column=0, row=2)
    country = Entry(window, width=30)
    country.grid(column=1, row=2)

    # 3
    label3 = Label(window, text="Continent: ")
    label3.grid(column=0, row=3)
    continent = Entry(window, width=30)
    continent.grid(column=1, row=3)

    # 4
    label4 = Label(window, text="Month:")
    label4.grid(column=0, row=4)
    month = Entry(window, width=30)
    month.grid(column=1, row=4)

    # 5
    label5 = Label(window, text="From: ")
    label5.grid(column=0, row=5)
    from_date = Entry(window, width=30)
    from_date.grid(column=1, row=5)

    # 5
    label7 = Label(window, text="Till: ")
    label7.grid(column=0, row=7)
    till_date = Entry(window, width=30)
    till_date.grid(column=1, row=7)

    # 6
    frame = Frame(window)
    frame.grid(column=1, row=10)

    total = BooleanVar()

    label11 = Label(window, text="Sum: ")
    label11.grid(column=0, row=10)
    sumRadioOn = Radiobutton(frame, text="on", value=True, variable=total)
    sumRadioOn.grid(column=0, row=0)
    sumRadioOn = Radiobutton(frame, text="off", value=False, variable=total)
    sumRadioOn.grid(column=1, row=0)

    def process():
        country_value = country.get().lower().capitalize() if country.get() != "" else None
        continent_value = continent.get().lower().capitalize() if continent.get() != "" else None
        month_value = month.get().lower().capitalize() if month.get() != "" else None
        from_date_value = from_date.get() if from_date.get() != "" else None
        till_date_value = till_date.get() if till_date.get() != "" else None

        if total.get():
            command_parser.process("Set total on")
        else:
            command_parser.process("Set total off")

        command = ""
        if deaths_or_cases.get():
            command += "Show deaths "
        else:
            command += "Show cases "

        if country_value != None:
            command += "in " + country_value + " "
        if continent_value != None:
            command += "in " + continent_value + " "
        if month_value != None:
            command += "in " + month_value + " "
        if from_date_value != None:
            command += "from " + from_date_value + " "
        if till_date_value != None:
            command += "till " + till_date_value + " "
        try:
            outcome = command_parser.process(command)
            top= Toplevel(window)
            top.geometry("500x800")
            top.title("Child Window")
            scrollbar = Scrollbar(top)
            scrollbar.pack(side = RIGHT, fill = Y)    

            mylist = Listbox(top, yscrollcommand = scrollbar.set, width=100)
            for line in outcome.splitlines():
                mylist.insert(END, line)
            mylist.pack( side = LEFT, fill = BOTH)
            scrollbar.config( command = mylist.yview)
        except Exception as e:
            tkinter.messagebox.showinfo("ERROR", e)

        

    process_button = Button(window, text="Process", command=process)
    process_button.grid(column=1, row=11)


    label12 = Label(window, text="Database textfile path: ")
    label12.grid(column=0, row=12)
    source_path = Entry(window, width=30)
    source_path.grid(column=1, row=12)

    def set_source():
        try:
            source_path_value = source_path.get()
            command_parser.set_records(source_path_value)
            source_path.delete(0, 'end')
            tkinter.messagebox.showinfo("INFO", "Database textfile was succesfully set!")
        except Exception as e:
            tkinter.messagebox.showinfo("ERROR", e)
        


    

    source_button = Button(window, text="Set", command=set_source)
    source_button.grid(column=1, row=13)

    window.mainloop()

