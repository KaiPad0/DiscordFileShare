import sys
from flask import Flask,request,send_from_directory

app = Flask(__name__)

@app.route("/")
def infex():
    return send_from_directory("files", "aaa.mov")

if __name__=="__main__":
    app.run()