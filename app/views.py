from flask import render_template
from flask import request, redirect
from app import app
from app import model
import numpy as np
from joblib import load



@app.route("/",methods=['POST','GET'])
def index():
	if request.method == "POST":

		req = request.form
		text=req["noticia"]
		resultado=model.detector_predict(text)


		return render_template("public/index.html",resultado=resultado, text=text)
		
	return render_template("public/index.html")

@app.route("/about")
def about():
	return render_template("public/about.html")