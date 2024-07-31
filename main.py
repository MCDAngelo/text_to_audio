import click

from text_to_audio.pdf_converter import PDFConverter
from text_to_audio.text_to_speech import TextToSpeech


@click.command()
@click.option(
    "--filepath",
    type=click.Path(exists=True, dir_okay=False),
    prompt="Filepath for PDF you wish to convert",
    help="Enter path to file, must be pdf",
)
@click.option(
    "--outpath",
    type=click.Path(dir_okay=False),
    required=False,
    default="",
    prompt="Filepath for mp3 output. If blank will use original filepath",
    help="Enter path to output mp3, if none provided original path is used",
)
def convert_pdf_to_audio(filepath, outpath):
    reader = PDFConverter(filepath)
    audio = TextToSpeech(reader.clean_pages[0:2])
    if outpath.strip() == "":
        outpath = filepath.split(".")[0] + ".mp3"
    audio.save_audio_file(outpath)


if __name__ == "__main__":
    convert_pdf_to_audio()
