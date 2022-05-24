from tkinter import *
from tkinter import ttk, simpledialog, messagebox
import tkinter.messagebox
import command_parser
import os
from tkcalendar import DateEntry
from datetime import datetime

command_parser.set_records("C:\\Users\\kacpe\\University\\bednar\\me\\Covid.txt")


class GUI:

    def __init__(self):
        self.countries = list(command_parser.countries)
        self.country_switch = False
        self.continents = command_parser.continents
        self.continent_switch = False
        self.months = command_parser.months
        self.month_switch = False
        self.comboboxes = {}
        self.checkboxes = {}
        self.checkboxes_objects = []
        self.window = None
        self.toolbar_images = None
        self.toolbar = None
        self.menubar = None
        self.sort_switch = False
        self.sorting_container = []
        self.radiobutions = {}
        self.sorting_var = None
        self.statusbar = None
        self.from_date = None
        self.till_date = None
        self.total = None
        self.deaths_or_cases = None
        self.make_gui()



    def make_gui(self):
        self.window = Tk()
        self.sorting_var = StringVar()

        self.window.title("Covid 2020 Database")
        self.window.geometry('400x400')
        self.create_toolbar()
        self.create_menu()
        self.add_status_bar("Status: ")

        # 1
        frame_deaths_or_cases = Frame(self.window)
        frame_deaths_or_cases.grid(column=1, row=1)
        self.deaths_or_cases = BooleanVar()

        label1 = Label(self.window, text="Deaths or cases: ")
        label1.grid(column=0, row=1)
        deaths_or_cases_radio = Radiobutton(frame_deaths_or_cases, text="deaths", value=True, variable=self.deaths_or_cases)
        deaths_or_cases_radio.grid(column=0, row=1)
        deaths_or_cases_radio = Radiobutton(frame_deaths_or_cases, text="cases", value=False, variable=self.deaths_or_cases)
        deaths_or_cases_radio.grid(column=1, row=1)

        # 2
        # label2 = Label(self.window, text="Country: ")
        # label2.grid(column=0, row=2)
        # country = Entry(self.window, width=30)
        # country.grid(column=1, row=2)

        self.country_switch = False
        self.checkboxes["Country"] = self.add_dropdown_list_widget_with_checkbox(
            self.window,
            "Country",
            self.toggle_country_switch,
            self.countries,
            column=0,
            row=2,
        )

        # 3
        # label3 = Label(self.window, text="Continent: ")
        # label3.grid(column=0, row=3)
        # continent = Entry(self.window, width=30)
        # continent.grid(column=1, row=3)

        self.continent_switch = False
        self.checkboxes["Continent"] = self.add_dropdown_list_widget_with_checkbox(
            self.window,
            "Continent",
            self.toggle_continent_switch,
            self.continents,
            column=0,
            row=3,
        )

        # 4
        # label4 = Label(self.window, text="Month:")
        # label4.grid(column=0, row=4)
        # month = Entry(self.window, width=30)
        # month.grid(column=1, row=4)

        self.month_switch = False
        self.checkboxes["Month"] = self.add_dropdown_list_widget_with_checkbox(
            self.window,
            "Month",
            self.toggle_month_switch,
            self.months,
            column=0,
            row=4,
        )

        # 5
        # label5 = Label(self.window, text="From: ")
        #         # label5.grid(column=0, row=5)
        #         # from_date = Entry(self.window, width=30)
        #         # from_date.grid(column=1, row=5)

        self.from_date = self.add_date_picker_widget(self.window, "From", 2020, 1, 1, 0, 5)

        # 5
        # label7 = Label(self.window, text="Till: ")
        # label7.grid(column=0, row=7)
        # till_date = Entry(self.window, width=30)
        # till_date.grid(column=1, row=7)

        self.till_date = self.add_date_picker_widget(self.window, "Till", 2020, 12, 31, 0, 6)

        # 6
        frame = Frame(self.window)
        frame.grid(column=1, row=10)

        self.total = BooleanVar()

        label11 = Label(self.window, text="Sum: ")
        label11.grid(column=0, row=10)
        sumRadioOn = Radiobutton(frame, text="on", value=True, variable=self.total)
        sumRadioOn.grid(column=0, row=0)
        sumRadioOn = Radiobutton(frame, text="off", value=False, variable=self.total)
        sumRadioOn.grid(column=1, row=0)

        #7
        self.checkboxes["Sorting"] = self.add_radio_button(
            self.window,
            "Sorting",
            ["Date", "Deaths", "Cases"],
            self.sorting_var,
            self.sorting_container,
            self.toggle_sort_switch,
            column=0,
            row=11,
            padding=0,
        )

        def process():
            command = self.create_command()

            try:
                outcome = command_parser.process(command)
                top= Toplevel(self.window)
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

        process_button = Button(self.window, text="Process", command=process)
        process_button.grid(column=1, row=15)

        self.window.mainloop()

    def create_command(self):
        self.update_statusbar("Processing")
        country_value = self.comboboxes['Country'].get() if self.country_switch is True else None
        continent_value = self.comboboxes['Continent'].get() if self.continent_switch is True else None
        month_value = self.comboboxes['Month'].get() if self.month_switch is True else None
        from_date_value = self.months[self.from_date.get_date().month - 1] + " " + str(self.from_date.get_date().day)
        till_date_value = self.months[self.till_date.get_date().month - 1] + " " + str(self.till_date.get_date().day)
        sorting_value = self.sorting_var.get().strip() if self.sorting_var is not None else ""

        if self.total.get():
            command_parser.process("Set total on")
        else:
            command_parser.process("Set total off")

        command = ""
        if self.deaths_or_cases.get():
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

        if sorting_value != "":
            command += "sort by "
            command += sorting_value

        return command

    def set_source(self):
        new_source_file = self.create_popup_window("Set source file", "Enter new source file:")
        try:
            command_parser.set_records(new_source_file)
            tkinter.messagebox.showinfo("INFO", "Database textfile was succesfully set!")
        except Exception as e:
            tkinter.messagebox.showinfo("ERROR", e)

    def save_to_file(self):
        command = self.create_command()
        try:
            outcome = command_parser.process(command)
            path = self.create_popup_window("Save to file", "Enter path:")
            with open(path, 'w', encoding='utf-8') as file:
                file.write(outcome)
            messagebox.showinfo("OUTCOME", "SUCCESS - DATA SAVED TO FILE!")
        except Exception as e:
            tkinter.messagebox.showinfo("ERROR", e)

    def clear_input(self):
        if self.country_switch is True:
            self.toggle_country_switch()
        if self.continent_switch is True:
            self.toggle_continent_switch()
        if self.month_switch is True:
            self.toggle_month_switch()
        if self.sort_switch is True:
            self.toggle_sort_switch()
        for x in self.checkboxes_objects:
            x.deselect()

    def quit(self):
        if messagebox.askokcancel("Zakoncz", "Czy jestes pewny ze chcesz zakonczyc?"):
            self.window.destroy()

    def create_toolbar(self):
        self.toolbar_images = [] #muszą być pamiętane stale
        self.toolbar = Frame(self.window)
        for image, command in (
            ("images/editdelete.gif", self.clear_input),
            ("images/editadd.gif", self.set_source),
            ("images/filesave.gif", self.save_to_file)):
            image = os.path.join(os.path.dirname(__file__), image)
            try:
                image = tkinter.PhotoImage(file=image)
                self.toolbar_images.append(image)
                button = tkinter.Button(self.toolbar, image=image,
                command=command)
                button.grid(row=0, column=len(self.toolbar_images) -1) #KOLEJNE ELEMENTY
            except tkinter.TclError as err:
                print(err) # gdy kłopoty z odczytaniem pliku
        self.toolbar.grid(row=0, column=0, columnspan=2, sticky=tkinter.NSEW)

    def create_menu(self):
        self.menubar = Menu(self.window)
        self.window["menu"] = self.menubar
        file_menu = Menu(self.menubar)
        for label, command, shortcut_text, shortcut in (
                ("Set source file", self.set_source, "Ctrl+N", "<Control-n>"),
                (None, None, None, None),
                ("Quit", self.quit, "Ctrl+Q", "<Control-q>")):
            if label is None:
                file_menu.add_separator()
            else:
                file_menu.add_command(label=label, underline=0,
                                     command=command, accelerator=shortcut_text)
                self.window.bind(shortcut, command)
        self.menubar.add_cascade(label="File", menu=file_menu, underline=0)
        pass

    def add_dropdown_list_widget_with_checkbox(
            self, parent, title, command, values, column=0, row=0
    ):
        temp_var = IntVar()
        checkbutton = Checkbutton(
            parent, text=title, command=command, variable=temp_var
        )
        checkbutton.grid(column=column, row=row, sticky="w")
        self.checkboxes_objects.append(checkbutton)
        current_var = StringVar()
        combobox = ttk.Combobox(parent, textvariable=current_var)
        combobox["values"] = values
        combobox["state"] = "disabled"
        combobox.grid(column=column + 1, row=row)
        self.comboboxes[title] = combobox
        return temp_var

    def toggle_country_switch(self):
        self.country_switch = not self.country_switch
        if "Country" in self.comboboxes:
            self.comboboxes["Country"]["state"] = (
                "readonly" if self.country_switch else "disabled"
            )

    def toggle_continent_switch(self):
        self.continent_switch = not self.continent_switch
        if "Continent" in self.comboboxes:
            self.comboboxes["Continent"]["state"] = (
                "readonly" if self.continent_switch else "disabled"
            )

    def toggle_month_switch(self):
        self.month_switch = not self.month_switch
        if "Month" in self.comboboxes:
            self.comboboxes["Month"]["state"] = (
                "readonly" if self.month_switch else "disabled"
            )

    def toggle_sort_switch(self):
        self.sort_switch = not self.sort_switch
        for sorting_opt in self.sorting_container:
            sorting_opt["state"] = "!disabled" if self.sort_switch else "disabled"

    def add_date_picker_widget(self, parent, title, year, month, day, column=0, row=0):
        labelText = StringVar()
        labelText.set(title)
        label = Label(parent, textvariable=labelText, height=1)
        label.grid(column=column, row=row, sticky="w")
        cal = DateEntry(parent, width=10, bg="darkblue", fg="white", year=year, month=month, day=day)
        cal.grid(column=column + 1, row=row)

        return cal

    def add_radio_button(
            self,
            parent,
            label,
            options,
            var,
            storage,
            command,
            column=0,
            row=0,
            padding=0,
            sticky="w",
    ):
        temp_var = IntVar()
        checkbox = Checkbutton(
            parent, text=label, command=command, variable=temp_var
        )
        checkbox.grid(column=column, row=row, sticky=sticky)
        self.checkboxes_objects.append(checkbox)
        column += 1
        for i in range(0, len(options)):
            button = ttk.Radiobutton(
                parent, text=options[i], variable=var, value=options[i]
            )
            button.grid(column=column, row=row + i, sticky=sticky)
            button["state"] = "disabled"
            button["padding"] = padding
            storage.append(button)

        return temp_var

    def create_popup_window(self, title, prompt):
        return simpledialog.askstring(title=title, prompt=(prompt + "\t\t\t\t"))

    def add_status_bar(self, text):
        self.statusbar = Label(self.window, text=text, anchor=W)
        self.statusbar.after(5000, self.clear_status_bar)
        self.statusbar.grid(row=16, column=0, columnspan=2, sticky=EW)
        pass

    def clear_status_bar(self):
        self.statusbar["text"] = ""

    def update_statusbar(self, text):
        self.statusbar.config(text=text)
        self.statusbar.after(5000, self.clear_status_bar)