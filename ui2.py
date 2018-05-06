from tkinter import *
import os
from main1 import file_ext_list,file_date_list


def file_type():
    print ("value is:" + variable1.get())

def owner_type():
    print ("value is:" + variable2.get())

def get_two():
		option=e2.get()

		if (int(option)==1):
			global variable1
			root2=Tk()
			root2.configure(background="skyblue1")
			root2.geometry("400x200")

			theLabel4=Label(root2,text="Enter the file extension of your choice",bg="cyan",fg="orange",height=5,font=("Arial", 16))
			theLabel4.pack(fill=X)

			variable1 = StringVar(root2)
			variable1.set(file_ext_list[0]) # default value

			w1 = OptionMenu(root2, variable1, *file_ext_list)
			w1.pack()

			button3 = Button(root2, text="OK", command=file_type)
			button3.pack()
			
		elif(int(option)==2):
			global variable2

			root3=Tk()
			root3.configure(background="skyblue1")
			root3.geometry("400x200")

			theLabel5=Label(root3,text="Enter the creation date of your choice",bg="cyan",fg="orange",height=5,font=("Arial", 16))
			theLabel5.pack(fill=X)

			variable2 = StringVar(root)
			variable2.set(file_date_list[0]) # default value

			w2 = OptionMenu(root3, variable2, *file_date_list)
			w2.pack()

			button4 = Button(root3, text="OK", command=owner_type)
			button4.pack()
		

		# for the second window 
		
		# root1=Tk()
		# root1.configure(background="skyblue1", )
		# root1.geometry("400x400") 
		# theLabel3=Label(root1,text="FILE APPLICATION",bg="cyan",fg="orange",height=5,font=("Arial", 16))
		# theLabel4.pack(fill=X)
		# root1.mainloop()
		# root.quit()

root=Tk() 

root.configure(background="skyblue1")
root.geometry("400x800") 

theLabel1=Label(root,text="FILE APPLICATION",bg="cyan",fg="orange",height=5,font=("Arial", 16))
theLabel1.pack(fill=X)

theLabel3=Label(root,text="Select search criteria 1. Search by File Type 2. Search by Date of Creation",bg="white",font=("Arial", 10))
theLabel3.pack(fill=X, pady=20)

e2 = Entry(root, width=50)
e2.pack(pady=40)

Button2 = Button(root, text="Enter", command=get_two) 
Button2.pack()

'''variable1 = StringVar(root)
variable1.set(file_ext_list[0]) # default value

w1 = OptionMenu(root, variable, *file_ext_list)
w1.pack()

def file_type():
    print ("value is:" + variable1.get())

button3 = Button(root, text="OK", command=file_type)
button3.pack()
variable2 = StringVar(root)
variable2.set(file_owner_list[0]) # default value

w2 = OptionMenu(root, variable2, *file_owner_list)
w2.pack()

def owner_type():
    print ("value is:" + variable2.get())

button4 = Button(root, text="OK", command=owner_type)
button4.pack()'''
root.mainloop()



