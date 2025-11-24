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


voices = elevenlabs.text_to_voice.create_previews(
    voice_description="A huge giant, at least as tall as a building. A deep booming voice, loud and jolly.",
    text="Hello there, tiny friends! I'm a jolly giant with a booming voice that echoes across the mountains! Come up here and share a laugh with me. Life is much better when you're tall enough to touch the clouds!"
)

voice = elevenlabs.text_to_voice.create(
    voice_name="Jolly giant",
    voice_description="A huge giant, at least as tall as a building. A deep booming voice, loud and jolly.",
    # The generated voice ID of the preview you want to use,
    # using the first in the list for this example
    generated_voice_id=voices.previews[0].generated_voice_id
)

print(voice.voice_id)

for preview in voices.previews:
    # Convert base64 to audio buffer
    audio_buffer = base64.b64decode(preview.audio_base_64)

    print(f"Playing preview: {preview.generated_voice_id}")

    play(audio_buffer)


print("Done")