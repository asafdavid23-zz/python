import os

dir_to_scan = "C:\\Users\\Assaf David\\Desktop\\chedek\\"															# set variablefor the dest file.

def create_csv(old, new, columns):																				    # def a function to handle the process.
	with open(old, 'r+') as f:																						# open the old file.
		with open(new, 'w+') as f_new: 																				# open the new file.
			f_new.seek(0, 0)																						# go to the begining of the file.
			f_new.write(columns + '\n')																				# write the column names to the first line

			for line in f: 																							# run over the file
				f_new.write(line.replace('|', ','))																	# Replace '|' with ','
		f_new.close()																								# close the new file
	f.close()
	os.remove(old)

def check_txt_is_exist(file):																						# def a function to check csv is exist
	filename = os.fsdecode(file)																					# set variable
	if filename.endswith(".txt"):																					# check if the file is a txt
		return file
		
def check_csv_is_exist(file):																						# def a function to check csv is exist
	filename = os.fsdecode(file)																					# set variable
	if filename.endswith(".csv"):																					# check if the file is a txt
		return file																									# return the file
				

for file in os.listdir(dir_to_scan):																				# run over dir_to_Scan
	if check_txt_is_exist(file):
		columns_head = input('Please enter columns names with comma delimited: \n')									# columns name.																						
		file_new = check_txt_is_exist(file).replace(".txt", ".csv")													# Set new file name variable
		create_csv(file, file_new, columns_head)																	# Call crate CSV function
		print("%s is updated." % file) 																				# print message
																																											
	elif check_csv_is_exist(file):
		print("%s, is alrady in CSV Format." % file)																# print message

	else:
		print("%s, is not CSV and not TXT format." % file)															# print message
