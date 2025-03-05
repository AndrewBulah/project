from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Конфигурация БД (будет заменена через Kubernetes Secrets)
db_config = {
    "host": os.getenv("DB_HOST", "node2"),  # Из переменных окружения
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
        result = cursor.fetchall()
        return jsonify({"users": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
