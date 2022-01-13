import csv
import time

start = time.perf_counter()

with open('tnea_file.csv', 'r') as file_handle:
    file_reader = csv.DictReader(file_handle, delimiter='|')
    fieldnames = next(file_reader)

    with open('temp_file1.csv', 'w', newline='') as temp_file:
        temp_writer = csv.DictWriter(temp_file, delimiter='\t', fieldnames=fieldnames)
        temp_writer.writeheader()

        for row in file_reader:
            if row['C.CODE'] == '2711':
                temp_writer.writerow(row)
        temp_file.close()
    file_handle.close()

stop = time.perf_counter()
print(f"Time taken: { stop - start }")
