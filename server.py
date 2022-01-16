from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'just@test'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/count', methods=['POST'])
def count():
    print("got this far")


if __name__=="__main__":
    app.run(debug=True)