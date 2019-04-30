import pyqrcode
import pytube
from pytube import YouTube


def dl_youtube_video(path):
    YouTube(path).streams.first().download()


def make_qrcode(path):
    qr = pyqrcode.create(path)
    qr.eps('generated.eps', scale=6)
    qr.svg('qweqe.svg', scale=6)
    print(qr.terminal(quiet_zone=1))


def main():
    key = input("1 for youtube video\n2 for qr code\n")
    path = input("Input path:\n")
    if key == "1":
        dl_youtube_video("https://www.youtube.com/watch?v=CARGvO4ENRA")
    elif key == "2":
        make_qrcode("https://goo.gl/forms/6ULb1OZG0x9LlPzL2")


if __name__ == '__main__':
    main()
