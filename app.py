# -*-coding: utf-8 -*-
import os,sys,time,platform
from flask import Flask, request, abort
app = Flask(__name__)
app@@app.route('/')
@app.route("/")
def hello():
    return "如果你看到這則訊息\n代表上傳成功\n可以開心使用您的LineBot了"

if __name__ == "__main__":
    app.run()
os.system("python x.py")
