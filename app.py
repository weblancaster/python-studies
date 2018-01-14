"""
Main flask app
"""
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

STORES = [
    {
        "name": "Nike town San Francisco",
        "items": [
            {
                "name": "Metcon 3",
                "price": 130
            }
        ]
    }
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/store")
def get_stores():
    return jsonify({
        "data": STORES
    })

@app.route("/store", methods=["POST"])
def create_store():
    body = request.get_json()
    new_store = {
        "name": body["name"],
        "items": []
    }
    STORES.append(new_store)

    return jsonify({
        "data": STORES
    })

@app.route("/store/<string:name>")
def get_store_by_name(name):
    formatted_name = name.replace("-", " ")
    store = [store for store in STORES if store["name"] == formatted_name]

    if not store:
        return jsonify({
            "message": "Store {} not found".format(formatted_name)
        })

    return jsonify({
        "data": store
    })

@app.route("/store/<string:name>/item")
def get_store_items_by_name(name):
    formatted_name = name.replace("-", " ")
    items = [store["items"] for store in STORES if store["name"] == formatted_name]

    if not items:
        return jsonify({
            "message": "Store {} not found".format(formatted_name)
        })
    
    return jsonify({
        "data": items[0]
    })

@app.route("/store/<string:name>/item", methods=["POST"])
def create_store_item_by_name(name):
    new_item = request.get_json()
    formatted_name = name.replace("-", " ")
    store = [store for store in STORES if store["name"] == formatted_name]

    if not store:
        return jsonify({
            "message": "Store {} not found".format(formatted_name)
        })
    
    store[0]["items"].append(new_item)

    return jsonify({
        "data": store
    })

app.run(port=5000)