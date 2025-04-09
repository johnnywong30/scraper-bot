import logging

from pydantic import HttpUrl

from app.config.log_config import LOG_FORMAT
from app.openai.model import Model, Tokenizer
from app.services.scraper import ScraperService

logging.basicConfig(format=LOG_FORMAT, level=logging.INFO)
log = logging.getLogger("GenAI Chat Service")


class ChatService:
    def __init__(self):
        self.model = Model
        self.tokenizer = Tokenizer

    def generate_response(self, input_text: HttpUrl):

        scraper = ScraperService()

        # check if the input text is a URL
        if "http" in input_text or "www" in input_text:
            scraped_text = scraper.scrape_page(input_text)
            input_text += " " + scraped_text

        # encode the input text
        input_text = self.tokenizer.encode(input_text, return_tensors="pt")

        # generate a response
        response = self.model.generate(
            input_text, max_length=500, num_return_sequences=1
        )

        # decode the response
        response_text = self.tokenizer.decode(response[0])

        return response_text
