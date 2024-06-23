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

@app.route('/users/<int:id>')
def get_user(id):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
        user = cursor.fetchone()
        cursor.close()
        connection.close()
        
        if user:
            return render_template('user_details.html', user=user)
        else:
            return "User not found", 404
    except Error as e:
        print(f"Error: {e}")
        return "There was an issue retrieving the user details."

if __name__ == '__main__':
    app.run(debug=True)
