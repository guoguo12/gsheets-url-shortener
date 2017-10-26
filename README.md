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
