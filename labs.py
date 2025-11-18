import requests
from bs4 import BeautifulSoup
from elevenlabs.play import play
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("ELEVENLABS_API_KEY")

target_url = input("Can you input in the URL that you would like to use? ")
page = requests.get(target_url)

if page.status_code == 200:
    print("Successfully connected to the website!")
else:
    print(f"Failed to connect. Status code: {page.status_code}")

soup = BeautifulSoup(page.text, "html.parser")

text_list = []

for tag in soup.find_all("p"):
    text_list.append(tag.get_text())


limited_text_list = text_list[:5]

final_text = " ".join(limited_text_list)

print(f"Sending the following text to ElevenLabs: \n{final_text}")

client = ElevenLabs(api_key=api_key)

audio = client.text_to_speech.convert(
    text=final_text,
    voice_id="qA5SHJ9UjGlW2QwXWR7w",
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
)

play(audio)
