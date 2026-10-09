#!/usr/bin/env python3
# Command-line CRUD menu for the person table in bmcaving.
# Based on databaseExample/07-1-connectToDB/6-menu.py
# Credentials are loaded from a .env file (not committed to git).

import mysql.connector, os
from dotenv import load_dotenv
load_dotenv()

def getConnection():
    connection = mysql.connector.connect(
        host=os.getenv('SQL_HOST'),
        user=os.getenv('SQL_USER'),
        password=os.getenv('SQL_PWD'),
        database=os.getenv('SQL_DB')
    )
    return connection

def blankToNone(value):
    # Optional columns: an empty answer is stored as NULL
    return value if value.strip() else None

def printTable():
    connection = getConnection()
    mycursor = connection.cursor()
    mycursor.execute("select person_id, first_name, last_name, role, years_active from person")
    print("\nIn the person table, we have the following items:")
    print("id | first_name | last_name | role | years_active")
    for row in mycursor.fetchall():
        print(" | ".join(str(value) for value in row))
    connection.close()
    print()

def insertIntoTable():
    firstname = input("First name: ")
    lastname = input("Last name: ")
    role = blankToNone(input("Role (optional): "))
    years = blankToNone(input("Years active (optional): "))
    connection = getConnection()
    mycursor = connection.cursor()
    query = "insert into person (first_name, last_name, role, years_active) values (%s, %s, %s, %s)"
    mycursor.execute(query, (firstname, lastname, role, years))
    connection.commit()
    print(f"Inserted new person with id {mycursor.lastrowid}\n")
    connection.close()

def updateRow():
    rowToUpdate = input("What is the id of the row you want to update? ")
    connection = getConnection()
    mycursor = connection.cursor()
    mycursor.execute("select * from person where person_id=%s", (rowToUpdate,))
    current = mycursor.fetchone()
    if current is None:
        print("No person with that id.\n")
        connection.close()
        return
    print(f"The current row has the value: {current}")
    print("Press Enter to keep the current value.")
    firstname = input(f"First name [{current[1]}]: ") or current[1]
    lastname = input(f"Last name [{current[2]}]: ") or current[2]
    role = input(f"Role [{current[3]}]: ") or current[3]
    years = input(f"Years active [{current[4]}]: ") or current[4]
    query = "update person set first_name=%s, last_name=%s, role=%s, years_active=%s where person_id=%s"
    mycursor.execute(query, (firstname, lastname, role, years, rowToUpdate))
    connection.commit()
    print("Row updated.\n")
    connection.close()

def deleteRowFromTable():
    rowToDelete = input("What is the id of the row to delete? ")
    connection = getConnection()
    mycursor = connection.cursor()
    try:
        mycursor.execute("delete from person where person_id=%s", (rowToDelete,))
        connection.commit()
        print(f"Deleted {mycursor.rowcount} row(s).\n")
    except mysql.connector.Error as err:
        print(f"Could not delete: {err.msg}\n")
    connection.close()

menuText = """Please select one of the following options:
1) Display contents of table
2) Insert new row to table
3) Update a row of the table
4) Delete a row of the table
q) Quit
"""

if __name__ == "__main__":
    menuOption = ""
    while menuOption != 'q':
        menuOption = input(menuText)
        if menuOption == "1":
            printTable()
        elif menuOption == "2":
            insertIntoTable()
        elif menuOption == "3":
            updateRow()
        elif menuOption == "4":
            deleteRowFromTable()
