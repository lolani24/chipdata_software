from flask import Flask, render_template 

#create a Flask Instance 
app = Flask(__name__)

#create a route decorator (creating the url)
@app.route('/') #homepage

def index():
    first_name = "Max"
    stuff = "This is bold text"

    favorite_pizza = ["pepperoni", "cheese", "mushrooms", 41]
    return render_template("index.html", first_name=first_name, stuff=stuff, favorite_pizza=favorite_pizza)

#localhost:5000.user/leilani
@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name=name)

#common functions for jinja
#safe = 
#capitalize 
#lower
#upper
#title
#trim
#striptags  

#create Custom Error Pages 

#Invalid URL 

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500