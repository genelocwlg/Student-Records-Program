from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
import json
import os

#--jsonfunctions
def ensure_json_file():
    FILE_NAME = "students.json"
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            json.dump([], f)

def load_from_json():
    ensure_json_file()
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)

def save_to_json():
    data = []
    for row in table.get_children():
        data.append(table.item(row)["values"])

    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

#--main
def function(function_name):
    if function_name == "add":
        if (name_entry.get() and age_entry.get() and  gender_entry.get() and religion_entry.get() and citizenship_entry.get() and
            birthdate_entry.get() and birthplace_entry.get() and homeadress_entry.get() and yearlevel_Entry.get() and schoolid_Entry.get()):
            table.insert(
                parent = "",
                index = 'end', 
                iid = len(table.get_children()) + 1, 
                values = (
                    yearlevel_Entry.get(),
                    name_entry.get(), 
                    age_entry.get(), 
                    gender_entry.get(), 
                    religion_entry.get(),
                    citizenship_entry.get(),
                    birthdate_entry.get(),
                    birthplace_entry.get(),
                    homeadress_entry.get(),
                    schoolid_Entry.get()))
            save_to_json()
            
        else:
            messagebox.showwarning("Warning: Some Fields are not yet answered or blank!", "All the fields are required to be answered")
    elif function_name == "delete_all":
        if len(table.get_children()) == 0:
            messagebox.showinfo("Unable to delete", "There are no records in the table")
        else:
            answer = messagebox.askyesno("Clear Table", "Are you sure you want to delete all of the records in the table?")
            if answer:
                for record in table.get_children():
                    table.delete(record)
                save_to_json()
    elif function_name == "delete_one":
        if len(table.selection()) == 0:
            messagebox.showerror("Error: Unable to delete", "Nothing was selected")
        else:
            answer = messagebox.askyesno("Delete Record", "Are you sure you want to delete this record?")
            if answer:
                table.delete(table.selection())
                save_to_json()
    elif function_name == "edit":
        if len(table.selection()) == 0:
            messagebox.showerror("Error: Unable to edit", "Nothing was selected")
        else:
            if(name_entry.get() and age_entry.get() and  gender_entry.get() and religion_entry.get() and citizenship_entry.get() and
            birthdate_entry.get() and birthplace_entry.get() and homeadress_entry.get() and yearlevel_Entry.get() and schoolid_Entry.get()):
                table.item(table.selection(),
                    values = (
                        yearlevel_Entry.get(),
                        name_entry.get(), 
                        age_entry.get(), 
                        gender_entry.get(), 
                        religion_entry.get(),
                        citizenship_entry.get(),
                        birthdate_entry.get(),
                        birthplace_entry.get(),
                        homeadress_entry.get(),
                        schoolid_Entry.get()))
                save_to_json()
            else:
                messagebox.showwarning("Warning: Some Fields are not yet answered or blank!", "All the fields are required to be answered")
              
def on_record_select(event):
    selected = table.selection()
    if not selected:
        return
    record = table.item(selected[0])["values"]
    #--clear
    name_entry.delete(0, END)
    age_entry.delete(0, END)
    gender_entry.delete(0, END)
    religion_entry.delete(0, END)
    citizenship_entry.delete(0, END)
    birthdate_entry.delete(0, END)
    birthplace_entry.delete(0, END)
    homeadress_entry.delete(0, END)
    yearlevel_Entry.delete(0, END)
    schoolid_Entry.delete(0, END)

    #--insert
    yearlevel_Entry.insert(0, record[0])
    name_entry.insert(0, record[1])
    age_entry.insert(0, record[2])
    gender_entry.insert(0, record[3])
    religion_entry.insert(0, record[4])
    citizenship_entry.insert(0, record[5])
    birthdate_entry.insert(0, record[6])
    birthplace_entry.insert(0, record[7])
    homeadress_entry.insert(0, record[8])
    schoolid_Entry.insert(0, record[9])
#--main window
main = Tk()
main.geometry("1100x635")
main.title("Student Database program")
main.resizable(False, False)

