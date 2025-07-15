# app.py
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        return f'Hello, {name}! Your password is: {password}'
    return '''
        <form method="post">
            Name: <input type="text" name="name"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0')