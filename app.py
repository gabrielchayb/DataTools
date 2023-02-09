from flask import Flask, render_template, request, jsonify, json, redirect, make_response, send_file
import json
from sidemodules.databasehandler import send_data, get_data
import webbrowser
from datetime import datetime
app = Flask(__name__)


@app.route('/')
@app.route("/home")
def home():
    return render_template('home.html')


if __name__== "__main__":
    app.run(debug=True)


