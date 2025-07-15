from flask import Flask, jsonify
from scraper import get_highest_bounties  # move logic to scraper.py

app = Flask(__name__)

@app.route("/")
def home():
    return "Replit Bounty Scraper is live!"

@app.route("/run")
def run_scraper():
    results = get_highest_bounties(limit=1)
    return jsonify(results)
