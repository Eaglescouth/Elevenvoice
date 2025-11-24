# example.py
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
import base64
import os

load_dotenv()


api_key = os.getenv("ELEVENLABS_API_KEY")
if api_key:
    print(f"✓ API key loaded (length: {len(api_key)} characters)")
    print(f"  First 10 chars: {api_key[:10]}...")
else:
    print("✗ ERROR: ELEVENLABS_API_KEY not found in environment variables!")
    print("  Please create a .env file with: ELEVENLABS_API_KEY=your_api_key_here")
    exit(1)

elevenlabs = ElevenLabs(
    api_key=api_key,
)



text = "Software that requires no maintenance"

# Ensure text is within 100-1000 characters for preview generation
preview_text = text
if len(preview_text) < 100:
    # Pad with a neutral phrase to meet minimum length
    while len(preview_text) < 100:
        preview_text += " . " + text
elif len(preview_text) > 1000:
    # Truncate to meet maximum length
    preview_text = preview_text[:1000]

print(f"Original text length: {len(text)}")
print(f"Preview text length: {len(preview_text)}")

voices = elevenlabs.text_to_voice.create_previews(
    voice_description="A huge giant, at least as tall as a building. A deep booming voice, loud and jolly.",
    text=preview_text
)

voice = elevenlabs.text_to_voice.create(
    voice_name="Jolly giant",
    voice_description="A huge giant, at least as tall as a building. A deep booming voice, loud and jolly.",
    # The generated voice ID of the preview you want to use,
    # using the first in the list for this example
    generated_voice_id=voices.previews[0].generated_voice_id
)

print(f"Created voice: {voice.voice_id}")

# Now generate the audio for the FULL text using the created voice
print("Generating full audio...")
audio = elevenlabs.text_to_speech.convert(
    text=text,
    voice_id=voice.voice_id,
    model_id="eleven_multilingual_v2"
)

play(audio)


print("Done")