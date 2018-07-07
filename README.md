# URL Shortener

This code accompanies ["A Concise URL Shortener in Python"](http://aguo.us/writings/url-shortener.html).

# Instructions

1. Follow the instructions in the blog post to set up the database (spreadsheet).
2. Acquire access to a machine with a fixed, public IP address. I use a cheap VPS from [DigitalOcean](https://m.do.co/c/d5db3c2c2cbf) ([non-referral link](https://www.digitalocean.com/)).
3. Clone this repo onto your server: `git clone https://github.com/guoguo12/gsheets-url-shortener.git`.
4. Change `SHEET_ID` (and other configuration) in `config.json` to your spreadsheet's ID.
5. Install dependencies with `pip install -r requirements.txt`. (Make sure you're using the pip for your Python 3 installation.)
6. Run test/development server: `python3 shortener.py`

You may also want to register a domain name and point it at your server.

## Production

1. Install virtualenv package with pip: `pip install virtualenv`.
2. Create a new virtual environment: `virtualenv env`.
3. Activate virtual environment: `source env/bin/activate`.
4. Install dependencies with `pip install -r requirements.txt`.
5. Serve with Gunicorn (Python WSGI HTTP Server): `gunicorn -b 0.0.0.0:49999 shortener:app` (pick any port).
6. Optional: configure upstream server (i.e. nginx) to proxy requests to Gunicorn.

## Run with Heroku

1. Install [Heroku cli](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).
2. Run `heroku login` to login.
3. Run `heroku create --region eu` to create your app in the EU region.
4. Run `git push heroku master` to deploy.
5. Run `heroku ps:scale web=1` to run an instance of the app.
5. Run `heroku open` to preview.

## Potential improvements

Ideas for improving the code:

* Find a way to modify the spreadsheet such that the server crashes while parsing the CSV.
Then use Python's [`csv` module](https://docs.python.org/3/library/csv.html) to parse the database instead.
* Cache database queries using [`functools.lru_cache`](https://docs.python.org/3/library/functools.html#functools.lru_cache), then add a special endpoint for clearing the cache.
* Keep track of how many times each short URL has been accessed. (Bonus points for writing click-count data back to the spreadsheet.)
