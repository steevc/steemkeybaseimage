import os, shutil, sys
from datetime import date
from PIL import Image
#from tkinter import Tk

maximage = 1000
keybase_local_folder = "/keybase/public/steevc/steemit"
keybase_web_folder = "https://steevc.keybase.pub/steemit/"


def get_filename(filename, description):
    # Build name using date and description
    name, suffix = os.path.splitext(filename)
    newname = date.today().isoformat() + description.replace(" ", "") + suffix
    #print(newname)
    return newname


def move_file(sourcefile, target):
    # Move to target location
    shutil.copy(sourcefile, target)


def resize_image(image, target):
    # Shrink to below max size
    scale = 1.0
    if image.size[0] > image.size[1]:
        dim = image.size[0]
    else:
        dim = image.size[1]
    while dim > maximage:
        scale /= 2
        dim /= 2
    smimage = image.resize((int(image.size[0]*scale), int(image.size[1]*scale)))
    smimage.save(target)


# Issues with pip to install packages
#def text_to_clipboard(text):
#    # From http://stackoverflow.com/questions/11063458/python-script-to-copy-text-to-clipboard
#    r = Tk()
#    r.withdraw()
#    r.clipboard_clear()
#    r.clipboard_append(text)
#    r.destroy()


def process(filename, description):
    im = Image.open(filename)
    #print(im.size)
    newname = get_filename(filename, description)
    target = os.path.join(keybase_local_folder, newname)
    if im.size[0] > maximage or im.size[1] > maximage:
        resize_image(im, target)
    else:
        move_file(filename, target) # Just move and rename

    web_file = keybase_web_folder + newname
    print("Web file", web_file)
    steemit_md = "![" + description + "](" + web_file + ")"
    print(steemit_md)
    #text_to_clipboard(steemit_md)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        process("/home/steve/Downloads/20160821picks.jpg", "Test picture")
    else:
        process(sys.argv[1], sys.argv[2])