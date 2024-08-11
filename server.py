# server.py

from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/runcode')
def run_code():
    script_name = request.args.get('script')
    if script_name:
        try:
            subprocess.run(['python', script_name], check=True)
            return '', 200
        except subprocess.CalledProcessError:
            return '', 500
    else:
        return '', 400

if __name__ == '__main__':
    app.run(debug=True)
