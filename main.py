import os
import shutil
import datetime
from os import stat
from pwd import getpwuid
import sys
from shutil import copyfile


filename="directory.txt"
filename1="final_directory.txt"

file=open(filename,"a")


#file names
folder_path=sys.argv[1]
#print(folder_path)
#folder_path = "/home/tejeshreddy/progs/python" 
names = os.listdir(folder_path)
# print(names)                                                       #Name Printing
# print("\n")

def modification_date(filename):                                   #To get the time stamp
	t = os.path.getmtime(filename)
	return datetime.datetime.fromtimestamp(t)

def find_owner(filename):											#To get the owner of the file
	return getpwuid(stat(filename).st_uid).pw_name


creation_date=[]
file_owner=[]
file_ext=[]
file_name=[]

for i in names:
	file_path=folder_path+"/"+i
	d = modification_date(file_path)    #function
	date = str(d.day).zfill(2) +"."+ str(d.month).zfill(2) +"."+str(d.year)
	creation_date.append(date)
	owner = find_owner(file_path)
	file_owner.append(owner)


for f in names:
	fi_name,fi_ext = os.path.splitext(f)
	file_name.append(fi_name)
	file_ext.append(fi_ext)


######################DEBUG SECTION################
# print(file_name)
# print("\n")
# print(creation_date)										# Creation Date Printing
# print("\n")
# print(file_owner)											#File Owner Printing
# print("\n")
# print(file_ext)
# print(len(file_owner),len(names),len(names))
# print("\n\n\n")

x=len(names)
y=0


#creating the file "directory"
for y in range(0,x):
	file.write(file_name[y]+"|")
	file.write(creation_date[y]+"|")
	file.write(file_owner[y]+"|")
	file.write(file_ext[y]+"\n")
file.close()

#new file name is being created

file=open(filename,"r+")
file1=open(filename1,"w")

for z in file:
	f_name,f_date,f_owner,f_ext=z.split("|")
	
	f_name = f_name.strip()
	f_date = f_date.strip()
	f_owner = f_owner.strip()
	f_ext = f_ext.strip()

	f_newname = '{} - {} - {}'.format(f_owner, f_date, f_name)
	
	file1.write(f_name+"|")
	file1.write(f_newname+"|")
	file1.write(f_ext+"\n")

file.close()
file1.close()

#creating the index file in the traget directory
current_wd = os.getcwd()
current_wd = current_wd +"/"+filename1
#print(current_wd)


os.chdir(folder_path)

target_wd = os.getcwd()
###################FOLDER ACCESS HAS BEEN CHANGED######################

filename2 = "#index.txt"
target_wd = target_wd +"/"+filename2

file2=open(filename2,"w")
copyfile(current_wd,target_wd)
file2.close()

#renaming opertaion..

file2 = open(filename2,"r")

for var in file2:
	f,nf,ext= var.split("|")
	
	f = f.strip()
	nf = nf.strip()
	ext= ext.strip()
	
	old_name = '{}{}'.format(f , ext)
	new_name = '{}{}'.format(nf , ext)
	print(f,nf,ext)
	#os.rename(old_name,new_name)
	