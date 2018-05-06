import os
os.chdir('/home/tejeshreddy/Desktop/FS Sample/1')

#print(os.getcwd())

for f in os.listdir():
	#print(f)
	#print(os.path.splitext(f))
	f_name,f_ext = os.path.splitext(f)
	#print(f_name.split('-'))
	f_title,f_course,f_num=f_name.split('-')
	#print(f_num)
	f_title = f_title.strip()
	f_course = f_course.strip()
	f_num = f_num.strip()[1:].zfill(2)
	f_num = '#'+f_num

	print('{}-{}-{}{}'.format(f_course, f_num, f_title, f_ext))
	new_name = '{} - {} - {}{}'.format(f_course, f_num, f_title, f_ext)
	os.rename(f, new_name)	