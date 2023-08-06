from flask import Flask, render_template, request, Response
from objectdetection.objectdetect import *
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route('/')
def upload_file():
   return render_template('upload.html')
	
@app.route('/upload', methods = ['GET', 'POST'])
def upload():
   global filename
   if request.method == 'POST':
      f = request.files['file']
      filename = f.filename
      path = os.path.join("uploads", f.filename)
      print(path)
      data_json = request.form.get("file")
      print(data_json)
      f.save(path)
      print(f.filename)
      return render_template('playvideo.html')


@app.route('/UploadVideo')
def UploadVideo():
    return Response(ShowVideo(filename), mimetype='multipart/x-mixed-replace; boundary=frame')

		
if __name__ == '__main__':
   #app.run(debug = True)
   app.run(port=5003, debug=True)
