import os
import shutil
import datetime
from os import stat
from pwd import getpwuid
import sys
from shutil import copyfile


#---------Functions-----
def modification_date(filename):                                   #To get the time stamp
	t = os.path.getmtime(filename)
	return datetime.datetime.fromtimestamp(t)

def find_owner(filename):											#To get the owner of the file
	return getpwuid(stat(filename).st_uid).pw_name

#---------End-----------

filename="index_file.txt"
filename1="attribute_file.txt"

file=open(filename,"a")

# folder_path = "/home/tejeshreddy/progs/python" 
folder_path=sys.argv[1] 

#print(folder_path)
names = os.listdir(folder_path)
#print(names)

#----all lists---
file_path = []
file_creation_date = []
file_owner = []
file_ext = []
file_name = []
file_name_raw = []




for i in names:
	f_path=folder_path+"/"+i
	file_path.append(f_path)

x=len(names)
y=0

#------------index file creation---

for y in range(0,x):	
	file.write(names[y]+"|")
	file.write(file_path[y])
	file.write("\n")


#-----------attribute list creation---
file=open(filename,"r+")

for z in file:
	ext_file_name,ext_file_path = z.split("|")
	ext_file_name = ext_file_name.strip()
	ext_file_path = ext_file_path.strip()
	file_name.append(ext_file_name)

	d = modification_date(ext_file_path)
	date = str(d.day).zfill(2) +"."+ str(d.month).zfill(2) +"."+str(d.year)
	file_creation_date.append(date)

	owner = find_owner(ext_file_path)
	file_owner.append(owner)

	fi_name,fi_ext = os.path.splitext(ext_file_name)
	file_name_raw.append(fi_name)
	file_ext.append(fi_ext)

# print(file_path)
# print(file_name)
# print(file_name_raw)
# print(file_ext)
# print(file_owner)
# print(creation_date)



#---------attribute file creation------
file1=open(filename1,"w")

for y in range(0,x):
	file1.write(file_name[y]+'|')
	file1.write(file_name_raw[y]+'|')
	file1.write(file_owner[y]+'|')
	file1.write(file_creation_date[y]+'|')
	file1.write(file_ext[y]+'|')

	f_newname = '{} - {} - {}'.format(file_owner[y], file_creation_date[y] , file_name_raw[y])

	file1.write(f_newname)
	file1.write('\n')
file.close()
file1.close()
#-----------change of folder acess and duplicate of attribute file-------------

current_wd = os.getcwd()
current_wd = current_wd +"/"+filename1
os.chdir(folder_path)

target_wd = os.getcwd()


filename2 = "#main_index.txt"
target_wd = target_wd +"/"+filename2

file2=open(filename2,"w")
copyfile(current_wd,target_wd)
file2.close()
 
 #--------creating 2 more index files for multilevel indexing-----

file2 = open(filename2,"r")

filename3= "#file_date_index.txt"
filename4= "#file_type_index.txt"

file3 = open(filename3,"w")
file4 = open(filename4,"w")

for p in file2:
	ind_file_name , ind_file_name_raw , ind_file_owner , ind_file_date , ind_file_ext , ind_file_newname=p.split('|')
	ind_file_newname = ind_file_newname.strip()
	rename_file_newname='{}{}'.format(ind_file_newname , ind_file_ext)
	rename_file_oldname='{}{}'.format(ind_file_name_raw , ind_file_ext)
	#os.rename(rename_file_oldname,rename_file_newname)

	file3.write(ind_file_date+'|')
	file3.write(rename_file_newname+'\n')
	print(ind_file_date)
	file4.write(ind_file_ext+'|')
	file4.write(rename_file_newname+'\n')	

file_ext_list=[]
for i in file_ext:
	if i not in file_ext_list:
		file_ext_list.append(i)

file_date_list=[]
for i in file_creation_date:
	if i not in file_date_list:
		file_date_list.append(i)

