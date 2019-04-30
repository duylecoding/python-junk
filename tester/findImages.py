import fnmatch
import os

images = ['*.jpg', '*.peg', '*.png', '*.tif', '*.tiff']
matches = []

for root, dirnames, filenames in os.walk("C:\\"):
    for extensions in images:
        for filename in fnmatch.filter(filenames, extensions):
            matches.append(os.path.join(root, filename))


for string in matches:
    print(string)

