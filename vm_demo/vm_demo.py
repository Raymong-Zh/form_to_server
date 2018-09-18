from flask import Flask, request, render_template
import os
import json
from datetime import timedelta
app = Flask(__name__)


@app.route('/', methods = ['GET'])
def signin_form():
	return render_template('form.html')

@app.route('/', methods=['POST'])
def signin():
	items = request.form
	with open("data.json","w") as f:
		json.dump(items,f)
	cmd = "ansible-playbook -s /vmware/create_vm_linux.xml -e @data.json"
	os.system(cmd)
	return render_template('form.html', message='Query OK')
if __name__=='__main__':
	app.run(host='192.168.7.2',port=5500)