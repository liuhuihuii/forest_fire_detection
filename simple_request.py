import requests
import json

keras_rest_api_url = "http://127.0.0.1:8888/predict"
x1 = 212
x2 = 12
payload = {"number1":x1,
           "number2":x2}
DIGITS = 3
MAXLEN = 2*DIGITS + 1
#submit request
r = requests.post(keras_rest_api_url, payload)
js = json.loads(r.text)
print(js)
q = '{}+{}'.format(x1, x2)
q+= ' '*(MAXLEN-len(q))
correct = str(x1 + x2)
correct += ' '*(DIGITS+1-len(correct))
class colors:
    ok = '\033[92m'
    fail = '\033[91m'
    close = '\033[0m'
if js["Success"]:
    guess= js["prediction"]
    print('Q', q, end=' ')
    print('T', correct, end=' ')
    if correct == guess:
        print(colors.ok + '☑' + colors.close, end=' ')
    else:
        print(colors.fail + '☒' + colors.close, end=' ')