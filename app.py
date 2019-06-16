from flask import Flask, request

import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    return "yes"



print("start server")
app.run()
