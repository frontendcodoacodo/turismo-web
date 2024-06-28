from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'turismo_db1'
mysql = MySQL(app)


# Ruta para obtener datos
@app.route('/data', methods=['GET'])
def get_data():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM comidas')
    data = cur.fetchall()
    cur.close()
    return jsonify(data)
    
if __name__ == '__main__':
    app.run(debug=True)   