import csv
import os
import time


class Examine:
    file_handle = open('tnea_file.csv', 'r')
    temp_file = open('temp_file.csv', 'w', newline='')
    final_file = open('final_file.csv', 'w', newline='')

    file_reader = csv.DictReader(file_handle, delimiter='|')
    fieldnames = next(file_reader)
    
    temp_writer = csv.DictWriter(temp_file, delimiter="\t", fieldnames=fieldnames)
    temp_writer.writeheader()

    final_writer = csv.DictWriter(final_file, delimiter="\t", fieldnames=fieldnames)
    final_writer.writeheader()

    def __init__(self, ddic):

        self.l = ddic.keys()
        self.temp1 = {}
        self.temp2 = []
        for item in self.l:
            for row in self.file_reader:
                if row[item] in ddic[item]:
                    self.temp_writer.writerow(row)
                    if row['S.NO'] in self.temp1:
                        self.temp1[row['S.NO']] += 1
                    else:
                        self.temp1[row['S.NO']] = 1
            self.file_handle.seek(0)
        

        maxval = max(self.temp1.values())
        for item in self.temp1:
            if self.temp1[item] == maxval:
                self.temp2.append(item)
        
        for row in self.file_reader:
            if row['S.NO'] in self.temp2:
                self.final_writer.writerow(row)
        
        self.file_handle.close()
        self.temp_file.close()
        self.final_file.close()

        os.remove('temp_file.csv')
        
        stop = time.perf_counter()
        print(f"Time taken: { stop - start }")


code = ['0004']
branch = []
com = []



ddic = {'BRANCH': branch, 'C.CODE': code, 'COM': com}
start = time.perf_counter()
obj = Examine(ddic)


