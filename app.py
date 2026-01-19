import os
import requests
from flask import Flask,request,send_from_directory,render_template,jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/files/<path:filename>")
def send_file(filename):
    return send_from_directory("files", filename)

@app.route('/upload', methods=['GET'])
def upload_page():
    webhook_url = request.args.get('webhook')
    user_id = request.args.get('userid')
    return render_template('upload.html', webhook=webhook_url, userid=user_id)
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "ファイルがありません", 400
    
    file = request.files['file']
    user_id = request.form.get('userid')
    webhook_url = request.form.get('webhook')

    if file.filename == '':
        return "ファイルが選択されていません", 400
    if file:
        dt = datetime.now()
        final_filename = f"{dt.strftime("%Y%m%d%H%M%S")}.mov"
        final_path = os.path.join("files", final_filename)
        file.save(final_path)
        file_url = f"http://{request.host}/files/{final_filename}"

        if webhook_url:
            payload = {"content": f"Uploaded by <@{user_id}>!\n{file_url}"}
            requests.post(webhook_url, json=payload)

        return jsonify({
            'message': 'Upload successful',
            'url': file_url,
            'original_name': file.filename
        })
    
        
if __name__=="__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)