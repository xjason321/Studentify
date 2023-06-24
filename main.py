"""
LING HACKS V - June 24th to 25th

Idea: Translate images of Sign Language to text
Description: Takes images of hands and returns. 

Coders: Jason Xie, Subhash Srinivasa, Komal Tummala
"""

from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
import json

app = Flask(__name__, static_folder='static')

if __name__ == '__main__':
    app.run()
