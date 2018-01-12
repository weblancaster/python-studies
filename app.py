from flask import Flask, jsonify

app = Flask(__name__)

stores = [
    {
        "name": "Nike town San Francisco",
        "items": [
            {
                "name": "Metcon 3",
                "price": 160
            }
        ]
    }
]

@app.route("/store")
def get_stores():
    return jsonify({
        "stores": stores
    })

@app.route("/store", methods=["POST"])
def create_store():
    pass

@app.route("/store/<string:name>")
def get_store_by_name(name):
    pass

@app.route("/store/<string:name>/item")
def get_store_item_by_name(name):
    pass

@app.route("/store/<string:name>/item", methods=["POST"])
def create_store_item_by_name(name):
    pass

app.run(port=5000)