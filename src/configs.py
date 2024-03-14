import os

import openai
from dotenv import find_dotenv, load_dotenv

_ = load_dotenv(find_dotenv())

openai.api_key = os.environ["OPENAI_API_KEY"]

AOAI_MODEL = os.environ["AOAI_MODEL"]
