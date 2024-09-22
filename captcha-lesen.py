import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import cv2
import matplotlib.pyplot as plt
from PIL import Image





image = Image.open(r'C:\Users\maxmi\Pictures\ocr-test.png')


captchaWort = pytesseract.image_to_string(image)



print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAACHTUNG")
print(captchaWort)