import flask
from flask import Flask, render_template,  request, redirect, g, send_file
from flask.helpers import url_for
app = flask.Flask(__name__)




@app.route('/')
def nighthawk():
    return render_template("WEB.html")

if __name__ == '__main__':
    app.debug = True
    app.run()






