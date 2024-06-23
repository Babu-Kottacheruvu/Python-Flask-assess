from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error


app = Flask(__name__)


# MySQL configurations
db_config = {
    'user': 'root',
    'password': 'KBABU0307',
    'host': 'localhost',
    'database': 'userdb'
}


@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        user_details = request.form
        name = user_details['name']
        email = user_details['email']
       
        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()
            cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
            connection.commit()
            cursor.close()
            connection.close()
        except Error as e:
            print(f"Error: {e}")
            return "There was an issue adding the user to the database."
       
        return redirect(url_for('success'))
    return render_template('new_user.html')


@app.route('/success')
def success():
    return "User added successfully!"


if __name__ == '__main__':
    app.run(debug=True)
