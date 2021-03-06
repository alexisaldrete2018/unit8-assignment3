
from crypt import methods
from flask import Flask
from about_me import me
from mock_data import catalog
import json

app = Flask('assignment2')

@app.route("/", methods=["GET"])
def home():
    return "This is the home page"

@app.route("/about")
def about():
    return (me["first"] +" "+ me["last"])

@app.route("/myaddress")
def address():
    return (me["address"]["street"] + " " + me["address"]["number"])


    ################## ENDPOINTS ##################

@app.route("/api/catalog", methods=["GET"])
def get_catalog():
    return json.dumps(catalog)

@app.route("/api/catalog/count", methods=["GET"])
def get_count():
    counts = len(catalog)
    return json.dumps(counts) 

@app.route("/api/catalog/<id>", methods=["GET"])
def get_product(id):

    return id

app.run(debug=True)