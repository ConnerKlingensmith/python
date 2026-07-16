from flask import Flask, jsonify, request
import psutil
import subprocess
import json
import platform

app = Flask(__name__)

# In memory, lost on restart
network_data - []

@app.before_request
def log_request():
    print("Method: ", request.method)
    print("Path: ", request.path)
    print("Time: ", request.time)

@app.route

