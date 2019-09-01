from tkinter import messagebox
from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk,Image
import pymysql

db=pymysql.connect("localhost","root","","gym")
cursor=db.cursor()

top=Tk()
top.title("Gym management")
top.geometry("1366x768")
top.configure(bg="black")

#home page
def home():

    def reset():
        entry1.delete(0,END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)


    def register():
        if entry1.get() and entry2.get() and entry3.get() and entry4.get() != "":
            try:
                name = entry1.get()
                email = entry2.get()
                mobile = entry4.get()
                password = entry3.get()
                sql = "insert into user(name,email,password,mobile)values('%s','%s','%s','%s')" % (name, email,password,mobile)
                cursor.execute(sql)
            except:
                messagebox.showinfo('Exception', "Enter the correct details")
        else:
            messagebox.showerror('Error', 'Fill all the Entries')
        db.commit()
        reset()
    tophome = Toplevel(top)
    tophome.geometry("1366x768")
    tophome.configure(bg="black")
    label = Label(tophome, text="FITNESS CENTER ", font=('Algerian', 30), fg="white", bg="black")
    label.place(x=500, y=30)
    label = Label(tophome, text="New User Registration", font=("Georgia", 25), bg="black", fg="orange")
    label.place(x=50, y=70)
    label = Label(tophome, text="Name ", font=("arial", 25), bg="black", fg="white")
    label.place(x=50, y=150)
    entry1 = Entry(tophome, font=("arial", 20), width=40)
    entry1.place(x=200, y=160)
    label = Label(tophome, text="Email ", font=("arial", 25), bg="black", fg="white")
    label.place(x=50, y=220)
    entry2 = Entry(tophome, font=("arial", 20), width=40)
    entry2.place(x=200, y=230)
    label = Label(tophome, text="Password", font=("arial", 25), bg="black", fg="white")
    label.place(x=50, y=290)
    entry3 = Entry(tophome, font=("arial", 20), width=40)
    entry3.place(x=200, y=300)
    label = Label(tophome, text="Mobile no", font=("arial", 25), bg="black", fg="white")
    label.place(x=50, y=360)
    entry4 = Entry(tophome, font=("arial", 20), width=40)
    entry4.place(x=200, y=370)
    btnhome1 = Button(tophome, text="REGISTER", bg="orange", fg="white", font=("arial", 25),command=register)
    btnhome1.place(x=200, y=430)
    btnhome2 = Button(tophome, text="EXIT", bg="orange", fg="white", font=("arial", 25),command=tophome.destroy)
    btnhome2.place(x=450, y=430)
    pathb = r"D:\girl.jpg"
    imgb = ImageTk.PhotoImage(Image.open(pathb))
    planeb = Label(tophome, image=imgb)
    planeb.place(x=940, y=200)
    pathc = r"D:\may.jpg"
    imgc = ImageTk.PhotoImage(Image.open(pathc))
    planec = Label(tophome, image=imgc)
    planec.place(x=940, y=510)
    planec.place_configure(height=150)
    pathd = r"D:\wall.jpg"
    imgd = ImageTk.PhotoImage(Image.open(pathd))
    planed = Label(tophome, image=imgd)
    planed.place(x=50, y=510)
    pathe = r"D:\wallpaper.jpg"
    imge= ImageTk.PhotoImage(Image.open(pathe))
    planee = Label(tophome, image=imge)
    planee.place(x=480, y=510)
    tophome.mainloop()

#About us page
def aboutus():
    topabout=Toplevel(top)
    topabout.geometry("1366x768")
    topabout.configure(bg="black")
    path2 = r"D:\image5.jpg"
    img2 = ImageTk.PhotoImage(Image.open(path2))
    plane2 = Label(topabout, image=img2)
    plane2.place(x=820, y=160)
    plane2.place_configure(width=450, height=290)
    label = Label(topabout, text="FITNESS CENTER ", font=('Algerian', 30), fg="white", bg="black")
    label.place(x=500, y=30)
    label1= Label(topabout, text="ABOUT US", font=("arial", 27), bg="black", fg="green")
    label1.place(x=80, y=90)
    text = Text(topabout, bg="black", fg="white", font=("Georgia", 20))
    text.place(x=30, y=160)
    text.insert("1.0","  Every person in the world would like to have a perfect body. In order to have a healthy and a strong body, people would need to consider going to a gym to work out. What do such people expect of a gym? Certainly, patrons would expect a wide selection of equipment available in a gym. Patrons would enjoy a well-educated staff who knows everything people want to know about working out. The Bally Total Fitness, located on the Boulevard, is a perfect match for that. Patrons will definitely enjoy working out at the Bally Total Fitness. What kind of environment would patrons expect? Patrons will find the Bally Total Fitness clean and well organized.")
    text.place_configure(width=750, height=380)
    btnhome = Button(topabout, text="BACK", bg="black", fg="red", font=("arial", 16),command=topabout.destroy)
    btnhome.place(x=300, y=570)
    btnhome.place_configure(width=200, height=50)
    topabout.mainloop()

