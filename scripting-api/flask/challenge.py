from flask import Flask, jsonify, request
import psutil
import subprocess
import json
import platform

app = Flask(__name__)



