from flask import Flask, redirect
import requests

PORT = 49999

SHEET_ID = '1vr6C7CD_RMaNXmxFybG5H6GibrT1Vsx6Jm3sRQnQ2m2'
DB_URL = 'https://docs.google.com/spreadsheets/d/{0}/export?format=csv&id={0}&gid=0'.format(SHEET_ID)

app = Flask(__name__)


def url_for(short_name):
    csv = requests.get(DB_URL).text
    mappings = dict(mapping.split(',') for mapping in csv.split('\r\n'))
    return mappings[short_name]


@app.route('/<short_name>')
def handler(short_name):
    return redirect(url_for(short_name))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
