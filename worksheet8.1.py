#Muhammad Azizi Mohd Ariffin
#mazizi@fskm.uitm.edu.my

from flask import Flask
app = Flask(__name__)

@app.route("/")
def index() :
    return "<h2> Welcome to Python Crash Course!</h2>"

@app.route("/bmi/<weight>/<height>")
def checkBmi(weight,height) :
    weight = float(weight)
    height = float(height)
    bmi = round(weight / (height * height), 1)
    if bmi < 18.5 :
        return('You are underweight')
    elif bmi >= 18.5 and bmi < 25.0 :
        return('Your weight is desirable')
    elif bmi >= 25.0 and bmi < 30: 
        return('You are overweight')
    else :
        return('You are obese')

if __name__ == "__main__" :
    app.run(ssl_context='adhoc', port=443)
    
    