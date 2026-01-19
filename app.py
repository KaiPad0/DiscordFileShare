import sys
from flask import Flask,request,send_from_directory

app = Flask(__name__)

@app.route("/")
def infex():
    return send_from_directory("files", "IMG_4879.mov")

if __name__=="__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)