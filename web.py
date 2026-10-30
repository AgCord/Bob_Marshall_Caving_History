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


from flask import Flask, render_template, request 



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
    cursor.execute("SELECT first_name, last_name, role, years_active FROM person ORDER BY person_id;")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('person.html', first_name=first_name, last_name=last_name, role=role, years_active=years_active, rows=rows)

@WebApp.route('/addperson')
def addperson():

    return render_template('form.html')

if __name__ == '__main__':
    WebApp.run(port=8000, debug=True, host="0.0.0.0")