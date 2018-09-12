from flask import Flask, flash, redirect, render_template, request, session, abort
 
app = Flask(__name__)
 
@app.route("/")
def index():
    return render_template('index.html');
 
@app.route("/hello/<string:name>/")
def hello(name):
    return render_template(
        'index.html',name=name)
 
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)