#Importing the modules
import tkinter
import tkinter.ttk as ttk
from tkinter import *
import sqlite3
import tkinter.messagebox as tkMessageBox


root = Tk()
root.title("Contact Management System")
root.geometry("780x600+0+0")
root.config(bg="light gray")


# Variables required for storing the values
f_name = StringVar()
l_name = StringVar()
home_address = StringVar()
gender = StringVar()
phone_number = StringVar()


#Function for resetting the values
def Reset():
    f_name.set("")
    l_name.set("")
    gender.set("")
    home_address.set("")
    phone_number.set("")


# For creating the database and the table
def Database():
    connectn = sqlite3.connect("contactdata1.db")
    cursor = connectn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `contactinformation` (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, first_name TEXT, last_name TEXT, gender TEXT, home_address TEXT, phone_number TEXT)")
    cursor.execute("SELECT * FROM `contactinformation` ORDER BY `last_name` ASC")
    fetchinfo = cursor.fetchall()
    for data in fetchinfo:
        tree.insert('', 'end', values=(data))
    cursor.close()
    connectn.close()

#Function for exiting the system
def Exit():
    O = tkinter.messagebox.askyesno("Contact Management System", "Do you want to exit the system")
    if O > 0:
        root.destroy()
    return

#Insert query for inserting the value in database Table
def Submit():
    if f_name.get() == "" or l_name.get() == "" or gender.get() == "" or home_address.get() == "" or phone_number.get() == "":
        msgg = tkMessageBox.showwarning('', 'Please Complete All the Fields', icon="warning")
    else:
        tree.delete(*tree.get_children())
    connectn = sqlite3.connect("contactdata1.db")
    cursor = connectn.cursor()

    cursor.execute("INSERT INTO `contactinformation` (first_name, last_name, gender, home_address, phone_number ) VALUES(?, ?, ?, ?, ?)", (str(f_name.get()), str(l_name.get()), str(gender.get()), str(home_address.get()), int(phone_number.get())))

    connectn.commit()
    cursor.execute("SELECT * FROM `contactinformation` ORDER BY `last_name` ASC")
    fetchinfo = cursor.fetchall()

    for data in fetchinfo:
        tree.insert('', 'end', values=(data))
    cursor.close()
    connectn.close()
    f_name.set("")
    l_name.set("")
    gender.set("")
    home_address.set("")
    phone_number.set("")


#Update Query for updating the table in the database
def Update():
    if gender.get() == "":
        msgg = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:
        tree.delete(*tree.get_children())
    connectn = sqlite3.connect("contactdata1.db")
    cursor = connectn.cursor()
    cursor.execute("UPDATE `contactinformation` SET `first_name` = ?, `last_name` = ?, `gender` =?, `home_address` = ?, `phone_number` = ? WHERE `id` = ?",
    (str(f_name.get()), str(l_name.get()), str(gender.get()), str(home_address.get()),
    str(phone_number.get()), int(id)))
    connectn.commit()
    cursor.execute("SELECT * FROM `contactinformation` ORDER BY `last_name` ASC")
    fetchinfo = cursor.fetchall()
    for data in fetchinfo:
        tree.insert('', 'end', values=(data))
    gender1 = gender.get()
    if not gender1:
        tkMessageBox.showerror("Please select the gender")

    cursor.close()
    connectn.close()

    f_name.set("")
    l_name.set("")
    gender.set("")
    home_address.set("")
    phone_number.set("")


