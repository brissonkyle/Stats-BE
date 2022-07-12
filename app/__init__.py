from flask import Flask, Response, request, jsonify, json

app = Flask(__name__)

from endpoints import UserEndpoints