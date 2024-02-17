from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("MARKSHEET")
window.geometry("700x400")


def calculate():
    nm_val = name.get()
    roll_val = roll.get()
    seat_val = seat.get()
    python_val = python.get()
    android_val = android.get()
    dw_val = dw.get()
    project_val = project.get()
    if nm_val == "" or roll_val == "" or seat_val == "" or python_val == "" or android_val == "" or dw_val == "" or project_val == "":
        not_valid()
    else:
        if int(python_val)>100 or int(android_val)>100 or int(dw_val)>100 or int(project_val)>100 :
            messagebox.showinfo("Not in Range","Please Fill Marks between 0 to 100")
        else:
            total = int(python_val) + int(android_val) + int(dw_val) + int(project_val)
            Label(window, text=total).place(x=520,y=120)

            per = total/4
            per_val = f"{per:.1f}%"
            Label(window, text=per_val).place(x=515,y=140)

            if int(python_val)<28 or int(android_val)<28 or int(dw_val)<28 or int(project_val)<28 :
                result = "Fail "
            else:
                result = "Pass"
            Label(window, text = result).place(x=516,y=180)

            if float(per)>=70 and float(per)<=100:
                grade = "A"
            elif float(per)>=50 and float(per)<=69:
                grade = "B"
            elif float(per)>=35 and float(per)<=49:
                grade = "C"
            elif float(per)<=34 or result=="Fail":
                grade = "F"
            
            Label(window, text=grade).place(x=525,y=160)

def not_valid():
    messagebox.showinfo("Incomplete","Please Fill All Required Fields")

Label(window, text="Name").place(x=10,y=10)
name = Entry(window)
name.place(x=60, y=10)
Label(window, text="Roll No.").place(x=10,y=40)
roll = Entry(window)
roll.place(x=60,y=40)
Label(window, text="Seat No.").place(x=400,y=10)
seat = Entry(window)
seat.place(x=460,y=10)

Label(window, text="Sr. No").place(x=20,y=100)
Label(window, text="1").place(x=30,y=120)
Label(window, text="2").place(x=30,y=140)
Label(window, text="3").place(x=30,y=160)
Label(window, text="4").place(x=30,y=180)

Label(window, text="Subject").place(x=120,y=100)
Label(window, text="Python").place(x=120,y=120)
Label(window, text="Android").place(x=117,y=140)
Label(window, text="DW").place(x=128,y=160)
Label(window, text="Project").place(x=120,y=180)

Label(window, text="Marks").place(x=260,y=100)
python = Entry(window)
python.place(x=220,y=120)
android = Entry(window)
android.place(x=220,y=140)
dw = Entry(window)
dw.place(x=220,y=160)
project = Entry(window)
project.place(x=220,y=180)

Label(window, text="Total Marks").place(x=400,y=120)

Label(window, text="Percentage").place(x=400,y=140)

Label(window, text="Grade").place(x=416,y=160)

Label(window, text="Result").place(x=415,y=180)

submit = Button(window, text="Submit", bg="blue", fg="white", command=calculate).place(x=118,y=220)

window.mainloop()
