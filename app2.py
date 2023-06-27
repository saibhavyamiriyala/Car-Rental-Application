from flask import Flask, render_template, request,url_for,redirect
import mysql.connector
app = Flask(__name__)

# Configure MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Dhanu@1265884",
    database="car_rental"
)
cursor = db.cursor()

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for handling the car rental form submission
@app.route('/rent', methods=['POST','GET'])
def rent():
    # Get form data
    car_name = request.form['car_name']
    customer_name = request.form['customer_name']
    rental_days = request.form['rental_days']
    cursor=db.cursor()
    cursor.execute("INSERT INTO rentals (car_name, customer_name, rental_days) VALUES (%s, %s, %s)",(car_name, customer_name, rental_days))
    db.commit()
    return redirect(url_for('view'))
@app.route('/view')
def view():
    cursor=db.cursor(buffered=True)
    cursor.execute('select car_Name,customer_name, rental_days  from  rentals')
    data=cursor.fetchall()
    cursor.close()
    return render_template('index.html',data=data)
app.run(debug=True,use_reloader=True)