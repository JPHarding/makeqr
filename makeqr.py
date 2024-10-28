import argparse
from qrcode import make
from random import randint
from os import path

parser = argparse.ArgumentParser(description='Creates a QR code PNG from your text input.')


parser.add_argument("user_text", help="This is the text data that will turn into a png QR Code.")
parser.add_argument("--path", default="", help="Where you want the png QR Code to be saved. (Optional)")
args = vars(parser.parse_args())

user_path = args["path"]

img = make(data = args["path"])

file_path = "qr" + str(randint(4545, 9654)) + ".png"
file_path = path.join(user_path, file_path)
img.save(file_path, "PNG")
print(f"QR Code created at: {file_path}")
