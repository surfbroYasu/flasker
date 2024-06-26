from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    greeting_message = "My name is Yasu. Nice to meet you!!!"
    favorite_fruits = ['pinapples', 'mangos', 'peaches']
    return render_template("index.html", 
                          message = greeting_message, 
                          fruits = favorite_fruits
                          
                          )
  
@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)
  
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
  
  
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500