#contact us page
def contactus():

    def reset():
        entry1.delete(0,END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete("0.0", END)

    def submit():
        if entry1.get() and entry2.get() and entry3.get() and entry4.get("0.0",END)!="":
            try:
                name=entry1.get()
                email=entry2.get()
                mobile=entry3.get()
                message=entry4.get("0.0",END)
                sql="insert into contact(name,email,mobile,message)values('%s','%s','%s','%s')"%(name,email,mobile,message)
                cursor.execute(sql)
            except:
                messagebox.showinfo('Exception', "Enter the correct details")
        else:
            messagebox.showerror('Error', 'Fill all the Entries')
        db.commit()
        reset()
    topcontact=Toplevel(top)
    topcontact.geometry("1366x768")
    topcontact.configure(bg="black")
    label = Label(topcontact, text="FITNESS CENTER ", font=('Algerian', 30), fg="white", bg="black")
    label.place(x=500, y=30)
    label1 = Label(topcontact, text="CONTACT US", font=("arial", 27), bg="black", fg="green")
    label1.place(x=80, y=90)
    label = Label(topcontact, text="Name", font=("arial", 25), bg="black", fg="white")
    label.place(x=80, y=160)
    entry1=Entry(topcontact,font=("arial",20),width=40)
    entry1.place(x=250,y=160)
    label = Label(topcontact, text="Email", font=("arial", 25), bg="black", fg="white")
    label.place(x=80, y=240)
    entry2 = Entry(topcontact, font=("arial", 20),width=40)
    entry2.place(x=250, y=240)
    label = Label(topcontact, text="Mobile no", font=("arial", 25), bg="black", fg="white")
    label.place(x=80, y=320)
    entry3 = Entry(topcontact, font=("arial", 20),width=40)
    entry3.place(x=250, y=320)
    label = Label(topcontact, text="Message", font=("arial", 25), bg="black", fg="white")
    label.place(x=80, y=400)
    entry4 = Text(topcontact, font=("arial", 20), width=40,height=4)
    entry4.place(x=250, y=400)
    btnhome1 = Button(topcontact, text="Submit", bg="black", fg="red", font=("arial", 16),command=submit)
    btnhome1.place(x=150, y=600)
    btnhome1.place_configure(width=200, height=50)
    btnhome2= Button(topcontact, text="Reset", bg="black", fg="red", font=("arial", 16),command=reset)
    btnhome2.place(x=360, y=600)
    btnhome2.place_configure(width=200, height=50)
    btnhome = Button(topcontact, text="Back", bg="black", fg="red", font=("arial", 16),command=topcontact.destroy)
    btnhome.place(x=580, y=600)
    btnhome.place_configure(width=200, height=50)
    l=Label(topcontact,text="Where to find us",fg="blue",bg="black",font=(20))
    l.place(x=950,y=160)
    path3 = r"D:\map.jpg"
    img3 = ImageTk.PhotoImage(Image.open(path3))
    plane3 = Label(topcontact, image=img3)
    plane3.place(x=950, y=200)
    l = Label(topcontact, text="Get in touch", fg="blue", bg="black", font=(20))
    l.place(x=950, y=450)
    add = Label(topcontact, text="Address=Scheme 23,Basant Vihar,Alwar", font=('Arial', 12), fg="white", bg="black")
    add.place(x=950, y=500)
    mail = Label(topcontact, text="fitnessalwar@gmail.com", font=('Arial', 12), fg="white", bg="black")
    mail.place(x=950, y=550)
    m = Label(topcontact, text="Mobile No.: 9458465842", font=('Arial', 12), fg="white", bg="black")
    m.place(x=950, y=600)
    topcontact.mainloop()

#login page
def login():

    def reset():
        e1.delete(0,END)
        e2.delete(0,END)

    def log():
        def equip():

            def clearform():
                txt.delete(0, END)
                E6.delete(0, END)
                E3.delete(0, END)
                E4.delete(0, END)
                num.set(0)
                pum.set(0)
            def addequip():
                if num.get() and pum.get() and txt.get() and E3.get() and E4.get() and E6.get() != "":
                    try:
                        ename = txt.get()
                        etype = num.get()
                        weight = E3.get()
                        used = pum.get()
                        rs = int(E4.get())
                        date = E6.get()
                        sql = "insert into equip(ename,etype,weight,used,rs,date)values('%s','%s','%s','%s','%d','%s')" % (ename, etype, weight, used, rs, date)
                        cursor.execute(sql)
                    except:
                        messagebox.showwarning("warning", "Enter correct values")
                else:
                    messagebox.showinfo("value", "Kindly fill all entries")
                db.commit()
                clearform()
            #add equipment page
            eq = Toplevel(own)
            eq.title("Equipments")
            eq.geometry("1366x768")
            eq.configure(bg="black")
            patha = r"D:\img.jpg"
            imga = ImageTk.PhotoImage(Image.open(patha))
            panela = Label(eq,image=imga)
            panela.place(x=1000, y=450)
            lbheader = Label(eq, text="ADD EQUIPMENTS", font=('Algerian', 30), fg="white", bg="black")
            lbheader.place(x=380, y=60)
            label1 = Label(eq, text="Equipment Name :", font=('Arial'), fg="red",bg="black")
            label1.place(x=360, y=130)
            txt = Entry(eq, width=25)
            txt.place(x=550, y=130)
            label2 = Label(eq, text="Equipment type :", font=('Arial'), fg="red",bg="black")
            label2.place(x=360, y=170)
            num = StringVar()
            cb = Combobox(eq, textvariable=num, state="readonly", width=22)
            cb['values'] = ("---SELECT TYPE---", "Automatic", "Manual")
            cb.place(x=550, y=170)
            cb.current(0)
            label3 = Label(eq, text="Weight:", font=('Arial'), fg="red",bg="black")
            label3.place(x=360, y=220)
            E3 = Entry(eq, width=25)
            E3.place(x=550, y=220)
            label4 = Label(eq, text="Rupees :", font=('Arial'), fg="red",bg="black")
            label4.place(x=360, y=270)
            E4 = Entry(eq, width=25)
            E4.place(x=550, y=270)
            label5 = Label(eq, text="Used For :", font=('Arial'), fg="red",bg="black")
            label5.place(x=360, y=320)
            pum = StringVar()
            cb = Combobox(eq, textvariable=pum, state="readonly", width=22)
            cb['values'] = ("---SELECT TYPE---", "Weight lift", "Arm Exercise", "Hip  Exercise")
            cb.place(x=550, y=320)
            cb.current(0)
            label6 = Label(eq, text="Purchase Date :", font=('Arial'), fg="red",bg="black")
            label6.place(x=360, y=370)
            E6 = Entry(eq, width=25)
            E6.place(x=550, y=370)
            b = Button(eq, text="Save", relief=RAISED, fg="red", bg="black", font=(20), command=addequip)
            b.place(x=530, y=460)

            eq.mainloop()

        def editequip():

            def updateequip():
                if num.get() and pum.get() and txt.get() and E3.get() and E4.get() and E6.get() != "":
                    try:
                        ename = txt.get()
                        etype = num.get()
                        weight = E3.get()
                        used = pum.get()
                        rs = int(E4.get())
                        date = E6.get()
                        s = "update equip set etype='%s',weight='%s',used='%s',rs='%d',date='%s' where ename='%s'" % (etype, weight, used, rs, date,ename)
                        q=cursor.execute(s)
                        if q > 0:
                            messagebox.showinfo("value", " Equipment updated successfully")
                        else:
                            messagebox.showwarning("warning", "No Equipment updated")
                    except:
                        messagebox.showwarning("warning", "Enter correct values")
                else:
                    messagebox.showinfo("value", "Kindly fill all entries")
                db.commit()

            def deleteequip():
                if txt.get() != 0:
                    try:
                        ename = txt.get()
                        sql = "delete from equip where ename='%s'" % (ename)
                        q = cursor.execute(sql)
                        if q > 0:
                            messagebox.showinfo("value", " Equipment deleted successfully")
                        else:
                            messagebox.showwarning("warning", "No Equipment deleted")
                    except:
                        messagebox.showwarning("warning", "Enter correct values")
                else:
                    messagebox.showinfo("value", "Kindly fill all entries")
                db.commit()
            #edit equipment page
            eqe = Toplevel(own)
            eqe.title("Euipments")
            eqe.geometry("1366x768")
            eqe.configure(bg="black")
            path8= r"D:\img5.jpg"
            img8 = ImageTk.PhotoImage(Image.open(path8))
            panel8 = Label(eqe, image=img8)
            panel8.place(x=1000,y=450)

            lbheader = Label(eqe, text="EDIT EQUIPMENTS", font=('Algerian', 30), fg="white", bg="black")
            lbheader.place(x=380, y=60)

            label1 = Label(eqe, text="Equipment Name :", font=('Arial'), fg="red",bg="black")
            label1.place(x=360, y=130)

            txt = Entry(eqe, width=25)
            txt.place(x=550, y=130)

            label2 = Label(eqe, text="Equipment type :", font=('Arial'), fg="red",bg="black")
            label2.place(x=360, y=170)

            num = StringVar()
            cb = Combobox(eqe, textvariable=num, state="readonly", width=22)
            cb['values'] = ("---SELECT TYPE---", "Automatic", "Manual")
            cb.place(x=550, y=170)
            cb.current(0)

            label3 = Label(eqe, text="Weight:", font=('Arial'), fg="red",bg="black")
            label3.place(x=360, y=220)

            E3 = Entry(eqe, width=25)
            E3.place(x=550, y=220)

            label4 = Label(eqe, text="Rupees :", font=('Arial'), fg="red",bg="black")
            label4.place(x=360, y=270)

            E4 = Entry(eqe, width=25)
            E4.place(x=550, y=270)

            label5 = Label(eqe, text="Used For :", font=('Arial'), fg="red",bg="black")
            label5.place(x=360, y=320)

            pum = StringVar()
            cb = Combobox(eqe, textvariable=pum, state="readonly", width=22)
            cb['values'] = ("---SELECT TYPE---", "Weight lift", "Arm Exercise", "Hip  Exercise")
            cb.place(x=550, y=320)
            cb.current(0)

            label6 = Label(eqe, text="Purchase Date :", font=('Arial'), fg="red",bg="black")
            label6.place(x=360, y=370)

            E6 = Entry(eqe, width=25)
            E6.place(x=550, y=370)

            b1 = Button(eqe, text="Update", relief=RAISED, fg="red", bg="black", font=(20), command=updateequip)
            b1.place(x=430, y=460)

            b2 = Button(eqe, text="Delete", relief=RAISED, fg="red", bg="black", font=(20), command=deleteequip)
            b2.place(x=520, y=460)

            b1 = Button(eqe, text="Exit", relief=RAISED, fg="red", bg="black", font=(20), command=eqe.destroy)
            b1.place(x=600, y=460)

            eqe.mainloop()

        def addmaster():

            def Enter():
                if nameentry.get() and number.get() and ageentry.get() and num2.get() and salentry.get() and num3.get() and joinentry.get() != "":
                    try:
                        mname = nameentry.get()
                        gender = number.get()
                        age = int(ageentry.get())
                        masterin = num2.get()
                        salary = float(salentry.get())
                        time = num3.get()
                        date = joinentry.get()
                        query = "insert into master(mname,gender,age,masterin,salary,time,date)values('%s','%s','%d','%s','%f','%s','%s')" % (
                        mname, gender, age, masterin, salary, time, date)
                        cursor.execute(query)
                    except:
                        messagebox.showinfo('Exception', "Enter the correct details")
                else:
                    messagebox.showerror('Error', 'Fill all the Entries')
                db.commit()
                clearform()
            def clearform():
                nameentry.delete(0, END)
                salentry.delete(0, END)
                joinentry.delete(0, END)
                ageentry.delete(0, END)
                number.set(0)
                num2.set(0)
                num3.set(0)

            add = Toplevel(own)
            add.title("Master")
            add.geometry("1366x768")
            add.configure(bg="light green")
            path8= r"D:\adduser.jpg"
            img8 = ImageTk.PhotoImage(Image.open(path8))
            panel8 = Label(add, image=img8)
            panel8.place(x=1000, y=450)

            lab = Label(add, text="Add Master", font=('Georgia', 20), width=30, fg="blue",bg="light green")
            lab.place(x=400, y=110)

            namelab = Label(add, text="Name :", width=10,bg="light green")
            namelab.place(x=400, y=190)

            nameentry = Entry(add, text="", width=50)
            nameentry.place(x=500, y=190)

            genderlab = Label(add, text="Gender :", width=10,bg="light green")
            genderlab.place(x=400, y=230)

            number = StringVar()
            cb = Combobox(add, textvariable=number, state="Readonly", width=47)
            cb["values"] = ("--Select Gender---", "Male", "Female")
            cb.place(x=500, y=230)
            cb.current(0)

            agelab = Label(add, text="Age :", width=10,bg="light green")
            agelab.place(x=400, y=270)

            ageentry = Entry(add, text="", width=50)
            ageentry.place(x=500, y=270)

            masterinlab = Label(add, text="Master in :", width=10,bg="light green")
            masterinlab.place(x=400, y=310)

            num2 = StringVar()
            cb2 = Combobox(add, textvariable=num2, state="Readonly", width=47)
            cb2["values"] = ("--Select mastery---", "Lifting", "Weighting", "Fitness", "Training")
            cb2.place(x=500, y=310)
            cb2.current(0)

            salarylab = Label(add, text="Salary :", width=10,bg="light green")
            salarylab.place(x=400, y=350)

            salentry = Entry(add, text="", width=50)
            salentry.place(x=500, y=350)

            Timinglab = Label(add, text="Timing :", width=10,bg="light green")
            Timinglab.place(x=400, y=390)

            num3 = StringVar()
            cb3 = Combobox(add, textvariable=num3, state="Readonly", width=47)
            cb3["values"] = ("--Select schedule---", "9 am - 12 am", "4 pm - 6 pm", "6 pm - 8pm", "8 pm -10 pm", "10 pm - 11 pm")
            cb3.place(x=500, y=390)
            cb3.current(0)

            Joinlab = Label(add, text="Joining :", width=10,bg="light green")
            Joinlab.place(x=400, y=430)

            joinentry = Entry(add, text="", width=50)
            joinentry.place(x=500, y=430)

            save = Button(add, text="Save", command=Enter, fg="red", bg="black", font=(20))
            save.place(x=450, y=470)
            clear = Button(add, text="clear", command=clearform, fg="red", bg="black", font=(20))
            clear.place(x=550, y=470)
            exit1 = Button(add, text="Exit", command=add.destroy, fg="red", bg="black", font=(20))
            exit1.place(x=650, y=470)

            add.mainloop()

        def editmaster():

            def Enter():
                if nameentry1.get() and number1.get() and ageentry1.get() and num5.get() and salentry1.get() and num31.get() and joinentry1.get() != "":
                    try:
                        name1 = nameentry1.get()
                        gender1 = number1.get()
                        age1 = int(ageentry1.get())
                        mastery1 = num5.get()
                        salary1 = float(salentry1.get())
                        timing1 = num31.get()
                        join1 = joinentry1.get()
                        query1 = "update master set gender='%s',age='%d',masterin='%s',salary='%f',time='%s',date='%s' where mname='%s'" % (gender1, age1, mastery1, salary1, timing1, join1,name1)
                        r = cursor.execute(query1)
                        if r > 0:
                            messagebox.showinfo("Success", "Master successfully Updated")
                        else:
                            messagebox.showinfo("Unsuccessful", "Master not Updated successfully")
                    except:
                        messagebox.showinfo("Exception", "Enter the correct details")
                else:
                    messagebox.showerror("Error", "Fill all the Entries")
                db.commit()

            def delete():
                if identry1.get() != "":
                    try:
                        id = int(identry1.get())
                        sql = "Delete from master where aid='%d' " % (id)
                        r = cursor.execute(sql)
                        if r > 0:
                            messagebox.showinfo('success', 'Master successfully deleted')
                        else:
                            messagebox.showinfo('Unsuccessful', 'Master not successfully Deleted')
                    except:
                        messagebox.showinfo('Exception', "Enter the correct details")
                else:
                    messagebox.showerror('Error', 'Fill all the Entries')
                db.commit()

            edit = Toplevel(own)
            edit.title("Master")
            edit.geometry("2160x1080")
            edit.configure(bg="light green")
            path9 = r"D:\add user.jpg"
            img9 = ImageTk.PhotoImage(Image.open(path9))
            panel9 = Label(edit, image=img9)
            panel9.place(x=1000, y=450)

            lab1 = Label(edit, text="Edit Master", font=('Georgia', 20), width=30,bg="light green")
            lab1.place(x=430, y=50)

            idlab1 = Label(edit, text="Master ID :", width=10,bg="light green")
            idlab1.place(x=400, y=150)

            identry1 = Entry(edit, text="", width=50)
            identry1.place(x=500, y=150)

            namelab1 = Label(edit, text="Name :", width=10,bg="light green")
            namelab1.place(x=400, y=190)

            nameentry1 = Entry(edit, text="", width=50)
            nameentry1.place(x=500, y=190)

            genderlab1 = Label(edit, text="Gender :", width=10,bg="light green")
            genderlab1.place(x=400, y=230)

            number1 = StringVar()
            cb1 = Combobox(edit, textvariable=number1, state="Readonly", width=47)
            cb1["values"] = ("--Select Gender---", "Male", "Female")
            cb1.place(x=500, y=230)
            cb1.current(0)

            agelab1 = Label(edit, text="Age :", width=10,bg="light green")
            agelab1.place(x=400, y=270)

            ageentry1 = Entry(edit, text="", width=50)
            ageentry1.place(x=500, y=270)

            masterinlab1 = Label(edit, text="Master in :", width=10,bg="light green")
            masterinlab1.place(x=400, y=310)

            num5 = StringVar()
            cb21 = Combobox(edit, textvariable=num5, state="Readonly", width=47)
            cb21["values"] = ("--Select mastery---", "Lifting", "Weighting", "Fitness", "Training")
            cb21.place(x=500, y=310)
            cb21.current(0)

            salarylab1 = Label(edit, text="Salary :", width=10,bg="light green")
            salarylab1.place(x=400, y=350)

            salentry1 = Entry(edit, text="", width=50)
            salentry1.place(x=500, y=350)

            Timinglab1 = Label(edit, text="Timing :", width=10,bg="light green")
            Timinglab1.place(x=400, y=390)

            num31 = StringVar()
            cb31 = Combobox(edit, textvariable=num31, state="Readonly", width=47)
            cb31["values"] = (
            "--Select schedule---", "9 am - 12 am", "4 pm - 6 pm", "6 pm - 8pm", "8 pm -10 pm", "10 pm - 11 pm")
            cb31.place(x=500, y=390)
            cb31.current(0)

            Joinlab1 = Label(edit, text="Joining :", width=10,bg="light green")
            Joinlab1.place(x=400, y=430)

            joinentry1 = Entry(edit, text="", width=50)
            joinentry1.place(x=500, y=430)

            update = Button(edit, text="Save", command=Enter, fg="red", bg="black", font=(20))
            update.place(x=450, y=470)
            Delete = Button(edit, text="Delete", command=delete, fg="red", bg="black", font=(20))
            Delete.place(x=550, y=470)
            exit1 = Button(edit, text="Exit", command=edit.destroy, fg="red", bg="black", font=(20))
            exit1.place(x=650, y=470)

            edit.mainloop()

        def addmember():

            def reset():
                entry1.delete(0, END)
                entry2.delete(0, END)
                entry3.delete(0, END)
                entry4.delete(0, END)

            def submit():
                if entry1.get() and entry2.get() and entry3.get() and entry4.get() != "":
                    try:
                        name = entry1.get()
                        email = entry2.get()
                        mobile = entry3.get()
                        password = entry4.get()
                        sql = "insert into user(name,email,password,mobile)values('%s','%s','%s','%s')" % (name, email,password,mobile)
                        cursor.execute(sql)
                    except:
                        messagebox.showinfo('Exception', "Enter the correct details")
                else:
                    messagebox.showerror('Error', 'Fill all the Entries')
                db.commit()
                reset()

            adding = Toplevel(own)
            adding.geometry("1366x768")
            adding.configure(bg="black")
            path10= r"D:\img1.jpg"
            img10= ImageTk.PhotoImage(Image.open(path10))
            panel10= Label(adding, image=img10)
            panel10.place(x=950, y=100)
            path11 = r"D:\img2.jpg"
            img11= ImageTk.PhotoImage(Image.open(path11))
            panel11 = Label(adding, image=img11)
            panel11.place(x=950, y=300)
            label1 = Label(adding, text="ADD MEMBER", font=("arial", 27), bg="black", fg="green")
            label1.place(x=430, y=50)
            label = Label(adding, text="Name", font=("arial", 25), bg="black", fg="white")
            label.place(x=80, y=160)
            entry1 = Entry(adding, font=("arial", 20), width=40)
            entry1.place(x=250, y=160)
            label = Label(adding, text="Email", font=("arial", 25), bg="black", fg="white")
            label.place(x=80, y=240)
            entry2 = Entry(adding, font=("arial", 20), width=40)
            entry2.place(x=250, y=240)
            label = Label(adding, text="Mobile no", font=("arial", 25), bg="black", fg="white")
            label.place(x=80, y=320)
            entry3 = Entry(adding, font=("arial", 20), width=40)
            entry3.place(x=250, y=320)
            label = Label(adding, text="Password", font=("arial", 25), bg="black", fg="white")
            label.place(x=80, y=400)
            entry4 = Entry(adding, font=("arial", 20), width=40)
            entry4.place(x=250, y=400)
            btnhome1 = Button(adding, text="Save", bg="black", fg="red", font=("arial", 16), command=submit)
            btnhome1.place(x=150, y=600)
            btnhome1.place_configure(width=200, height=50)
            btnhome2 = Button(adding, text="Reset", bg="black", fg="red", font=("arial", 16), command=reset)
            btnhome2.place(x=360, y=600)
            btnhome2.place_configure(width=200, height=50)
            btnhome = Button(adding, text="Back", bg="black", fg="red", font=("arial", 16),command=adding.destroy)
            btnhome.place(x=580, y=600)
            btnhome.place_configure(width=200, height=50)

            adding.mainloop()

        def editmember():

            def update():
                if entry1.get() and entry2.get() and entry3.get() and entry4.get()!= "":
                    try:
                        name=entry1.get()
                        email=entry2.get()
                        mobile=entry3.get()
                        password=entry4.get()
                        query1 = "update user set email='%s',mobile='%s',password='%s' where name='%s'" % (email,mobile,password,name)
                        r = cursor.execute(query1)
                        if r > 0:
                            messagebox.showinfo("Success", "Member successfully Updated")
                        else:
                            messagebox.showinfo("Unsuccessful", "Member not Updated successfully")
                    except:
                        messagebox.showinfo("Exception", "Enter the correct details")
                else:
                    messagebox.showerror("Error", "Fill all the Entries")
                db.commit()

            def delete():
                if entry1.get()!= "":
                    try:
                        name = entry1.get()
                        sql = "Delete from user where name='%s' " % (name)
                        r = cursor.execute(sql)
                        if r > 0:
                            messagebox.showinfo('success', 'Member successfully deleted')
                        else:
                            messagebox.showinfo('Unsuccessful', 'Member not successfully Deleted')
                    except:
                        messagebox.showinfo('Exception', "Enter the correct details")
                else:
                    messagebox.showerror('Error', 'Fill all the Entries')
                db.commit()

            editing = Toplevel(own)
            editing.geometry("1366x768")
            editing.configure(bg="black")
            path12 = r"D:\may.jpg"
            img12 = ImageTk.PhotoImage(Image.open(path12))
            panel12 = Label(editing , image=img12)
            panel12.place(x=950, y=100)
            path13 = r"D:\girl.jpg"
            img13 = ImageTk.PhotoImage(Image.open(path13))
            panel13 = Label(editing, image=img13)
            panel13.place(x=950, y=300)
            label1 = Label(editing , text="EDIT MEMBER", font=("arial", 27), bg="black", fg="green")
            label1.place(x=430, y=50)
            label = Label(editing , text="Name", font=("arial", 25), bg="black", fg="white")
            label.place(x=80, y=160)
            entry1 = Entry(editing , font=("arial", 20), width=40)
            entry1.place(x=250, y=160)
            label = Label(editing , text="Email", font=("arial", 25), bg="black", fg="white")
            label.place(x=80, y=240)
            entry2 = Entry(editing , font=("arial", 20), width=40)
            entry2.place(x=250, y=240)
            label = Label(editing , text="Mobile no", font=("arial", 25), bg="black", fg="white")
            label.place(x=80, y=320)
            entry3 = Entry(editing , font=("arial", 20), width=40)
            entry3.place(x=250, y=320)
            label = Label(editing , text="Password", font=("arial", 25), bg="black", fg="white")
            label.place(x=80, y=400)
            entry4 = Entry(editing , font=("arial", 20), width=40)
            entry4.place(x=250, y=400)
            btnhome1 = Button(editing , text="Update", bg="black", fg="red", font=("arial", 16), command=update)
            btnhome1.place(x=150, y=600)
            btnhome1.place_configure(width=200, height=50)
            btnhome2 = Button(editing , text="Delete", bg="black", fg="red", font=("arial", 16), command=delete)
            btnhome2.place(x=360, y=600)
            btnhome2.place_configure(width=200, height=50)
            btnhome = Button(editing , text="Back", bg="black", fg="red", font=("arial", 16), command=editing .destroy)
            btnhome.place(x=580, y=600)
            btnhome.place_configure(width=200, height=50)

            editing.mainloop()

        def fees():

            def reset():
                entry1.delete(0, END)
                entry2.delete(0, END)
                entry3.delete(0, END)
                entry4.delete(0, END)
                entry5.delete(0,END)
            def save():
                if entry1.get() and entry2.get() and entry3.get() and entry4.get() and entry5.get() != "":
                    try:
                        name = entry2.get()
                        fee=int(entry4.get())
                        date=entry5.get()
                        sql="update user set fees='%d',date='%s' where name='%s'"%(fee,date,name)
                        cursor.execute(sql)
                    except:
                        messagebox.showinfo('Exception', "Enter the correct details")
                else:
                    messagebox.showerror('Error', 'Fill all the Entries')
                db.commit()
                reset()

            topfees = Toplevel(own)
            topfees.geometry("1366x768")
            topfees.configure(bg="black")
            pathf = r"D:\fees.jpg"
            imgf = ImageTk.PhotoImage(Image.open(pathf))
            panelf = Label(topfees, image=imgf)
            panelf.place(x=1000, y=20)
            label = Label(topfees, text="Add Fees", font=("Georgia", 40), bg="black", fg="orange")
            label.place(x=500, y=50)
            label = Label(topfees, text="User id:", font=("arial", 25), bg="black", fg="white")
            label.place(x=330, y=200)
            entry1 = Entry(topfees, font=("arial", 20), width=40)
            entry1.place(x=520, y=200)
            label = Label(topfees, text="Name:", font=("arial", 25), bg="black", fg="white")
            label.place(x=330, y=300)
            entry2 = Entry(topfees, font=("arial", 20), width=40)
            entry2.place(x=520, y=300)
            label = Label(topfees, text="Mobile no:", font=("arial", 25), bg="black", fg="white")
            label.place(x=330, y=400)
            entry3 = Entry(topfees, font=("arial", 20), width=40)
            entry3.place(x=520, y=400)
            label = Label(topfees, text="Fees:", font=("arial", 25), bg="black", fg="white")
            label.place(x=330, y=500)
            entry4 = Entry(topfees, font=("arial", 20), width=40)
            entry4.place(x=520, y=500)
            label = Label(topfees, text="Paid Date:", font=("arial", 25), bg="black", fg="white")
            label.place(x=330, y=600)
            entry5 = Entry(topfees, font=("arial", 20), width=40)
            entry5.place(x=520, y=600)
            btnhome1 = Button(topfees, text="SAVE", bg="orange", fg="white", font=("arial", 13), width=16,command=save)
            btnhome1.place(x=520, y=650)
            btnhome1 = Button(topfees, text="CLEAR", bg="orange", fg="white", font=("arial", 13), width=16,command=reset)
            btnhome1.place(x=700, y=650)
            btnhome1 = Button(topfees, text="EXIT", bg="orange", fg="white", font=("arial", 13), width=16,command=topfees.destroy)
            btnhome1.place(x=870, y=650)
            topfees.mainloop()

        def report1():
            ownreport = Toplevel(own)
            ownreport.title("MEMBER REPORT")
            ownreport.geometry("1366x768")
            ownreport.configure(bg="black")
            label = Label(ownreport, text="Members report", font=("Georgia", 40), bg="black", fg="orange")
            label.place(x=500, y=50)
            tree = Treeview(ownreport )
            tree["column"] = ("a", "b", "c", "d", "e", "f", "g")
            tree.column("a", width=100)
            tree.column("b", width=100)
            tree.column("c", width=200)
            tree.column("d", width=100)
            tree.column("e", width=200)
            tree.column("f", width=100)
            tree.column("g", width=200)
            tree.heading("a", text="User id")
            tree.heading("b", text="Username")
            tree.heading("c", text="Email Id")
            tree.heading("d", text="Password")
            tree.heading("e", text="Mobile No.")
            tree.heading("f", text="Fees")
            tree.heading("g", text="Paid Date")
            query7 = "select * from user"
            cursor.execute(query7)
            row = cursor.fetchall()
            for i in row:
                a = i[0]
                b = i[1]
                c= i[2]
                d = i[3]
                e = i[4]
                f = i[5]
                g= i[6]
                tree.insert("", 0, values=(a,b,c,d,e,f,g))
            tree.place(x=60,y=150)
            ownreport.mainloop()

        def report2():
            report2 = Toplevel(own)
            report2.title("MASTER REPORT")
            report2.geometry("1366x768")
            report2.configure(bg="black")
            label = Label(report2, text="Master report", font=("Georgia", 40), bg="black", fg="orange")
            label.place(x=500, y=50)
            tree = Treeview(report2)
            tree["column"] = ("a", "b", "c", "d", "e", "f", "g","i")
            tree.column("a", width=100)
            tree.column("b", width=100)
            tree.column("c", width=100)
            tree.column("d", width=100)
            tree.column("e", width=100)
            tree.column("f", width=100)
            tree.column("g", width=100)
            tree.column("i", width=100)
            tree.heading("a", text="Master id")
            tree.heading("b", text="Mastername")
            tree.heading("c", text="Gender")
            tree.heading("d", text="Age")
            tree.heading("e", text="Master In")
            tree.heading("f", text="Salary")
            tree.heading("g", text="Time")
            tree.heading("i", text="Joining date")
            query7 = "select * from master"
            cursor.execute(query7)
            row = cursor.fetchall()
            for i in row:
                a = i[0]
                b = i[1]
                c = i[2]
                d = i[3]
                e = i[4]
                f = i[5]
                g = i[6]
                i=i[7]
                tree.insert("", 0, values=(a, b, c, d, e, f, g,i))
            tree.place(x=90, y=150)
            report2.mainloop()

        def report3():
            report3= Toplevel(own)
            report3.title("EQUIPMENT REPORT")
            report3.geometry("1366x768")
            report3.configure(bg="black")
            label = Label(report3, text="Equipment report", font=("Georgia", 40), bg="black", fg="orange")
            label.place(x=500, y=50)
            tree = Treeview(report3)
            tree["column"] = ("a", "b", "c", "d", "e", "f", "g")
            tree.column("a", width=100)
            tree.column("b", width=100)
            tree.column("c", width=200)
            tree.column("d", width=100)
            tree.column("e", width=200)
            tree.column("f", width=100)
            tree.column("g", width=200)
            tree.heading("a", text="Equipment id")
            tree.heading("b", text="Equipment Name")
            tree.heading("c", text="Equipment Type")
            tree.heading("d", text="Weight")
            tree.heading("e", text="Used For")
            tree.heading("f", text="Ruppes")
            tree.heading("g", text="Joining Date")
            query7 = "select * from equip"
            cursor.execute(query7)
            row = cursor.fetchall()
            for i in row:
                a = i[0]
                b = i[1]
                c = i[2]
                d = i[3]
                e = i[4]
                f = i[5]
                g = i[6]
                tree.insert("", 0, values=(a, b, c, d, e, f, g))
            tree.place(x=60, y=150)
            report3.mainloop()

        def change():

             def clear1():
                 entry11.delete(0,END)
                 entry12.delete(0,END)
                 entry13.delete(0,END)
                 entry14.delete(0,END)

             def save():
                 if entry11.get() and entry12.get() and entry13.get() and entry14.get() and entry13.get() == entry14.get():
                     try:
                         name=entry11.get()
                         password=entry13.get()
                         q="update user set password='%s' where name='%s'"%(password,name)
                         cursor.execute(q)
                         db.commit()
                         clear1()
                     except:
                         messagebox.showinfo('Exception', "Enter the correct details")
                 else:
                     messagebox.showerror('Error', 'Fill all the Entries')

             use = Toplevel(user)
             use.geometry("1366x768")
             use.configure(bg="black")
             pathi= r"D:\doing.jpg"
             imgi = ImageTk.PhotoImage(Image.open(pathi))
             paneli = Label(use, image=imgi)
             paneli.place(x=500, y=470)
             label = Label(use, text="Change Password", font=("arial", 45), bg="black", fg="white")
             label.place(x=400, y=10)
             label = Label(use , text="Name", font=("arial", 25), bg="black", fg="white")
             label.place(x=250, y=100)
             entry11 = Entry(use , font=("arial", 20), width=40)
             entry11.place(x=520, y=100)
             label = Label(use, text="Current Password", font=("arial", 25), bg="black", fg="white")
             label.place(x=250, y=160)
             entry12 = Entry(use , font=("arial", 20), width=40)
             entry12.place(x=520, y=160)
             label = Label(use, text="New Password", font=("arial", 25), bg="black", fg="white")
             label.place(x=250, y=220)
             entry13 = Entry(use , font=("arial", 20), width=40)
             entry13.place(x=520, y=220)
             label = Label(use, text="Confirm Password", font=("arial", 25), bg="black", fg="white")
             label.place(x=250, y=280)
             entry14 = Entry(use , font=("arial", 20), width=40)
             entry14.place(x=520, y=280)

             btnhome1 = Button(use , text="Save", bg="orange", fg="white", font=("arial", 13), width=16,command=save)
             btnhome1.place(x=520, y=340)
             btnhome1 = Button(use , text="Clear", bg="orange", fg="white", font=("arial", 13), width=16,command=clear1)
             btnhome1.place(x=700, y=340)

             btnhome1 = Button(use, text="Exit", bg="orange", fg="white", font=("arial", 13), width=16,command=use.destroy)
             btnhome1.place(x=880, y=340)
             use.mainloop()


        def reciept():
             rec = Toplevel(user)
             rec.title("MEMBER REPORT")
             rec.geometry("1366x768")
             rec.configure(bg="black")
             label = Label(rec, text="User report", font=("Georgia", 40), bg="black", fg="orange")
             label.place(x=500, y=50)
             tree = Treeview( rec)
             tree["column"] = ("a", "b", "c", "d", "e", "f", "g")
             tree.column("a", width=100)
             tree.column("b", width=100)
             tree.column("c", width=200)
             tree.column("d", width=100)
             tree.column("e", width=200)
             tree.column("f", width=100)
             tree.column("g", width=200)
             tree.heading("a", text="User id")
             tree.heading("b", text="Username")
             tree.heading("c", text="Email Id")
             tree.heading("d", text="Password")
             tree.heading("e", text="Mobile No.")
             tree.heading("f", text="Fees")
             tree.heading("g", text="Paid Date")
             name=e1.get()
             password=e2.get()
             query7 = "select * from user where name='%s' and password='%s'"%(name,password)
             cursor.execute(query7)
             row = cursor.fetchall()
             for i in row:
                 a = i[0]
                 b = i[1]
                 c = i[2]
                 d = i[3]
                 e = i[4]
                 f = i[5]
                 g = i[6]
                 tree.insert("", 0, values=(a, b, c, d, e, f, g))
             tree.place(x=60, y=150)
             k=Button(rec,text="Click to print the reciept",fg="red",bg="black", font=("arial", 16))
             k.place(x=550,y=400)
             k.place_configure(width=300, height=40)
             rec.mainloop()

        if e1.get() and e2.get() and num.get()!="":
            try:
                if num.get()=="Owner":
                    oname = str(e1.get())
                    opass = str(e2.get())
                    sql = "select * from owner where oname='%s' and opass='%s'" % (oname, opass)
                    r1 = cursor.execute(sql)
                    if r1>0:
                      #owner page
                      own = Toplevel(toplogin)
                      own.title("OWNER INTERFACE")
                      own.geometry("1366x768")
                      own.configure(bg="black")
                      label = Label(own, text="FITNESS CENTER ", font=('Algerian', 30), fg="white", bg="black")
                      label.place(x=500, y=30)
                      path6 = r"D:\user1.jpg"
                      img6 = ImageTk.PhotoImage(Image.open(path6))
                      panel6 = Label(own, image=img6)
                      panel6.place(x=500, y=250)
                      menubar = Menu(own)
                      eq = Menu(menubar, tearoff=0)
                      eq.add_command(label="Add Equipments",command=equip)
                      eq.add_separator()
                      eq.add_command(label="Edit Equipments",command=editequip)
                      eq.add_separator()
                      own.configure(menu=menubar)
                      menubar.add_cascade(label="Equipments", menu=eq)
                      mas = Menu(menubar, tearoff=0)
                      mas.add_command(label="Add Master",command=addmaster)
                      mas.add_separator()
                      mas.add_command(label="Edit Master",command=editmaster)
                      mas.add_separator()
                      own.configure(menu=menubar)
                      menubar.add_cascade(label="Master", menu=mas)
                      mem = Menu(menubar, tearoff=0)
                      mem.add_command(label="Add Members",command=addmember)
                      mem.add_separator()
                      mem.add_command(label="Edit Members",command=editmember)
                      mem.add_separator()
                      own.configure(menu=menubar)
                      menubar.add_cascade(label="Members", menu=mem)
                      f = Menu(menubar, tearoff=0)
                      f.add_command(label="Add Fees",command=fees)
                      own.configure(menu=menubar)
                      menubar.add_cascade(label="Fees", menu=f)
                      r = Menu(menubar, tearoff=0)
                      r.add_command(label="Equipment Report",command=report3)
                      r.add_separator()
                      r.add_command(label="Master Report",command=report2)
                      r.add_separator()
                      r.add_command(label="Members Report",command=report1)
                      r.add_separator()
                      own.configure(menu=menubar)
                      menubar.add_cascade(label="Report", menu=r)
                      e = Menu(menubar, tearoff=0)
                      e.add_command(label="Exit", accelerator="Alt+F4", command=toplogin.destroy)
                      own.configure(menu=menubar)
                      menubar.add_cascade(label="Exit", menu=e)
                      own.mainloop()
                    else:
                        messagebox.showerror("Error", "No such Owner Found")
                if num.get()=="Traniee":
                    name = str(e1.get())
                    password = str(e2.get())
                    sql1 = "select * from user where name='%s' and password='%s'" % (name, password)
                    r2 = cursor.execute(sql1)
                    if r2 > 0:
                        user= Toplevel(toplogin)
                        user.title("USER INTERFACE")
                        user.geometry("1366x768")
                        user.configure(bg="black")
                        label = Label(user, text="FITNESS CENTER ", font=('Algerian', 30), fg="white", bg="black")
                        label.place(x=500, y=30)
                        pathg = r"D:\image.jpg"
                        imgg= ImageTk.PhotoImage(Image.open(pathg))
                        panelg = Label(user, image=imgg)
                        panelg.place(x=20, y=150)
                        panelg.place_configure(width=1366, height=520)
                        btnhome = Button(user, text="Change Password", bg="orange", fg="white", font=("arial", 16),command=change)
                        btnhome.place(x=20, y=100)
                        btnhome.place_configure(width=200, height=50)
                        btnhome = Button(user, text="Report", bg="orange", fg="white", font=("arial", 16),command=reciept)
                        btnhome.place(x=220, y=100)
                        btnhome.place_configure(width=200, height=50)
                        btnhome = Button(user, text="Logout", bg="orange", fg="white", font=("arial", 16), command=user.destroy)
                        btnhome.place(x=420, y=100)
                        btnhome.place_configure(width=200, height=50)
                        user.mainloop()
                    else:
                        messagebox.showerror("error","No Trainee Found")
            except:
                messagebox.showwarning("warning", "Enter correct values")
        else:
            messagebox.showinfo("value", "Kindly fill all entries")



    #login page
    toplogin=Toplevel(top)
    toplogin.geometry("1366x768")
    toplogin.configure(bg="black")
    label = Label(toplogin, text="FITNESS CENTER ", font=('Algerian', 30), fg="white", bg="black")
    label.place(x=500, y=30)
    label1 = Label(toplogin, text="LOGIN", font=("arial", 27), bg="black", fg="green")
    label1.place(x=80, y=90)
    l=Label(toplogin,text="Login as :",fg="white",bg="black")
    l.place(x=510,y=190)
    num = StringVar()
    cb = Combobox(toplogin, textvariable=num, state="Readonly", width=27)
    cb["values"] = ("--Select type--","Owner","Traniee")
    cb.place(x=590, y=190)
    cb.current(0)
    l1 = Label(toplogin, text="Username :",fg="white",bg="black")
    l1.place(x=510, y=220)
    e1 = Entry(toplogin, bg="white", fg="black", width=30)
    e1.place(x=590, y=220)
    l2 = Label(toplogin, text="Password :",fg="white",bg="black")
    l2.place(x=510, y=250)
    e2 = Entry(toplogin, bg="white", fg="black", width=30, show='*')
    e2.place(x=590, y=250)
    btn1 = Button(toplogin, text="Login", relief=RAISED, fg="red", bg="black", font=(20),command=log)
    btn1.place(x=530, y=290)
    btn2 = Button(toplogin, text="Back", relief=RAISED, command=toplogin.destroy, fg="red", bg="black", font=(20))
    btn2.place(x=600, y=290)
    btn3 = Button(toplogin, text="Reset", relief=RAISED, fg="red", bg="black", font=(20),command=reset)
    btn3.place(x=660, y=290)
    path4 = r"D:\equip2.jpg"
    img4= ImageTk.PhotoImage(Image.open(path4))
    plane4= Label(toplogin, image=img4)
    plane4.place(x=50, y=150)
    plane4.place_configure(width=400, height=250)
    path5 = r"D:\image3.jpg"
    img5= ImageTk.PhotoImage(Image.open(path5))
    plane5 = Label(toplogin, image=img5)
    plane5.place(x=50, y=430)
    plane5.place_configure(width=400, height=250)
    path6 = r"D:\image4.jpg"
    img6 = ImageTk.PhotoImage(Image.open(path6))
    plane6= Label(toplogin, image=img6)
    plane6.place(x=850, y=150)
    plane6.place_configure(width=400, height=250)
    path7 = r"D:\save.jpg"
    img7= ImageTk.PhotoImage(Image.open(path7))
    plane7 = Label(toplogin, image=img7)
    plane7.place(x=850, y=430)
    plane7.place_configure(width=400, height=250)
    h=Label(toplogin,text="Don't Give up",font=('Goudy Stout',20),bg="black",fg="green")
    h.place(x=460,y=500)
    toplogin.mainloop()

#top first page
label=Label(top,text="FITNESS CENTER ",font=('Algerian',30),fg="white",bg="black")
label.place(x=500,y=30)
btnhome=Button(top,text="Home",bg="orange",fg="white",font=("arial",16),command=home)
btnhome.place(x=20,y=100)
btnhome.place_configure(width = 200, height = 50)
btnhome=Button(top,text="About us",bg="orange",fg="white",font=("arial",16),command=aboutus)
btnhome.place(x=220,y=100)
btnhome.place_configure(width = 200, height = 50)
btnhome=Button(top,text="Login",bg="orange",fg="white",font=("arial",16),command=login)
btnhome.place(x=420,y=100)
btnhome.place_configure(width = 200, height = 50)
btnhome=Button(top,text="Contact us",bg="orange",fg="white",font=("arial",16),command=contactus)
btnhome.place(x=620,y=100)
btnhome.place_configure(width = 200, height = 50)
path=r"D:\page.jpg"
img = ImageTk.PhotoImage(Image.open(path))
plane=Label(top,image=img)
plane.place(x=20,y=150)
plane.place_configure(width=1366,height=520)
path1=r"D:\will.jpg"
img1 = ImageTk.PhotoImage(Image.open(path1))
plane1=Label(top,image=img1)
plane1.place(x=960,y=160)
plane1.place_configure(width=270,height=170)
tag=Label(top,text="Sore Today,",bg="black",fg="red",font=(('Cooper Black'),25))
tag.place(x=250,y=400)
line=Label(top,text="Strong Tomorrow",bg="black",fg="red",font=(('Cooper Black'),25))
line.place(x=420,y=450)

top.mainloop()