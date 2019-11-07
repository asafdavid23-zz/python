
# -*- coding: utf-8 -*-
import os

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

                    # f_new.seek(0, 0)								# go to the begining of the file.
                    # f_new.write(columns + '\n')
                    # f_new.write(line[0] + ',' + line[1] + ',' + line[2])
        f_new.close()
    f.close()

csv('DemogExample.txt', 'DemogExample.csv', 'name, surename,phone')