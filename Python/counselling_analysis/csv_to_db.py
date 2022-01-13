import sqlite3
import csv

def create_table():
    conn = sqlite3.connect('tnea_file.db')
    cur = conn.cursor()

    sql = '''
        CREATE TABLE tnea_2019 (
            SNO INTEGER,
            ANO TEXT,
            COM TEXT,
            ORANK TEXT,
            CRANK TEXT,
            MARK TEXT,
            CCODE TEXT,
            BRANCH TEXT,
            CHOICE NO TEXT,
            ACATEGORY TEXT,
            PRIMARY KEY(SNO)
        )'''

    cur.execute(sql)
    conn.commit()
    conn.close()

def write_table():
    conn = sqlite3.connect('tnea_file.db')
    cur = conn.cursor()

    with open('tnea_file.csv', 'r') as csv_file:
        no_rec = 0
        for row in csv_file:
            cur.execute(
            "INSERT INTO tnea_2019 VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", row.split("|")
            )
            conn.commit()
            no_rec += 1

    conn.close()


write_table()
