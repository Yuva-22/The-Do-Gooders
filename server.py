from flask import Flask ,redirect, render_template, request, url_for

app = Flask(__name__, static_url_path='/static')

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
    return render_template('fooddonate.html')

if __name__ == "__main__":
    app.run()