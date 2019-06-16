from __future__ import print_function
from flask import Flask, request
import flask
import os
import tensorflow as tf
from keras.models import Sequential
from keras.datasets import mnist
from keras import layers
import numpy as np
from keras.models import load_model
from six.moves import range
from PIL import Image

app = Flask(__name__)

def loadmodel():
    print('start load model')
    global model
    model_dir = 'firstimplementation-adadelta.h5'
    #model_dir = 'test.h5'
    if os.path.exists(model_dir):
        print('yes it is')
        model = load_model(model_dir)
    else:
        print('it doesnt')
    global graph
    graph = tf.get_default_graph()

def forest_test(datapath, model):
    img_width = 200
    img_height = 200
    X = np.zeros((1, 200, 200, 3))
    img = Image.open(datapath)
    imgarray = np.array(img)
    imgarray = np.resize(imgarray, (200,200,3))
    X[0]= imgarray
    X[0]/=255
    with graph.as_default():
        preds = model.predict(X)
    print(preds[0][0])
    if preds[0][0]<0.5:
        return "Fire"
    else:
        return "No Fire"
@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    return flask.render_template("ajax_upload.html")

@app.route('/photo', methods=['GET', 'POST'])
def photo():
    data = dict()
    img = request.files.get('file')
    path = "static/photo/"
    file_path = path + img.filename
    img.save(file_path)
    data["prediction"] = forest_test(file_path, model)
    file_url = "/static/photo/" + img.filename
    data["url"] = file_url
    #print(file_path)
    print(data)
    return flask.jsonify(data)

print("start server")
loadmodel()
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8888)
