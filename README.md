# Elevenvoice

Building a project using the ElevenLabs API.

## Overview

Elevenvoice is a Python-based toolkit designed to interface seamlessly with the ElevenLabs API. It provides modular scripts for text-to-speech generation, voice cloning, and custom voice design, allowing developers to integrate high-quality AI voices into their applications.

## Project Structure

The repository is divided into focused, single-purpose scripts:

* **`clone.py`**: Handles the voice cloning functionality. Use this to upload audio samples and generate a custom, cloned voice model via the API.
* **`labs.py`**: The core utility script for general API interactions, account configuration, and retrieving available voice models.
* **`voice.py`**: Manages standard Text-to-Speech (TTS) operations. Pass text strings to pre-made or custom voices and output high-quality audio files.
* **`voice_design.py`**: Interfaces with the ElevenLabs Voice Design tool, allowing you to generate entirely new voices based on specific attributes like age, gender, and accent.

## Prerequisites

* Python 3.8+
* An active [ElevenLabs account](https://elevenlabs.io/) and API Key.

## Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/Eaglescouth/Elevenvoice.git](https://github.com/Eaglescouth/Elevenvoice.git)
   cd Elevenvoice


   2. Create and activate a virtual environment to keep your dependencies isolated:

   Windows:

   python -m venv venv
venv\Scripts\activate


Mac/Linux:

python -m venv venv
source venv/bin/activate



3. Install the required dependencies:

pip install elevenlabs python-dotenv




4. Create a .env file in the root directory and add your API key:

ELEVENLABS_API_KEY=your_api_key_here



Usage
Each script is designed to be run independently based on the task you need to perform. Make sure your virtual environment is activated before running any scripts.

For example, to generate standard text-to-speech, you would execute:


python voice.py

License

https://www.google.com/search?q=LICENSE







