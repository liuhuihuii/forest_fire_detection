from __future__ import print_function
from flask import Flask, request
import flask
import os
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
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
    model_dir = 'firstimplementation-adadelta.h5' ##0.92 ##test.h5 .94
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
    datadir = datapath
    # only rescaling
    test_datagen = ImageDataGenerator(rescale=1. / 255)
    validation_generator = test_datagen.flow_from_directory(
        datadir,
        target_size=(img_width, img_height),
        batch_size=1,
        class_mode='binary')
    with graph.as_default():
        preds = model.predict_generator(validation_generator, steps=1)
    print(preds[0])
    if preds[0]<0.6:   ##Fire:0; not Fire:1
        return "Fire"
    else:
        return "No Fire"

@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    return flask.render_template("render.html")

@app.route('/photo', methods=['GET', 'POST'])
def photo():
    data = dict()
    img = request.files.get('file')
    path = "static/photo/"
    for i in os.listdir(path):
        path_file = os.path.join(path, i)
        if os.path.isfile(path_file):
            os.remove(path_file)
    file_path = path + img.filename
    datapath = "static"
    img.save(file_path)
    data["prediction"] = forest_test(datapath, model)
    file_url = "/static/photo/" + img.filename
    data["url"] = file_url
    print(file_path)
    print(data)
    return flask.jsonify(data)

print("start server")
loadmodel()
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8888)