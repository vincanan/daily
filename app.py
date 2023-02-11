from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://<username>:<password>@cluster0.wpr6ivo.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta