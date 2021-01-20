#!/usr/bin/python3
'''
Start A Flask with web application
'''
from models import storage
from models.state import State
from os import environ
from flask import Flask, render_template
app = Flask(__name__)



