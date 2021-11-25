from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/", methods=['GET'])
def login():
    return render_template('login.html')

@app.route("/register", methods=['GET'])
def register():
    return render_template('registration.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)