from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# Конфигурация MySQL
app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_USER'] = 'user'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'mydb'

mysql = MySQL(app)

@app.route('/add', methods=['POST'])
def add():
    data = request.json
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO users(name, age) VALUES(%s, %s)", (data['name'], data['age']))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'User added'}), 201

@app.route('/users', methods=['GET'])
def users():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    cursor.close()
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
