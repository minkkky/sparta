from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def upload_file():
    return render_template('index.html')

@app.route('/uploader', methods=['GET','POST'])
def uploader_file():
    if request.method=='POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return '업로드 완료!'

if __name__ == '__main__':
    app.debug = True
    app.run()