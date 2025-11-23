from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
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

audio = elevenlabs.text_to_speech.convert(
    text="Us Southern Folk like to have some fun but FUCK those short sellers. I hope they get fucked in the ass. Hahaaaa, NIGGERRRR! .",
    voice_id="Bj9UqZbhQsanLzgalpEG",
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
)

play(audio)
