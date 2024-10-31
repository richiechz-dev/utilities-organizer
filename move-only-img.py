from PIL import Image

import os

downloadsFolder = "/Users/Ricardo/Downloads/"
picturesFolder = "/Users/Ricardo/Pictures/"

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            os.rename(downloadsFolder + filename, picturesFolder + filename)
            print(name + ": " + extension)

        if extension in [".mp3"]:
            musicFolder = "/Users/Ricardo/Music/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
        
        if extension in [".pdf"]:
            documentsFolder = "/Users/Ricardo/Documents/PDF/"
            os.rename(downloadsFolder + filename, documentsFolder + filename)
