from flask import Flask, render_template, request
import subprocess
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/')
def alive():
	return 'OK'

@app.route('/upload')
def upload_file():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      if f.filename != "subtract.py": return render_template('error.html')
      f.save(secure_filename(f.filename))
      return grade().replace('\n', '<br>').replace('\t', '&emsp;')

def grade():
	num_correct = subprocess.call("./execute_submission_and_assess_output.sh", shell=True)
	str = ""
	str += "<center>Score: {0} out of 2 correct.\n\n".format(num_correct)
	str += "*************Original submission*************\n\n"
	with open("subtract.py", "r") as ret:
		for line in ret:
			str += line
	return str + "</center>"


if __name__ == '__main__':
   app.run(debug = True,host="0.0.0.0")
