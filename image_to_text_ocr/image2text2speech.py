# Pytesseract(Python-tesseract) : It is an optical character recognition (OCR) tool for python sponsored by google.
import pytesseract
# pyttsx3 : It is an offline cross-platform Text-to-Speech library
import pyttsx3
# Python Imaging Library (PIL) : It adds image processing capabilities to your Python interpreter
from PIL import Image
# Googletrans : It is a free python library that implements the Google Translate API.
from googletrans import Translator

# Open the image 
img = Image.open('image_to_text_ocr\london.png')
print(img)

# path where Tesseract module is installed
pytesseract.pytesseract.tesseract_cmd = "c:\\Users\\sivaneshl\\AppData\\Local\\Tesseract-OCR\\tesseract.exe"

# convert the image 
result = pytesseract.image_to_string(img)
print(result)

# write to a file 
with open('image_to_text_ocr\output.txt', 'w') as f:
    f.write(result)


# translate to any language
translator = Translator()
translated = translator.translate(result, dest='de')
print(translated)

# text to speech 
engine = pyttsx3.init()
engine.say(translated)
engine.say(result)
engine.runAndWait()






