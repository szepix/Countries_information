import random

import requests
from flask import Flask, render_template, request, session

from flask_session import Session

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


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        continent_code = request.form.get("continent")
        num_countries = int(request.form.get("num_countries"))

        country_data = get_countries(continent_code)
        random_countries = random.sample(country_data, num_countries)
        country_details = [get_country_details(country) for country in random_countries]

        session["country_details"] = country_details
        return render_template("index.html", continents=continents, country_details=country_details)
    else:
        session.pop("country_details", None)
        return render_template("index.html", continents=continents)


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


def get_country_details(country):
    response = requests.get(rest_url + country["name"])
    data = response.json()[0]
    return {
        "name": data["name"]["common"],
        "capital": data["capital"][0],
        "population": data["population"],
        "currency": list(data["currencies"].keys())[0],
        "subregion": data["subregion"],
        "languages": ", ".join(data["languages"].values()),
    }


if __name__ == "__main__":
    app.run(debug=True)
