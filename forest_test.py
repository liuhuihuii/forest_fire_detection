from __future__ import print_function
from keras.models import Sequential
from keras.datasets import mnist
from keras import layers
import numpy as np
from keras.models import load_model
from six.moves import range
from PIL import Image
from keras import backend as K
from keras.preprocessing.image import ImageDataGenerator


img_width = 200
img_height = 200
datapath = ["data/validation/Fire/fire-9033.49143155.png","data/validation/No Fire/forrest-9432.18298017.png","data/validation/No Fire/forrest-9245.16899239.png"]
model = load_model("firstimplementation-adadelta.h5")
X = np.zeros((3, 200, 200, 3))
for i, file in enumerate(datapath):
  img = Image.open(file)
  imgarray = np.array(img)
  imgarray = np.resize(imgarray, (200,200,3))
  X[i]= imgarray
  X[i]/=255
preds = model.predict(X)
<<<<<<< HEAD
print(preds)
print(preds.shape)
print(res)
=======
print(preds)
>>>>>>> c9021fd45c5bbc179b389bd23eb9e94f49b82198
