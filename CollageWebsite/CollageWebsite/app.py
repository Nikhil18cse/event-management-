print("Hello, running app.py...")
  # Explicitly print the server URL

# Your existing code follows here


from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)

@app.route('/')
def Home():
    return render_template('Home.html')

@app.route('/SignUp')
def SignUp():
    return render_template('SignUp.html')

@app.route('/SignUp', methods=['POST'])
def form():
    if request.method == 'POST':
        FirstName = request.form['FirstName']
        LastName = request.form['LastName']
        Location = request.form['Location']
        NewPassword = request.form['NewPassword']
        ConfirmPassword = request.form['ConfirmPassword']

        cursor = mysql.connection.cursor()
        cursor.execute(
            'INSERT INTO users (FirstName, LastName, Location, NewPassword, ConfirmPassword) VALUES (%s, %s, %s, %s, %s)',
            (FirstName, LastName, Location, NewPassword, ConfirmPassword)
        )

        mysql.connection.commit()
        cursor.close()
        return render_template('LogIn.html')

@app.route('/LogIn')
def LogIn():
    return render_template('LogIn.html')

@app.route('/LogIn', methods=['POST'])
def form2():
    if request.method == 'POST':
        UserName = request.form['UserName']
        Password = request.form['Password']
        cursor = mysql.connection.cursor()
        query = "SELECT * FROM users where FirstName = %s and NewPassword = %s"
        cursor.execute(query, (UserName, Password))

        result = cursor.fetchone()
        cursor
