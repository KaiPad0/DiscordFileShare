import sys
from flask import Flask,request,send_from_directory

app = Flask(__name__)

@app.route("/files/<path:filename>")
def infex(filename):
    return send_from_directory("files", filename)

if __name__=="__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)