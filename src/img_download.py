import tarfile
import urllib
import bs4
import csv
import os
from urllib.request import urlopen
from PIL import ImageFile

minWidth = 100
minHeight = 100

def getsizes(uri):
    # get file size *and* image size (None if not known)
    file = urllib.request.urlopen(uri)
    size = file.headers.get("content-length")
    if size: 
        size = int(size)
    p = ImageFile.Parser()
    while True:
        data = file.read(1024)
        if not data:
            break
        p.feed(data)
        if p.image:
            return p.image.size
            break
    file.close()
    return None   

def import_csv():
    print("csv")
    f = open("results.csv") # change to downloaded csv file
    csv_f = csv.reader(f)
    return csv_f


def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = bs4.BeautifulSoup(thepage, "html.parser")
    return soupdata


csvv = import_csv()

next(csvv, None) #skip header

for row in csvv:
    print(row[0])
    i = 1
    soup = make_soup(row[0])
    for img in soup.findAll('img'):
        # print(img)
        temp = img.get('src')
        if temp is not None:
            if temp[:1] == "/":
                image = row[0] + temp
            else:
                image = temp

            # print(image)
            if image.lower().endswith(('.png', '.jpg', '.jpeg')):
                width, height = getsizes(image)
                if width > minWidth and height > minHeight:
                    nametemp = img.get('alt')
                    # if nametemp is None:
                    # if len(nametemp) == 0:
                    if nametemp is None or len(nametemp) == 0:
                    # if not nametemp:
                        filename = str(i)
                        i = i + 1
                    else:
                        filename = nametemp

                    filename = '_'.join(filename.split('/'))
                    info = (filename[:75] + '..') if len(filename) > 75 else filename
                    info = info.replace(" ", "")
                    print("filename: ", info)
                    imagefile = open("./photos/" + info + ".jpeg", 'wb')
                    try:
                        imagefile.write(urllib.request.urlopen(image).read())
                        imagefile.close()
                    except:
                        pass

path = "./photos"
dirList = os.listdir(path)
for filename in dirList:
    print(os.path.splitext(filename)[
              0] + " " + os.getcwd() + "/photos/" + filename + "\n")
    f = open("output1.txt", "a")
    f.write(os.path.splitext(filename)[
                # TODO: change path to relative
                0] + " " + os.getcwd()  + "/photos/"  + filename + "\n")
    f.close()


def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))


make_tarfile('links3.tar.gz', './output1.txt') # TODO: fix compression
