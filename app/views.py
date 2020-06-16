from flask import render_template
from flask import request, redirect
from app import app


@app.route("/",methods=['POST','GET'])
def index():
	if request.method == "POST":

		req = request.form
		text=req["noticia"]
		print(text)

		return render_template("public/index.html",text=text)
		
	return render_template("public/index.html")

@app.route("/about")
def about():
	return render_template("public/about.html")