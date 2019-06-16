from flask import Flask, requst
import flask
import os
import numpy as np
app = Flask(__name__)


@app.route('/photo', methods=["post"])
def get_frame():
    # 接收图片
    upload_file = request.files['file']
    # 获取图片名
    file_name = upload_file.filename
    # 文件保存目录（桌面）
    file_path = r'C:/Users/Administrator/Desktop/'
    if upload_file:
        # 地址拼接
        file_paths = os.path.join(file_path, file_name)
        # 保存接收的图片到桌面
        upload_file.save(file_paths)
        # 随便打开一张其他图片作为结果返回，
        with open(r'C:/Users/Administrator/Desktop/1001.jpg', 'rb') as f:
            res = base64.b64encode(f.read())
            return res

if __name__ == "__main__":
    app.run()