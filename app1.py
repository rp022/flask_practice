#create a simple flask application
from flask import Flask,render_template,redirect,url_for

##create the flask app
app=Flask(__name__) # app is the entry point of the particular program, creating flask app

@app.route('/')
def home():
    return "<h2>Hello WOrld</h2>"

@app.route('/welcome')
def welcome():
    return "Welcome to python tutorial"

@app.route('/index')
def index():
    #return "Welcome to python tutorial"
    return redirect(url_for("index"))
    #return render_template("index.html")

if __name__=='__main__': #entry points of the app and then run the app, app.run() is the method
    app.run(debug=True)


    