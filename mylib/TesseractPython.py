try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from textblob import TextBlob
import argparse
import cv2

# class for normal ocr and translated ocr
class tesseract_class(object):

    def extract_ocr(filename):
        ##To set tesseract path manually in the code. Note: it varies according to your installation.
        #pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        # apply tesseract ocr
        text = pytesseract.image_to_string(Image.open(filename))
        return text


    def translate_ocr(filename):
        ##To set tesseract path
        #pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        print("")
        lang = input("Enter the source lang. (ex. deu for german, swe for swedish): ")

        ap = argparse.ArgumentParser()
        ap.add_argument("-t", "--to", type=str, default="en",
        	help="language that we'll be translating to")
        args = vars(ap.parse_args())

        ##load the input image and convert it from BGR to RGB channel. To test.
        # orig = pytesseract.image_to_string(Image.open(filename))
        # rgb = cv2.cvtColor(orig, cv2.COLOR_BGR2RGB)

        # apply tesseract ocr
        text = pytesseract.image_to_string(Image.open(filename))

        # show the original OCR'd text
        print("")
        print("SOURCE LANGUAGE:")
        print("==========")
        print(text)
        print("")

        # translate the text into a different language
        tb = TextBlob(text)
        translated = tb.translate(to=args["to"])
        translated1 = ''.join(translated)

        # show the translated text
        print("TRANSLATED LANGUAGE:")
        print("==========")
        print(translated)
        return text, translated1
