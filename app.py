import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
    )

def print_people(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT person_id, first_name, last_name, role FROM person ORDER BY person_id;")
    for person_id, first_name, last_name, role in cursor:
        print(f"{person_id:>3}  {first_name} {last_name}  ({role})")
    cursor.close()

def print_expeditions(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT expedition_id, year, label FROM expedition ORDER BY year;")
    for expedition_id, year, label in cursor:
        print(f"{expedition_id:>3}  {year}  {label}")
    cursor.close()

MENU = """
1) Print people
2) Print expeditions
3) Print expeditions a person was on
4) Print people on an expedition
5) Add a person to an expedition
6) Remove a person from an expedition
q) Quit
"""

def print_person_expeditions(conn):
    print_people(conn)
    person_id = input("\nEnter a person ID: ").strip()

    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT e.expedition_id, e.year, e.label
        FROM expedition AS e
        JOIN expedition_person AS ep
          ON e.expedition_id = ep.expedition_id
        WHERE ep.person_id = %s
        ORDER BY e.year
        """,
        (person_id,),
    )
    rows = cursor.fetchall()
    cursor.close()

    if not rows:
        print("That person isn't on any expeditions.")
    else:
        for expedition_id, year, label in rows:
            print(f"  {expedition_id}  {year}  {label}")
   

def print_expedition_people(conn):
    print_expeditions(conn)
    expedition_id = input("\nEnter an expedition ID: ").strip()

    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT p.person_id, p.first_name, p.last_name, p.role
        FROM person AS p
        JOIN expedition_person AS ep
          ON p.person_id = ep.person_id
        WHERE ep.expedition_id = %s
        ORDER BY p.last_name
        """,
        (expedition_id,),
    )
    rows = cursor.fetchall()
    cursor.close()

    if not rows:
        print("No one is on that expedition.")
    else:
        for person_id, first_name, last_name, role in rows:
            print(f"  {person_id}  {first_name} {last_name}  ({role})")


def add_person_to_expedition(conn):
    print_people(conn)
    person_id = input("\nEnter a person ID: ").strip()
    print_expeditions(conn)
    expedition_id = input("\nEnter an expedition ID: ").strip()

    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO expedition_person (expedition_id, person_id)
            VALUES (%s, %s)
            """,
            (expedition_id, person_id),
        )
        conn.commit()
        print("Person added to expedition.")
    except mysql.connector.IntegrityError as err:
        conn.rollback()
        if err.errno == 1062:
            print("That person is already on that expedition.")
        else:
            print("Couldn't add them. Check that both IDs exist.")
    finally:
        cursor.close()   


def remove_person_from_expedition(conn):
    print_people(conn)
    person_id = input("\nEnter a person ID: ").strip()
    print_expeditions(conn)
    expedition_id = input("\nEnter an expedition ID: ").strip()

    cursor = conn.cursor()
    cursor.execute(
        """
        DELETE FROM expedition_person
        WHERE expedition_id = %s AND person_id = %s
        """,
        (expedition_id, person_id),
    )
    conn.commit()

    if cursor.rowcount == 0:
        print("Nothing removed. That person wasn't on that expedition.")
    else:
        print("Person removed from expedition.")
    cursor.close()


def main():
    conn = get_connection()
    try:
        while True:
            print(MENU)
            choice = input("Choose an option: ").strip().lower()
            if choice == "1":
                print_people(conn)
            elif choice == "2":
                print_expeditions(conn)
            elif choice == "3":
                print_person_expeditions(conn)
            elif choice == "4":
                print_expedition_people(conn)
            elif choice == "5":
                add_person_to_expedition(conn)
            elif choice == "6":
                remove_person_from_expedition(conn)
            elif choice == "q":
                print("Goodbye.")
                break
            else:
                print("Not a valid option.")
            input("\nPress Enter to continue...")
    finally:
        conn.close()

if __name__ == "__main__":
    main()