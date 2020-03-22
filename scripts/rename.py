import os
import glob

os.chdir("/home/rohit/Desktop/python/scripts")

for file in glob.glob("*.json"):
	file_name = os.path.splitext(file)[0]
	extension = os.path.splitext(file)[1]
	#print(file_name)
	#print(extension)
	new_file_name = file_name[:-6]+extension
	try:
		os.rename(file,new_file_name)
	except OSError  as e:
		print(e)
	else:
		print("Renamed {} to {}".format(file,new_file_name))
		


