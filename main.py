import os
import random
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='./images')

# 设置图片目录
IMAGE_DIR = 'images'

@app.route('/')
def random_image():
    # 获取图片目录下所有文件
    images = os.listdir(IMAGE_DIR)

    # 随机选择一张图片
    selected_image = random.choice(images)

    # 返回选定的图片
    return send_from_directory(IMAGE_DIR, selected_image)

if __name__ == '__main__':
    app.run(debug=True)
