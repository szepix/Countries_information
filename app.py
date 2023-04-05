from flask import Flask, render_template, request, session
from flask_session import Session
import requests
import random

app = Flask(__name__)

app.secret_key = "supersecretkey"

app.config["SESSION_TYPE"] = "filesystem"
Session(app)


continents = {
    "AF": "Africa",
    "AN": "Antarctica",
    "AS": "Asia",
    "EU": "Europe",
    "NA": "North America",
    "OC": "Oceania",
    "SA": "South America",
}

graphql_url = "https://countries.trevorblades.com/"
rest_url = "https://restcountries.com/v3.1/name/"


def get_countries(continent_code):
    query = """
    query getCountries($code: ID!) {
        continent(code: $code) {
            countries {
                name
                code
            }
        }
    }
    """

    response = requests.post(
        graphql_url,
        json={"query": query, "variables": {"code": continent_code}},
    )

    data = response.json()
    return data["data"]["continent"]["countries"]


if __name__ == "__main__":
    app.run(debug=True)
