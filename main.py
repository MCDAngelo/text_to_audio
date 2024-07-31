from text_to_audio.pdf_converter import PDFConverter
from text_to_audio.text_to_speech import TextToSpeech

reader = PDFConverter("example.pdf")
audio = TextToSpeech(reader.clean_pages)
audio.save_audio_file("example.mp3")
