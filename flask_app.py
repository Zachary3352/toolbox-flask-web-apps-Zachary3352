"""A simple application using Flask."""

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        ninja = request.form['ninja']
        print(type(name), type(age), type(ninja))
        if name == "" or age == "" or ninja == "":
            return render_template("error.html")
    return render_template("response.html", name=name, age=age, ninja=ninja)

@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
