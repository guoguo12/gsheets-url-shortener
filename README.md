# URL Shortener

This code accompanies ["A Concise URL Shortener in Python"](http://aguo.us/writings/url-shortener.html).

## Instructions

1. Follow the instructions in the blog post to set up the database (spreadsheet).
2. Acquire access to a machine with a fixed, public IP address. I use a cheap VPS from [DigitalOcean](https://m.do.co/c/d5db3c2c2cbf) ([non-referral link](https://www.digitalocean.com/)).
3. Clone this repo onto your server: `git clone https://github.com/guoguo12/gsheets-url-shortener.git`.
4. Change `SHEET_ID` in `shortener.py` to your spreadsheet's ID, and also configure `PORT`.
5. Install dependencies with `pip install -r requirements.txt`. (Make sure you're using the pip for your Python 3 installation.)
6. Run the server: `python3 shortener.py`.

You may also want to register a domain name and point it at your server.

## Deploy to Heroku

1. Install [Heroku cli](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).
2. Run `heroku login` to login.
3. Run `heroku create` to create your app.
4. Run `git push heroku master` to deploy.
5. Run `heroku ps:scale web=1` to run an instance of the app.
5. Run `heroku open` to preview.

## Potential improvements

Ideas for improving the code:

* Find a way to modify the spreadsheet such that the server crashes while parsing the CSV.
Then use Python's [`csv` module](https://docs.python.org/3/library/csv.html) to parse the database instead.
* Cache database queries using [`functools.lru_cache`](https://docs.python.org/3/library/functools.html#functools.lru_cache), then add a special endpoint for clearing the cache.
* Keep track of how many times each short URL has been accessed. (Bonus points for writing click-count data back to the spreadsheet.)
