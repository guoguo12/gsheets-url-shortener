from flask import Flask, redirect
import requests
import os

# Define where to redirect by default
DEFAULT_URL = 'https://www.google.com'

# Google Sheet
SHEET_ID = '1vr6C7CD_RMaNXmxFybG5H6GibrT1Vsx6Jm3sRQnQ2m2'
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