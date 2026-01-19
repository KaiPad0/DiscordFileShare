import sys
import os
from flask import Flask,request,send_from_directory,render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/files/<path:filename>")
def send_file(filename):
    return send_from_directory("files", filename)

@app.route('/upload', methods=['GET'])
def upload_page():
    return render_template('upload.html')
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "ファイルがありません", 400
    
    file = request.files['file']
    if file.filename == '':
        return "ファイルが選択されていません", 400
    if file:
        dt = datetime.now()
        final_filename = f"{dt.strftime("%Y%m%d%H%M%S")}.mp4"
        final_path = os.path.join("files", final_filename)
        file.save(final_path)
        file_url = f"http://{request.host}/files/{final_filename}"
        return f"アップロード成功！<br>URL: <a href='{file_url}'>{file_url}</a>"
    
        
if __name__=="__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)