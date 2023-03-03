from flask import Flask, render_template, request, flash

app = Flask(__name__) # creates a class for our app
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/hello")
def index():
	flash("what's your name?")
	return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"]) # Methods are specified here because we are interacting with the server when we click greet
def greet():
	flash("Hi " + str(request.form['name_input']) + ", great to see you!")
	return render_template("index.html")
