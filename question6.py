#6. Build a Flask app that allows users to upload files and display them on the website.
from flask import Flask, render_template, request 
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/upload')  
def upload_file():
   return render_template('upload.html')

@app.route('/upload_post', methods = ['POST'])
def upload_post():
   if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'
   pass

if __name__ == '__main__':
    app.run(host="0.0.0.0")
