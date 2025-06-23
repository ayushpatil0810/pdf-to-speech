# PDF Narrator

A Python tool that converts PDF documents to audio files using text-to-speech technology. Extract text from any PDF and transform it into clear, natural-sounding speech with intelligent text processing for optimal audio quality.

## Features

- 📄 **PDF Text Extraction**: Supports multi-page PDF documents
- 🗣️ **Text-to-Speech Conversion**: Uses Google Text-to-Speech (gTTS) for natural audio
- 🧹 **Intelligent Text Cleaning**: Automatically fixes common PDF extraction issues
- 🎵 **MP3 Output**: Generates high-quality audio files
- ⚡ **Auto-Playback**: Automatically plays the generated audio
- 🔧 **Error Handling**: Robust error handling for file operations

## Requirements

- Python 3.6+
- Required packages:
  - `pypdf`
  - `gtts` (Google Text-to-Speech)

## Installation

1. Clone or download this repository
2. Install the required dependencies:

```bash
pip install pypdf gtts
```

## Usage

1. Place your PDF file in the same directory as `main.py`
2. Update the `pdf_file` variable in the script with your PDF filename:

```python
pdf_file = "your_document.pdf"  # Replace with your PDF filename
```

3. Run the script:

```bash
python main.py
```

4. The script will:
   - Extract text from your PDF
   - Clean and process the text
   - Generate an MP3 file (`converted.mp3`)
   - Automatically play the audio

## Text Processing Features

The application includes intelligent text cleaning to improve speech quality:

- Removes extra whitespace and normalizes spacing
- Fixes hyphenated words split across lines
- Removes problematic special characters
- Ensures proper spacing after punctuation
- Truncates long texts to prevent API limitations (4500 characters max)

## File Structure

```
PDF Reader/
├── main.py          # Main application script
├── sample.pdf       # Your PDF file (place here)
├── converted.mp3    # Generated audio output
└── README.md        # This file
```

## Example

```python
# Basic usage
pdf_file = "sample.pdf"
text = pdf_to_text(pdf_file)
if text:
    if text_to_speech(text):
        os.system("converted.mp3")  # Auto-play the audio
```

## Customization

You can customize the following parameters in the `text_to_speech()` function:

- **Output filename**: Change `output_file` parameter
- **Language**: Modify the `lang` parameter (default: "en")
- **Speech speed**: Set `slow=True` for slower speech
- **Character limit**: Adjust `max_chars` for longer/shorter audio

```python
text_to_speech(text, output_file="my_audio.mp3", max_chars=5000)
```

## Limitations

- Maximum text length: 4500 characters (truncated automatically)
- Requires internet connection for gTTS
- Audio quality depends on PDF text extraction accuracy

## Error Handling

The application handles common errors:

- File not found errors
- PDF reading errors
- Text-to-speech conversion errors
- Audio file creation issues

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is open source and available under the [MIT License](LICENSE).
