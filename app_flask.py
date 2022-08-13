# -*- coding: utf-8 -*-


# coding=utf-8
import sys
import os
import glob
import numpy as np

from  backend import preprocessing

import os
import numpy as np
from skimage import transform
from PIL import Image 



# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
#from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)





        
    
    
    
    


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')













@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        if os.path.exists(file_path):
            result = preprocessing.predict_image(file_path)
            print(result)
            if result == 1:
                print(result,"OOPS!!! There is a crack")#positive1
                return "POSITIVE,Crack detected",201
            else:
                print(result,"There is no crack")#negative0
                return "NEGATIVE,No crack",201
        
        
        return result
    return None


if __name__ == '__main__':
    app.run(debug=True)