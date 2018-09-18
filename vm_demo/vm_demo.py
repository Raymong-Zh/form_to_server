from flask import Flask, request, render_template
import os
import json
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def signin_form():
	return render_template('form.html')

@app.route('/', methods=['POST'])
def signin():
	items = request.form
	with open("record.json","w") as f:
		json.dump(items,f)
	cmd = "rename record.json record_new.json"
	os.system(cmd)
	return render_template('form.html', message='Query OK')
if __name__=='__main__':
	app.run(host='192.168.7.2',port=5500)