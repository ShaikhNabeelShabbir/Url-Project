import pyshorteners as url
import pyqrcode
import png
from png import Image
from pyqrcode import QRCode


def get_shortener(link):
    x = (url.Shortener().tinyurl.short(link))
    print(x)
    return x


def get_QR(s):
    url = pyqrcode.create(s)
    url.png('QR.png', scale=6)


# while True:
#     print("1)shortened your link\n2)Create a QR Code\n3)quit")
#     user = int(input("Enter your choice: "))
#     if user == 1:
#         get_shortener()
#     elif user == 2:
#         get_QR()
#     elif user == 3:
#         quit()
#     else:
#         print("invalid input")
