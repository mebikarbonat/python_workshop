#Muhammad Azizi Mohd Ariffin
#mazizi@fskm.uitm.edu.my

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index() :
    return render_template('index.html')

@app.route("/about-us")
def about() :
    return render_template('about.html')

@app.route("/redeem/<code>")
def redeem(code) :
    return render_template('redeem.html', voucher = code)

if __name__ == "__main__" :
    app.run(ssl_context='adhoc', port=443)
    
    