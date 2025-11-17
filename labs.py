import requests
from bs4 import BeautifulSoup

from elevenlabs import play, save
from elevenlabs.client import ElevenLabs


target_url = input("Can you input in the URL that you would like to use? ")
page = requests.get(target_url)
