from flask import Flask, redirect
import json
import requests
import os

with open(os.path.dirname(os.path.realpath(__file__)) + '/config.json', 'r') as f:
    config = json.load(f)

# Define where to redirect by default
DEFAULT_URL = config['DEFAULT_URL']
# Google Sheet
SHEET_ID = config['SHEET_ID']
DB_URL = ('https://docs.google.com/spreadsheets/d/{0}/export'
          '?format=csv&id={0}&gid=0').format(SHEET_ID)

app = Flask(__name__)


def look_up_long_url(path):
    try:
        csv = requests.get(DB_URL).text
        mappings = dict(mapping.split(',') for mapping in csv.split('\r\n'))
        result = mappings[path]
    except:  # catch all exceptions
        result = None

    return result


@app.route("/")
def home():
    if config['SHOW_HOME_PAGE'] is True:
        return "<h1>It works!</h1>"
    else:
        return redirect(DEFAULT_URL)


@app.route('/<path>')
def handler(path):
    url = look_up_long_url(path)
    if url is None:
        return redirect(DEFAULT_URL)
    else:
        return redirect(url)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    if port == 5000:
        app.debug = True
    app.run(host='0.0.0.0', port=port)