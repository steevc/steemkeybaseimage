import os, shutil, sys

maximage = 1000
keybase_local_folder = "/keybase/public/steevc/steemit"
keybase_web_folder = "https://steevc.keybase.pub/steemit/"


def get_filename(filename, description):
    name, suffix = os.path.splitext(filename)
    newname = description.replace(" ", "") + suffix
    print(newname)
    return newname


def move_file(sourcefile, description):
    newname = get_filename(sourcefile, description)
    target = os.path.join(keybase_local_folder, newname)
    shutil.copy(sourcefile, target)
    return newname


def process(filename, description):
    # resize
    # move
    target = move_file(filename, description)
    web_file = keybase_web_folder + target
    print("Web file", web_file)
    steemit_md = "![" + description + "](" + web_file + ")"
    print(steemit_md)

if __name__ == "__main__":
    process("/home/steve/Downloads/20160821picks.jpg", "Test picture")