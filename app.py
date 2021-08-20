import requests
import datetime
from flask import jsonify, Flask, request
from flask_mysqldb import MySQL
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3305
app.config['MYSQL_USER'] = 'surer'
app.config['MYSQL_PASSWORD'] = 'surer'
app.config['MYSQL_DB'] = 'surer'
app.config['JWT_SECRET_KEY'] = 'surer'

mysql = MySQL(app)
jwt = JWTManager(app)


@app.route('/registration', methods=['POST'])
def registration():

    if not request.json:
        return("Invalid body request."), 400

    first_name = request.json['first_name']
    last_name = request.json['last_name']
    email = request.json['email']
    password = request.json['password']
    contact = ""
    if "contact" in request.json:
        contact = request.json['contact']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO Users(first_name, last_name, email, password, contact) VALUES (%s, %s, %s, %s, %s)",
                (first_name, last_name, email, password, contact))
    mysql.connection.commit()
    cur.close()

    return("Success"), 201


@app.route('/login', methods=['POST'])
def login():

    if not request.json:
        return("Invalid body request."), 400

    cur = mysql.connection.cursor()
    cur.execute(
        f"SELECT * FROM Users WHERE email = '{request.json['email']}' AND password = '{request.json['password']}'")
    result = cur.fetchall()

    if len(result) == 0:
        return("Invalid email or password"), 404

    access_token = create_access_token(identity=result[0][2])
    return jsonify(access_token=access_token), 200


@app.route('/member_details', methods=['GET'])
@jwt_required()
def member_details():

    current_user = get_jwt_identity()

    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM Users WHERE email = '{current_user}'")
    result = cur.fetchall()

    return jsonify(user=result[0]), 200


@app.route('/carpark_availability', methods=['GET'])
# @jwt_required()
def carpark_availability():

    paras = {"data_time": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")}
    response = requests.get(
        url="https://api.data.gov.sg/v1/transport/carpark-availability", data=paras)

    return jsonify(response.json()), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0')
