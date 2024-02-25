from tkinter import *
import mysql.connector
from tkinter import messagebox

con = mysql.connector.connect(host="localhost", user="root", passwd="", database="pydb")

cur = con.cursor()

try:
    cur.execute("CREATE TABLE IF NOT EXISTS student(rollno int(20), name varchar(20), mobile varchar(10), city varchar(20))")
except Error as e:
    con.rollback()

main = Tk()
main.geometry("700x400")

def clear():
    roll.delete(0, 'end')
    name.delete(0, 'end')
    number.delete(0, 'end')
    city.delete(0, 'end')

def insert():
    rno = roll.get()
    nm = name.get()
    num = number.get()
    ct = city.get()

    if rno == "" or nm == "" or num == "" or ct == "" :
        messagebox.showinfo("Error","Please Fill All Required Fields")
    else:
        i = cur.execute("INSERT INTO student values('"+rno+"','"+nm+"','"+num+"','"+ct+"')")
        if i != 0:
            messagebox.showinfo("Success","Record Successfull Inserted")
            clear()
        else :
            messagebox.showinfo("Error","Record is not Inserted")

def update():
    rno = roll.get()
    nm = name.get()
    num = number.get()
    ct = city.get()

    if rno == "" or nm == "" or num == "" or ct == "" :
        messagebox.showinfo("Error","Please Fill All Required Fields")
    else:
        i = cur.execute("UPDATE student set name = '"+nm+"', mobile = '"+num+"', city='"+ct+"' WHERE rollno = '"+rno+"'")
        if i != 0:
            messagebox.showinfo("Success","Record Successfull Updated")
            clear()
        else :
            messagebox.showinfo("Error","Record is not Found for Update")

def delete():
    rno = roll.get()

    if rno == "" :
        messagebox.showinfo("Error","Please Enter Roll Number to Delete Record")
    else:
        i = cur.execute("DELETE FROM student WHERE rollno = '"+rno+"'")
        if i != 0:
            messagebox.showinfo("Success","Record Successfull Deleted")
            clear()
        else :
            messagebox.showinfo("Error","Record is not Found for Delete")

def select():
    rno = roll.get()
    
    if rno == "" :
        messagebox.showinfo("Error","Please Enter Roll Number to View Record")
    else:
        cur.execute("SELECT * FROM student WHERE rollno = '"+rno+"'")
        result = cur.fetchall()
        for row in result:
            name.insert('end',row[1])
            number.insert('end',row[2])
            city.insert('end',row[3])

Label(main,text="Roll No. :",font=30).place(x=80,y=50)
Label(main,text="Student Name :",font=30).place(x=80,y=100)
Label(main,text="Mobile Number :",font=30).place(x=80,y=150)
Label(main,text="City :",font=30).place(x=80,y=200)

roll = Entry(main,font=30)
roll.place(x=300,y=50)

name = Entry(main,font=30)
name.place(x=300,y=100)

number = Entry(main,font=30)
number.place(x=300,y=150)

city = Entry(main,font=30)
city.place(x=300,y=200)

insert = Button(main,text="Insert",font=30,command=insert)
insert.place(x=100,y=280)

delete = Button(main,text="Delete",font=30,command=delete)
delete.place(x=210,y=280)

update = Button(main,text="Update",font=30,command=update)
update.place(x=320,y=280)

select = Button(main,text="Select",font=30,command=select)
select.place(x=430,y=280)

main.mainloop()