#Module for the update contact form window
def UpdateContact(event):
    global id, UpdateWindow
    curItem = tree.focus()
    contents = (tree.item(curItem))
    item = contents['values']
    id = item[0]
    f_name.set("")
    l_name.set("")
    gender.set("")
    home_address.set("")
    phone_number.set("")


    f_name.set(item[1])
    l_name.set(item[2])
   
    home_address.set(item[4])
    phone_number.set(item[5])


    UpdateWindow = Toplevel()
    UpdateWindow.title("Contact Information")
    UpdateWindow.geometry("500x520+0+0")
    UpdateWindow.resizable(0, 0)
    if 'Opennewwindow' in globals():
        Opennewwindow.destroy()

    # FRAMES
    #module is for the frame, labels, text entry, and button for update contact form window
    FormTitle = Frame(UpdateWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(UpdateWindow)
    ContactForm.pack(side=TOP, pady=10)
    RadioGroup = Frame(ContactForm)
    Male = Radiobutton(RadioGroup, text="Male", variable=gender, value="Male", font=('arial', 14)).pack(side=LEFT)
    Female = Radiobutton(RadioGroup, text="Female", variable=gender, value="Female", font=('arial', 14)).pack(side=LEFT)

# LABELS
    label_title = Label(FormTitle, text="Update the Contact Information", font=('Arial', 17), bg="light yellow", width=400)
    label_title.pack(fill=X)
    label_FirstName = Label(ContactForm, text="First Name", font=('Calibri', 14), bd=5)
    label_FirstName.grid(row=0, sticky=W)

    label_LastName = Label(ContactForm, text="Last Name", font=('Calibri', 14), bd=5)
    label_LastName.grid(row=1, sticky=W)

    label_Gender = Label(ContactForm, text="Gender", font=('Calibri', 14), bd=5)
    label_Gender.grid(row=2, sticky=W)

    label_HomeAddress = Label(ContactForm, text=" Home Address", font=('Calibri', 14), bd=5)
    label_HomeAddress.grid(row=3, sticky=W)

    label_PhoneNumber = Label(ContactForm, text="Phone Number", font=('Calibri', 14), bd=5)
    label_PhoneNumber.grid(row=4, sticky=W)



# TEXT ENTRY
    FirstName = Entry(ContactForm, textvariable=f_name, font=('Calibri', 14, 'bold'),bd=2, width=20, justify='left')
    FirstName.grid(row=0, column=1)

    LastName = Entry(ContactForm, textvariable=l_name, font=('Calibri', 14, 'bold'), bd=2, width=20, justify='left')
    LastName.grid(row=1, column=1)

    RadioGroup.grid(row=2, column=1)

    HomeAddress = Entry(ContactForm, textvariable=home_address, font=('Calibri', 14, 'bold'), bd=2, width=20,
    justify='left')
    HomeAddress.grid(row=3, column=1)

    PhoneNumber = Entry(ContactForm, textvariable=phone_number, font=('Calibri', 14, 'bold'), bd=2, width=20,
    justify='left')
    PhoneNumber.grid(row=4, column=1)

#  Buttons
    ButtonUpdatContact = Button(ContactForm, text='Update', bd=2, font=('Calibri', 14, 'bold'), fg="black",
    bg="light gray", command=Update)
    ButtonUpdatContact.grid(row=8, columnspan=2, pady=10)


#Delete query for deleting the value
def Delete():
    if not tree.selection():
        msgg = tkMessageBox.showwarning('', 'Please Select the data!', icon="warning")
    else:
        msgg = tkMessageBox.askquestion('', 'Are You Sure You Want To Delete', icon="warning")
    if msgg == 'yes':
        curItem = tree.focus()
        contents = (tree.item(curItem))
        item = contents['values']
        tree.delete(curItem)
    connectn = sqlite3.connect("contactdata.db")
    cursor = connectn.cursor()
    cursor.execute("DELETE FROM `contactinformation` WHERE `id` = %d" % item[0])
    connectn.commit()
    cursor.close()
    connectn.close()

#For creating the frame, labels, text entry, and button for add new contact form window
def MyNewContact():
    global opennewwindow
    f_name.set("")
    l_name.set("")
    gender.set("")
    home_address.set("")
    phone_number.set("")

    Opennewwindow = Toplevel()
    Opennewwindow.title("Contact Details")
    Opennewwindow.resizable(0, 0)
    Opennewwindow.geometry("500x500+0+0")
    if 'UpdateWindow' in globals():
        UpdateWindow.destroy()

#############Frames####################
    FormTitle = Frame(Opennewwindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(Opennewwindow)
    ContactForm.pack(side=TOP, pady=10)
    RadioGroup = Frame(ContactForm)
    Male = Radiobutton(RadioGroup, text="Male", variable=gender, value="Male", font=('Calibri', 14)).pack(side=LEFT)
    Female = Radiobutton(RadioGroup, text="Female", variable=gender, value="Female", font=('Calibri', 14)).pack(side=LEFT)
    # ===================LABELS==============================
    label_title = Label(FormTitle, text="Adding New Contacts", bd=12,  fg="black", bg="light blue",
    font=("Calibri", 15, "bold"), pady=2)
    label_title.pack(fill=X)
    label_FirstName = Label(ContactForm, text="First Name", font=('Calibri', 14), bd=5)
    label_FirstName.grid(row=0, sticky=W)

    label_LastName = Label(ContactForm, text="Last Name", font=('Calibri', 14), bd=5)
    label_LastName.grid(row=1, sticky=W)

    label_Gender = Label(ContactForm, text="Gender", font=('Calibri', 14), bd=5)
    label_Gender.grid(row=2, sticky=W)

    label_HomeAddress = Label(ContactForm, text="Home Address", font=('Calibri', 14), bd=5)
    label_HomeAddress.grid(row=3, sticky=W)

    label_PhoneNumber = Label(ContactForm, text="Phone Number", font=('Calibri', 14), bd=5)
    label_PhoneNumber.grid(row=4, sticky=W)



# ===================ENTRY===============================
    FirstName = Entry(ContactForm, textvariable=f_name, font=('Calibri', 14, 'bold'), bd=3, width=20, justify='left')
    FirstName.grid(row=0, column=1)

    LastName = Entry(ContactForm, textvariable=l_name, font=('Calibri', 14, 'bold'), bd=3, width=20, justify='left')
    LastName.grid(row=1, column=1)

    RadioGroup.grid(row=2, column=1)

    HomeAddress = Entry(ContactForm, textvariable=home_address, font=('Calibri', 14, 'bold'), bd=3, width=20, justify='left')
    HomeAddress.grid(row=3, column=1)

    PhoneNumber = Entry(ContactForm, textvariable=phone_number, font=('Calibri', 14, 'bold'), bd=3, width=20, justify='left')
    PhoneNumber.grid(row=4, column=1)


# ==================BUTTONS==============================
    ButtonAddContact = Button(ContactForm, text='Please Save', bd=5, font=('Calibri', 12, 'bold'), fg="black",
    bg="#ADFF2F", command=Submit)
    ButtonAddContact.grid(row=7, columnspan=2, pady=10)

#module for whole frame window, labels and button of contact management system
# ============================FRAMES======================================
Top = Frame(root, width=600, bd=1)
Top.pack(side=TOP)
M = Frame(root, width=650, bg="light gray")
M.pack(side=BOTTOM)
F = Frame(width=7, height=8, bd=10, bg="light gray")
F.pack(side=BOTTOM)
MR = Frame(M, width=100)#Right Middle frame
MR.pack(side=RIGHT, pady=10)
TableMargin = Frame(root, width=500)
TableMargin.pack(side=TOP)

# LABELS
label_title = Label(Top, text="Contact System", bd=7, relief=GROOVE, fg="Black", bg="#FFEC8B",
font=("Calibri", 25, "bold"), pady=3)
label_title.pack(fill=X)


# BUTTONS
Add_Button = Button(F, text='Add New Contact', font=('Calibri',17, 'bold'), fg="black",
bg="light blue", command=MyNewContact).grid(row=0, column=0, ipadx=20, padx=30)

Delete_Button = Button(F, text='Delete The Contact', font=('Calibri', 17, 'bold'), command=Delete,
fg="black", bg="light blue").grid(row=0, column=1, ipadx=20)

Exit_Button = Button(F, text='Exit System', font=('Calibri', 17, 'bold'), command=Exit,
fg="black", bg="light blue").grid(row=0, column=2, ipadx=20, padx=30)

#creating a tables in contact management system
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("Id", "First Name", "Last Name", "Gender", "Home Address", "Phone Number"),
height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)

tree.heading('Id', text="Id", anchor=W)
tree.heading('First Name', text="First Name" ,anchor=W)
tree.heading('Last Name', text="Last Name", anchor=W)
tree.heading('Gender', text="Gender", anchor=W)
tree.heading('Home Address', text="Home Address", anchor=W)
tree.heading('Phone Number', text="phone Number", anchor=W)

tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=0)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=90)
tree.column('#5', stretch=NO, minwidth=0, width=80)

tree.pack()
tree.bind('<Double-Button-1>', UpdateContact)

# ============================INITIALIZATION==============================
if __name__ == '__main__':
    Database()
root.mainloop()