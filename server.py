from flask import Flask ,redirect, render_template, request, url_for
import mysql.connector
from database import createDB, createTable, fetchData

app = Flask(__name__, static_url_path='/static')

charity = ["Safe Chennai Orphanage,Adayar", "Child safe Orphanage,Avadi", "Elder Orphanage,Villivakkam", "Amirtha Orphanage,Redhills", "Nanda Orphanage,Ambattur", "Cauvery charity trust,Adayar", "Hari trust,Korattur", "Radha Elder Orphanage,OMR"]
quantity = ["Less than 20 people","25-50 people","50-100 people","100-200 people","200-300 people","300-400 people","400-500 people","500 above"]
transport = ["Delivery Van", "Car", "Bulk Carriers", "Cargo Vans", "Box Trucks", "Motorcycles", "Tanker Trucks"]

dbCheck = createDB()
tableCheck = createTable()
cursor = None

print("Database and Table check successful")
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="NGO"
)
cursor = db.cursor()

@app.route('/') # Homepage - index.html
def home():
    return render_template('index.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/donate')
def donate():
    results = fetchData()
    return render_template('fooddonate.html', results=results)

@app.route('/submit', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        form_data = request.form

        orgName = form_data['orgname']
        personName = form_data['personname']
        contactNumber = form_data['contact']
        email = form_data['email']
        foodQuantity = quantity[int(form_data['food-quantity'])]
        charityName = charity[int(form_data['charity-name'])]
        transportRequired = transport[int(form_data['transport-required'])]
        ngoMember = form_data['ngomember']
        
        query = "INSERT INTO DONATIONS (PERSON_NAME, ORGANIZATION, CONTACT, EMAIL, FOOD_QUANTITY, CHARITY_NAME, TRANSPORT, NGO_MEMBER) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (personName, orgName, contactNumber, email, foodQuantity, charityName, transportRequired, ngoMember)

        cursor.execute(query, values)
        db.commit()
        
        print(f'DATA STORED: {orgName} {personName} {contactNumber} {email} {foodQuantity} {charityName} {transportRequired} {ngoMember}')
        
    return redirect(url_for('donate'))

if __name__ == "__main__":
    app.run()
