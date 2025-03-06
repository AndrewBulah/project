from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os

app = Flask(__name__)

db_config = {
    "host": os.getenv("DB_HOST", "192.168.56.101"),
    "user": os.getenv("DB_USER", "drupal_user"),
    "password": os.getenv("DB_PASSWORD", "drupal_pass"),
    "database": os.getenv("DB_NAME", "drupal_db"),
    "port": 3306
}

@app.route('/')
def index():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        return render_template('index.html', users=users)
    except Exception as e:
        return f"Ошибка: {str(e)}", 500

@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['username']
        email = request.form['email']
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, email) VALUES (%s, %s)", (name, email))
            conn.commit()
            return redirect(url_for('index'))
        except Exception as e:
            return f"Ошибка при добавлении: {str(e)}", 500
    return render_template('add.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
