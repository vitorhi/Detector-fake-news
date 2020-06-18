import numpy as np
from joblib import load

def detector_predict(news):
	model=load("app/model/model.pkl")
	result=model.predict([news])
	if result==1:
		# Not Fake news
		return "Verdadeira"
	else:
		# Fake News
		return "Falsa"
