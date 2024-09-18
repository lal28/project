from flask import Flask
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    conn = mysql.connector.connect(
        host="db",
        database="mydb",
        user="myuser",
        password="mypassword"
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees;')
    employees = cursor.fetchall()
    cursor.close()
    conn.close()
    
    result = '<h1>Employees</h1>'
    result += '<ul>'
    for emp in employees:
        result += f'<li>{emp[1]} - {emp[2]}</li>'
    result += '</ul>'
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0')
