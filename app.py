#create a simple flask application
from flask import Flask,render_template,request,redirect,url_for

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
    #return redirect(url_for("index"))
    return render_template("index.html")
    
@app.route('/success/<int:score>')
def success(score):
    return "The person has passed and the score is  " + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and the score is " + str(score)

@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method=='GET':
        return render_template("calculate.html")
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])
        average_marks=(maths+science+history)/3
     #return render_template('calculate.html',results=average_marks)
#redirect to app route success and failure
        result=""
        if average_marks>=50:
            result="success" 
        else:        
            result="fail"
            
       # return redirect(url_for(result,score=average_marks))
    #use render_template when you want to redirect to the html page
    #use redirect when you want to redirect directly to the page
            
#@app.route('/calculatemarks')
#def calculatemarks():
    return render_template("result.html",results=average_marks)
    

if __name__=='__main__': #entry points of the app and then run the app, app.run() is the method
    app.run(debug=True)


    