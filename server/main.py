"""
Day 16
Flask and Flask-RESTful
"""
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

countries = [
    {
        "name": "Brazil",
        "population": "207.7 million"
    }
]

class Country(Resource):
    def get(self, name):
        country = [country for country in countries if country["name"].lower() == name.lower()]

        return country[0]
    
    def post(self, name):
        countries.append({
            "name": name,
            "population": "Unknown"
        })

        return countries


# localhost:5000/country/jamaica
api.add_resource(Country, "/country/<string:name>")

app.run(port=5000)
