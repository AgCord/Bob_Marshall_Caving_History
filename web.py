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


from flask import Flask, render_template, request, redirect 



WebApp = Flask(__name__)


@WebApp.route('/')
def default():
    return 'Flask is working.'

@WebApp.route('/person')
def person():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    role = request.args.get('role')
    years_active = request.args.get('years_active')
    conn = get_connection()
    cursor = conn.cursor()
    if first_name:
        cursor.execute(
            "INSERT INTO person (first_name, last_name, role, years_active) VALUES (%s, %s, %s, %s);",
            (first_name, last_name, role, years_active),
        )
        conn.commit()
    elif request.args.get('delete') == 'true':
        delete_id = request.args.get('id')
        cursor.execute("DELETE FROM person WHERE person_id = %s;", (delete_id,))
        conn.commit()
    expedition_id = request.args.get('expedition_id')
    if expedition_id:
        cursor.execute("SELECT label FROM expedition WHERE expedition_id = %s;", (expedition_id,))
        label = cursor.fetchone()
        heading = f"People on the {label[0]}"
        cursor.execute(
            """
            SELECT p.first_name, p.last_name, p.role, p.years_active, p.person_id
            FROM person AS p
            JOIN expedition_person AS ep
              ON p.person_id = ep.person_id
            WHERE ep.expedition_id = %s
            ORDER BY p.last_name
            """,
            (expedition_id,),
        )
    else:
        cursor.execute("SELECT first_name, last_name, role, years_active, person_id FROM person ORDER BY person_id;")
        heading = "Person"
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('person.html', first_name=first_name, last_name=last_name, role=role, years_active=years_active, rows=rows, heading=heading)

@WebApp.route('/updateperson')
def updateperson():
    person_id = request.args.get('id')
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    role = request.args.get('role')
    years_active = request.args.get('years_active')
    conn = get_connection()
    cursor = conn.cursor()
    if first_name:
        cursor.execute("UPDATE person SET first_name = %s, last_name = %s, role = %s, years_active = %s WHERE person_id = %s;", (first_name, last_name, role, years_active, person_id))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/person')
    cursor.execute("SELECT first_name, last_name, role, years_active FROM person WHERE person_id = %s;", (person_id,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('update.html', id=person_id, first_name=row[0], last_name=row[1], role=row[2], years_active=row[3])

@WebApp.route('/expedition')
def expedition():
    person_id = request.args.get('person_id')
    conn = get_connection()
    cursor = conn.cursor()
    add_expedition_id = request.args.get('add_expedition_id')
    if person_id and add_expedition_id:
        cursor.execute(
            "INSERT INTO expedition_person (expedition_id, person_id) VALUES (%s, %s);",
            (add_expedition_id, person_id),
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(f'/expedition?person_id={person_id}')
    if person_id:
        cursor.execute("SELECT first_name, last_name FROM person WHERE person_id = %s;", (person_id,))
        name = cursor.fetchone()
        heading = f"Expeditions for {name[0]} {name[1]}"
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
    else:
        cursor.execute("SELECT expedition_id, year, label FROM expedition ORDER BY year;")
        heading = "All expeditions"
    rows = cursor.fetchall()
    others = None
    if person_id:
        cursor.execute(
            """
            SELECT expedition_id, year, label
            FROM expedition
            WHERE expedition_id NOT IN (
                SELECT expedition_id
                FROM expedition_person
                WHERE person_id = %s
            )
            ORDER BY year
            """,
            (person_id,),
        )
        others = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('expedition.html', rows=rows, heading=heading, others=others, person_id=person_id)

@WebApp.route('/addperson')
def addperson():

    return render_template('form.html')

if __name__ == '__main__':
    WebApp.run(port=8000, debug=True, host="0.0.0.0")