#--widets
main_header = Label(main, text = "Student Records", width = 83, height = 2, font = "arial 17", relief = "groove").place(x = 10, y = 0)
tabs = Notebook(main, width = 1080, height = 530)
Students_tab = Frame(main, bg= "white")
tabs.add(Students_tab, text = "Student's Personal Data")
name_label = Label(Students_tab, text = "Name", font = "Arial 13", bg = "white").place(x = 10, y = 10)
age_label = Label(Students_tab, text = "Age", font = "Arial 13", bg = "white").place(x = 10, y = 40)
gender_label = Label(Students_tab, text = "Gender", font = "Arial 13", bg = "white").place(x = 150, y = 40)
religion_label = Label(Students_tab, text = "Religion", font = "Arial 13", bg = "white").place(x = 10, y = 70)
citizenship_label = Label(Students_tab, text = "Citizenship", font = "Arial 13", bg = "white").place(x = 10, y = 100)
birthdate_label = Label(Students_tab, text = "Birthdate", font = "Arial 13", bg = "white").place(x = 10, y = 130)
birthplace_label = Label(Students_tab, text = "Birth Place", font = "Arial 13", bg = "white").place(x = 10, y = 160)
homeadress_label = Label(Students_tab, text = "Home Address", font = "Arial 13", bg = "white").place(x = 10, y = 190)
yearlevel_label = Label(Students_tab, text = "Year Level", font  = "Arial 13", bg = "white").place(x = 480, y = 10)
schoolid_label = Label(Students_tab, text = "School ID", font  = "Arial 13", bg = "white").place(x = 480, y = 40)
name_entry = Entry(Students_tab, font = "Arial 12", bg = "white", width = 40)
name_entry.place(x = 80, y = 10)
age_entry = Entry(Students_tab, font = "Arial 12", bg = "white", width = 5)
age_entry.place(x = 60, y = 40)
gender_entry = Entry(Students_tab, font = "Arial 12", bg = "white",width = 10)
gender_entry.place(x = 230, y = 40)
religion_entry = Entry(Students_tab, font = "Arial 12", bg = "white")
religion_entry.place(x = 100, y = 70)
citizenship_entry = Entry(Students_tab, font = "Arial 12", bg = "white")
citizenship_entry.place(x = 125, y = 100)
birthdate_entry =Entry(Students_tab, font = "Arial 12", bg = "white", width = 10)
birthdate_entry.place(x = 110, y = 130)
birthplace_entry =Entry(Students_tab, font = "Arial 12", bg = "white", width = 40)
birthplace_entry.place(x = 110, y =160 )
homeadress_entry =Entry(Students_tab, font = "Arial 12", bg = "white", width = 40)
homeadress_entry.place(x = 130, y =190 )
yearlevel_Entry = Entry(Students_tab, font = "Arial 13", bg = "white")
yearlevel_Entry.place(x = 580, y = 10)
schoolid_Entry = Entry(Students_tab, font = "Arial 13", bg = "white", width = 15)
schoolid_Entry.place(x = 580, y = 40)
add_button = Button(Students_tab, text = "Add Record", command = lambda:function("add"))
add_button.place(x = 160, y = 480)
remove_one_button = Button(Students_tab, text = "Remove Record", command = lambda:function("delete_one"))
remove_one_button.place(x = 320, y = 480)
remove_all_button = Button(Students_tab, text = "Remove all Records", command = lambda:function("delete_all"))
remove_all_button.place(x = 480, y = 480)
edit_button = Button(Students_tab, text = "Edit Record", command = lambda:function("edit"))
edit_button.place(x =640, y = 480)

#--record table
table = Treeview(Students_tab)
table['columns'] = ('Yearlevel', 'Name', 'Age', 'Gender', 'Religion','Citizenship', 'Birthdate','Birthplace', 'Homeaddress', 'Schoolid')
table.column("#0", width = 0, minwidth = 0)
table.column("Yearlevel", anchor = "center", width = 70, minwidth =70)
table.column("Name", anchor = "center", width = 140, minwidth = 140)
table.column("Age", anchor = "center", width = 70, minwidth = 70)
table.column("Gender", anchor = "center", width = 90, minwidth =90)
table.column("Religion", anchor = "center", width = 90, minwidth =90)
table.column("Citizenship", anchor = "center", width = 90, minwidth =90)
table.column("Birthdate", anchor = "center", width = 90, minwidth =90)
table.column("Birthplace", anchor = "center", width = 155, minwidth = 155)
table.column("Homeaddress", anchor = "center", width = 155, minwidth = 155)
table.column("Schoolid", anchor = "center", width = 90, minwidth = 90)
table.heading("Yearlevel", text = "Year Level")
table.heading("#0", text = "Label")
table.heading("Name", text = "Name")
table.heading("Age", text = "Age")
table.heading("Gender", text = "Gender")
table.heading("Religion", text = "Religion")
table.heading("Citizenship", text = "Citizenship")
table.heading("Birthdate", text = "Birth Date")
table.heading("Birthplace", text = "Birth Place")
table.heading("Homeaddress", text = "Home Address")
table.heading("Schoolid", text = "School ID")
table.place(x = 20, y = 230)
tabs.place(x = 10, y= 70)
table.bind("<<TreeviewSelect>>", on_record_select)

#--load current data
for record in load_from_json():
    table.insert("", "end", values=record)
main.mainloop()

#made by geneloclwg
