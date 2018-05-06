from tkinter import *
import os

def get_one():

		'''command='python3 main1.py '+path
		os.system(command) '''

		path=e1.get()
		command='python3 main1.py '+path
		os.system(command)


root=Tk() 

root.configure(background="skyblue1")
root.geometry("400x800") 

theLabel1=Label(root,text="FILE APPLICATION",bg="cyan",fg="orange",height=5,font=("Arial", 16))
theLabel1.pack(fill=X)

theLabel2=Label(root,text="Select filename",bg="white",font=("Arial", 10))
theLabel2.pack(fill=X, pady=20)

e1 = Entry(root, width=50)
e1.pack(pady=40)

Button1 = Button(root, text="Enter", command=get_one) 
Button1.pack()


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

