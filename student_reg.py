from tkinter import *
from tkinter import messagebox

from PIL import ImageTk,Image
import tkinter
import ar_master
import sample_data

mm = ar_master.master_flask_code()


window=tkinter.Tk()
window.geometry("700x600")
window.title("student_attentive")
class sample:
    name="guru"

image_0=Image.open('static/class.jpg')
bck_end=ImageTk.PhotoImage(image_0)

def login():
    
  text1=entry1.get()
  text2=entry2.get()
  if(text1=="" and text2==""):
    messagebox.showinfo(title="Alert", message="Enter Your Name")
  else:
    sample_data.student.name=text1
    maxin = mm.find_max_id("student_details")
    qry = ("insert into student_details values('" + str(maxin) + "','" + str(text1) + "','" + str(
        text2) + "','')")
    result = mm.insert_query(qry)


    import face_reg


def back():
    window.destroy()
    import staff_home


canvas = tkinter.Canvas(window,  width=1550, height=900)
canvas.pack()
canvas.create_image(-10,-3,anchor=NW,image=bck_end)

canvas.create_text(200,220,text="Name",font=('times', 15, ' bold '),fill="white")

canvas.create_text(200,300,text="Register Number",font=('times', 15, ' bold '),fill="white")

entry1=Entry(width=20,font=('times', 15, ' bold '))
entry1.place(x=300,y=210)
entry2=Entry(width=20,font=('times', 15, ' bold '))
entry2.place(x=300,y=285)

txt=Button(window,width=10,height=0,text="Add",fg="white",bg="#334CAF",font=('times', 15, ' bold '),command=login)
txt.place(x=160,y=450)
txt=Button(window,width=10,height=0,text="Back",fg="white",bg="#334CAF",font=('times', 15, ' bold '),command=back)
txt.place(x=380,y=450)

window.mainloop()