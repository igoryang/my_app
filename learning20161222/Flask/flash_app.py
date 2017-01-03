#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#author = 'igor'
from flask import Flask
app = Flask(__name__)

@ app.route('/')
def index():
    #print("hello world!")
    return ("hello world!<h1>hello world!</h1>")


if __name__ == "__main__":
    app.run(debug=True,port=8009)