import pickle
import numpy as np
from flask import Flask,request,render_template

app=Flask(__name__)

with open('model.pkcls', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template("index.html",pred="")

@app.route('/predict',methods=['POST','GET'])
def click():
    x=request.form['X']
    
    X_test = np.array([[int(x)]])

    predictions = model.predict(X_test)
    predictions=int(predictions[0])
    res="Predicted res is "+str(predictions)
    return render_template("index.html",pred=res)

if __name__=="__main__":
    app.run()

