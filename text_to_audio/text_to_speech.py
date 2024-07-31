import re

from google.cloud import texttospeech


class TextToSpeech:
    def __init__(self, text_list):
        self.client = texttospeech.TextToSpeechClient()
        self.text_list = text_list
        self.voice = texttospeech.VoiceSelectionParams(
            language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
        )
        self.audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )
        print("Converting to audio, this may take a few minutes")
        self.audio_versions = [self.create_audio_versions(p) for p in self.text_list]

    def create_audio_versions(self, text):
        input = texttospeech.SynthesisInput(text=text)
        audio_version = self.client.synthesize_speech(
            input=input, voice=self.voice, audio_config=self.audio_config
        )
        return audio_version

    def save_audio_file(self, filename):
        if not re.match(r"\.mp3$", filename):
            base_name = filename.split(".")[0]
            filename = base_name + ".mp3"
        with open(filename, "wb") as out:
            for pages in self.audio_versions:
                out.write(pages.audio_content)
            print(f'Audio content written to file "{filename}"')
