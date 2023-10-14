from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

@app.route('/index')
def index():
    return render_template('index.html', password=None)

@app.route('/generate', methods=['POST'])
def generate():
    length = int(request.form['length'])
    password = generate_password(length)
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
