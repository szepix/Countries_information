# Country Information App

This web application allows users to fetch information about countries located in a given continent. Users can specify the number of countries they would like to display, and the app will fetch and display random countries based on the user's input.

## Features

- Select a continent from a pre-defined list
- Specify the number of countries to display (between 2 and 10)
- Fetch country information, including official name, capital, population, currency, subregion, and languages
- Display results in an easy-to-read format, ordered alphabetically by country name

## Requirements

- Python 3.6+
- Flask
- Requests

## Installation

1. Clone the repository or download the source code:

git clone https://github.com/yourusername/country-information-app.git

bash
Copy code

2. Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```
3. Install the required packages:
```bash
pip install -r requirements.txt
```
## Usage
Set the environment variable for Flask:
```bash
Copy code
export FLASK_APP=app.py
Run the Flask application:
flask run
```
Open your web browser and navigate to http://127.0.0.1:5000/ to access the application.