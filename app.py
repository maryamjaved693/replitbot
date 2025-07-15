from flask import Flask, jsonify
import os
import json
import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import firecrawl

# Load secrets from environment
firecrawl_api_key = os.environ.get('FIRECRAWL_API_KEY')
slack_webhook_url = os.environ.get('SLACK_WEBHOOK_URL')

# Init Firecrawl
app_fc = firecrawl.FirecrawlApp(api_key=firecrawl_api_key)

# Init Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Replit Bounty Scraper is live!"

@app.route('/run')
def run():
    from scraper import get_highest_bounties  # assuming logic is in scraper.py
    bounties = get_highest_bounties(limit=1)
    return jsonify(bounties)
