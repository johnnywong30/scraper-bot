import logging

import httpx
import requests
from bs4 import BeautifulSoup
from pydantic import HttpUrl

from app.config.log_config import LOG_FORMAT

logging.basicConfig(format=LOG_FORMAT, level=logging.INFO)
log = logging.getLogger("Scraper Service")


class ScraperService:
    def __init__(self):
        pass

    def scrape_page(self, url: HttpUrl):
        # Fetch content from url
        with httpx.Client() as client:
            response = requests.get(url)
            response.raise_for_status()
            content = response.content
            soup = BeautifulSoup(content, "html.parser")

        # Extract text from website
        text = soup.get_text()
        return text
