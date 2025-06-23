from pypdf import PdfReader
from gtts import gTTS
import os
import re

def pdf_to_text(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        pages_list = reader.pages
        pdf_text_list = [page.extract_text() for page in pages_list]
        pdf_text = " ".join(pdf_text_list).strip()
        return pdf_text
    except FileNotFoundError:
        print(f"Error: File '{pdf_path}' not found")
        return None
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None

def clean_text(text):
    """Clean extracted PDF text for better speech synthesis"""
    # Remove extra whitespace and normalize spaces
    text = re.sub(r'\s+', ' ', text)
    
    # Fix hyphenated words split across lines
    text = re.sub(r'-\s+', '', text)
    
    # Remove special characters that might cause issues
    text = re.sub(r'[^\w\s.,!?;:]', ' ', text)
    
    # Ensure proper spacing after punctuation
    text = re.sub(r'([.!?])\s*', r'\1 ', text)
    
    return text.strip()

def text_to_speech(text, output_file = "converted.mp3", max_chars=4500):
    # Clean the text first
    text = clean_text(text)
    
    if len(text) > max_chars:
        text = text[:max_chars] + "..."
        print(f"Text truncated to {max_chars} characters")
    try:
        speaker = gTTS(text=text, lang="en", slow=False)  # Use the 'text' parameter instead of calling pdf_to_text again
        speaker.save(output_file)
        print(f"Audio saved as {output_file}")
        return True
    except Exception as e:
        print(f"Error creating audio: {e}")
        return False


if __name__ == "__main__":
    pdf_file = "sample.pdf"
    text = pdf_to_text(pdf_file)
    if text:
        if text_to_speech(text):
            os.system("converted.mp3")
    else:
        print("Failed to extract text from PDF")
