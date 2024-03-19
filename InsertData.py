# This Module has the Functions to Insert the Data in the MySQL Tables

# Importing Required Modules

import csv
import mysql.connector as con

# Functions


def InsertDataTrain():
    """
    InsertDataTrain() -> Inserts all the Train details in the train_info Table

    Parameters -> None
    """

    mn = con.connect(host="localhost",
                     user='root',
                     password='Sangeeta@5785',
                     database="railway")

    cur = mn.cursor()

    # Iterating through all the values and insert's them in the table
    # Replace the path below with the absolute path of the file on your computer
    try:
        with open("Train_details.csv") as csv_data:
            csv_reader = csv.reader(csv_data, delimiter=",")
            for row in csv_reader:
                row_data = tuple(row[0].split(','))
                cur.execute(
                    'INSERT INTO train_info VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (row_data[0],row_data[1],row_data[2],row_data[3],row_data[4],row_data[5],row_data[6],row_data[7],row_data[8],row_data[9]))
                
    except FileNotFoundError:
        print("Please check whether the file is in the Assets Folder or not and try changing the Location in InsertData.py")
    
    finally:
        mn.commit()  # Important: Committing the Changes
        cur.close()
        mn.close()