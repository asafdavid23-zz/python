
# -*- coding: utf-8 -*-
import os

dir_to_scan = "C:\\Users\\Assaf David\\Desktop\\chedek\\"	# set variable for the dest file.

def csv(old_file, new_file, columns):
    with open(old_file, 'r+', encoding = "ISO-8859-1") as f:
        with open(new_file, 'w+', encoding = "ISO-8859-1") as f_new:
            for line in f:
                if "PID" in line:
                    line = line.split('||')

                    while ("" in line):
                        line.remove("")

                    line.remove('C')
                    line.remove('PID')
                    line.remove('\n')
                    print(line)
                    line[1] = line[1].replace('^', ' ')
                    line[2] = line[2].replace('|', '')
                    print(line[1])
                    print(line[2])

                    f_new.seek(0, 0)								# go to the begining of the file.
                    f_new.write(columns + '\n')
                    f_new.write(line[0] + ',' + line[1] + ',' + line[2])
        f_new.close()
    f.close()

def check_csv_is_exist(file):								# def a function to check csv is exist
	filename = os.fsdecode(file)							# set variable
	if filename.endswith(".csv"):							# check if the file is a txt
		return True											# return the file

for file in os.listdir(dir_to_scan):
    txt = check_csv_is_exist(file)

    if txt:
        columns_head = input('Please enter columns names with comma delimited: \n')		# columns name.`
        file_new = os.fsdecode(file).replace('.txt', '.csv')
        csv(file, file_new, columns_head)
        print("%s is updated." % file) 													# print message
    else:
        print("There is no any TXT files in dest folder.")