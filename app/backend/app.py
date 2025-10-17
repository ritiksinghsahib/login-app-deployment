
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return jsonify({'success': bool(user)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
