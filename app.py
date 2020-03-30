import os
import urllib
from io import BytesIO
from fastai import *
from fastai.vision import *
from fastai.vision.data import *
from flask import Flask,request,redirect,url_for,render_template,flash
from werkzeug.utils import secure_filename

import json, requests
import os, base64
import urllib

import sys
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")
    

def preprocess(url):
    Image = requests.get(url)
    with open("test.jpg","wb") as f:
        f.write(Image.content)
    with open("test.jpg", mode='rb') as file:
        test = file.read()

    data = str(base64.b64encode(test), encoding='utf-8')  
    input_data = json.dumps({'data': data})
    return input_data

   
def run(raw_data):
    base64_string = json.loads(raw_data)['data']
    base64_bytes = base64.b64decode(base64_string)
    with open(os.path.join(os.getcwd(),"score.jpg"), 'wb') as f:
        f.write(base64_bytes)
    
    # make prediction
    path = Path(os.getcwd())
    learn = load_learner(path)
    img = open_image(os.path.join(os.getcwd(),"score.jpg"))
    result = learn.predict(img)
    return json.dumps({'category':str(result[0]), 'confidence':result[2].data[1].item()})


# create the application project 
app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')

@app.route("/predict", methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        
        # Make prediction
        url = "http://192.168.0.23:8080/shot.jpg"
        input_data = preprocess(url)
        preds = run(input_data)
        return preds
    return None

if __name__=='__main__':
     app.run(debug=True, port=8080, host='0.0.0.0')