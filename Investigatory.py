#Project on:- School Admission Form
#Developed by:-Pragati
#importing all the functions of tkinter
from tkinter import *
#importing PILLOW(Pillow is a Python Imaging Library (PIL), which adds
#support for opening, manipulating, and saving images.)
from PIL import ImageTk
#importing messagebox
from tkinter import messagebox
#importing CSV (Comma Separated Values)
import csv

#function for taking values
def values():
#coding for taking values from user
#by using the function get()
name_values=name.get()
Class_values=Class.get()
age_values=age.get()
parent_name_values=parent_name.get()
gender_values=gender.get()
contact_no_values=contact_no.get()
# if the field are empty
if name_values== "":
messagebox.showinfo('Error','Please enter Student Name!!')
elif Class_values== 0:
messagebox.showinfo('Error','Please enter Class!!')

Page 10

elif age_values== 0:
messagebox.showinfo('Error','Please enter Age!!')
elif parent_name_values== "":
messagebox.showinfo('Error','Please enter Parent Name!!')
elif gender_values== "":
messagebox.showinfo('Error','Please enter the Gender!!')
elif contact_no_values== 0:
messagebox.showinfo('Error','Please enter Contact Number!!')

#checking for valid contact no.
#printing the values entered by the user
else:
a=str(contact_no_values)
Len=len(a)
if 10<Len or Len<10:
messagebox.showerror('ERROR','you entered invalid Contact no.!!!')
#Confirmation page
else:
result=messagebox.askquestion('Confirmation' , 'Please,finally check you
details\n ' + name_values +'\n' +str(Class_values) + '\n' + str(age_values)
+ '\n' + parent_name_values + '\n' + gender_values + '\n' + str(contact_no
_values))
if result =='yes' :
messagebox.showinfo('Sussecful','You are sussecfully resigtered!!!')
#saving data in CSVfile
with open('F:\\registration form.csv', mode='a') as file:
writer = csv.writer(file, delimiter=',' )
writer.writerow([name_values,Class_values,age_values,
parent_name_values,gender_values,contact_no_values])

file.close
#defining a function show details
def show_details():
window=Tk( )
#using csv in read mode
with open('F:\\registration form.csv', mode='rt') as f:

Page 11

data=csv.reader(f)
s=0
#showing the data
for j in data:
s=s+1
Label(window,text=j[0]).grid(row=s,column=0)
Label(window,text=j[1]).grid(row=s,column=1)
Label(window,text=j[2]).grid(row=s,column=2)
Label(window,text=j[3]).grid(row=s,column=3)
Label(window,text=j[4]).grid(row=s,column=4)
Label(window,text=j[5]).grid(row=s,column=5)

f.close()
root.mainloop()
#creating a class and defining various functions
#designing the body of the admission form
root=Tk( )
root.title("Admission Form")
root.geometry("1600x900+0+0")
#selecting some images
bg_icon=ImageTk.PhotoImage(file="F:\photo\kv.jpg")
logo_icon=ImageTk.PhotoImage(file="F:\photo\kvs new logo1.jpg")
userlogo_icon=ImageTk.PhotoImage(file="F:\photo\down.jpg")
user_icon=ImageTk.PhotoImage(file="F:\photo\download.jpg")

#defining the datatype
name=StringVar()
Class=IntVar()
age=IntVar()
parent_name=StringVar()
gender=StringVar()
contact_no=IntVar()
#setting an image in the background of the form

Page 12

bg_lbl=Label(root,image=bg_icon).grid(row=0,column=0)
#GUI Coding
#-Title
title=Label(root,text="Admission Form",font=("times new
roman",40,"bold"),bg="dark red",fg="white",bd=10,relief="groove")
title.place(x=0,y=0,relwidth=1)

#-Making a frame
Login_Frame=Frame(root,bg="white")
Login_Frame.place(x=400,y=110)
#-Placing the images
userlbl=Label(Login_Frame,image=userlogo_icon).grid(row=0,columnspan=2,p
ady=20)
schoollg=Label(Login_Frame,image=logo_icon).grid(row=1,column=0,padx=20
,pady=10)
schoollbl=Label(Login_Frame,text="K.V No.4 O.N.G.C Vadodara",font=("times
new roman",20,"bold"),bg="white",fg="maroon").grid(row=1,column=1,padx
=20,pady=10)
#-Designing labels,textboxes and placing it
# 1. Label:- Student Name
namelbl=Label(Login_Frame,text="Student
Name",image=user_icon,compound=LEFT,font=("times new
roman",20,"bold"),bg="white").grid(row=2,column=0,padx=20,pady=10)
txtname=Entry(Login_Frame,bd=5,textvariable=name,relief="groove",font=("
",15)).grid(row=2,column=1,padx=20)
# 2. Label:- Class
classlbl=Label(Login_Frame,text="Class",image=user_icon,compound=LEFT,fo
nt=("times new
roman",20,"bold"),bg="white").grid(row=3,column=0,padx=20,pady=10)
txtclass=Entry(Login_Frame,bd=5,textvariable=Class,relief="groove",font=("
",15)).grid(row=3,column=1,padx=20)
# 3. Label:- Age
agelbl=Label(Login_Frame,text="Age",image=user_icon,compound=LEFT,font

Page 13
=("times new roman",20,"bold"),bg="white").grid(row=4,column=0,padx=20
,pady=10)
txtname=Entry(Login_Frame,bd=5,textvariable=age,relief="groove",font=("
",15)).grid(row=4,column=1,padx=20)
# 4. Label:- Parent Name
parent_namelbl=Label(Login_Frame,text="Parent
Name",image=user_icon,compound=LEFT,font=("times new
roman",20,"bold"),bg="white").grid(row=5,column=0,padx=20,pady=10)
txtparentname=Entry(Login_Frame,bd=5,textvariable=parent_name,relief="groo
ve",font=(" ",15)).grid(row=5,column=1,padx=20)
# 5. Label:- Gender
genderlbl=Label(Login_Frame,text="Gender",image=user_icon,compound=LEF
T,font=("times new
roman",20,"bold"),bg="white").grid(row=6,column=0,padx=20,pady=10)
L=["Male","Female"]
droplist=OptionMenu(Login_Frame,gender,*L)
droplist.config(font=("times new
roman",15,"bold"),bd=5,relief="groove",width=19)
droplist.grid(row=6,column=1)
# 6. Label:- Contact Number
contact_nolbl=Label(Login_Frame,text="Contact
No.",image=user_icon,compound=LEFT,font=("times new
roman",20,"bold"),bg="white").grid(row=7,column=0,padx=20,pady=10)
txtcontact_no=Entry(Login_Frame,bd=5,textvariable=contact_no,relief="groove
",font=(" ",15)).grid(row=7,column=1,padx=20)
#making Submit Button and placing it
btn_submit=Button(Login_Frame,text="Submit",width=15,font=("times new
roman",14,"bold"),command=values,bg="orange",fg="white").grid(row=8,colum
n=0,pady=10)
#making show details button and placing it
btn_show_details=Button(Login_Frame,text="Show Details",width=15,font=
("times new roman",14,"bold" ),command=show_details ,bg="orange",fg=
"white").grid(row=8,column=1,pady=10)
root.mainloop()
