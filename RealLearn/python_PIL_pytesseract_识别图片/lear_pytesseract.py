from PIL import Image
import pytesseract
import sys



def readPicture(address):
    image = Image.open(address)
    text = pytesseract.image_to_string(image, lang='chi_sim') # , lang='chi_sim'
    print(text)

a = r'e:\Desktop\hhh.png'
b = r'e:\Desktop\opop.png'
c = r'e:\Desktop\123.png'
d = r'e:\Desktop\qiufengci.png'
readPicture(c)


# def aaa(image):
#     imgry = image.convert('L')












