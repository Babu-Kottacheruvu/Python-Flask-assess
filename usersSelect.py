from flask import *
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

#Database Setup

db_setup={
    'user':'root',
    'password':'KBABU0307',
    'host':'localhost',
    'database':'userdb'
}

@app.route('/users')
def listOfUsers():
    try:
        connection=mysql.connector.connect(**db_setup)
        if connection.is_connected():
            cursour=connection.cursor()
            cursour.execute("SELECT id, name, email FROM users")
            users=cursour.fetchall()
            cursour.close()
            connection.close()
            return render_template('users.html',users=users)
        else:
            flash('Database Connection Failed')
            return "error : Database connection failed"
    except Error as e:
        flash(f"Error :{e}")
        return "Error as occured.."
if __name__ == '__main__':
    app.run(debug=True)