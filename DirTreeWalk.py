import os
import sys
import hashlib
from os.path import join

directoryStack = []

def walkTheTree(htap):
    # prevent recursion if directory is linked in directory over and over again
    real_path = os.path.realpath(htap)
    if real_path in directoryStack:
        return
    directoryStack.append(real_path)

    if os.path.isdir(htap):
        try:
            for item in os.listdir(htap):
                fil = join(htap, item)
                real_fil = os.path.realpath(fil) # if file is sym-link, get real file
                try:
                    if os.path.isfile(real_fil):
                        md5hash = hashlib.md5(open(fil, 'rb').read()).hexdigest()
                        print("File-Name: ", item, "\tDirectory: ", htap, "\tHash-Sum: ", md5hash)
                    elif os.path.islink(fil):
                        print("Directory-Name: ", fil, " , is Sym-Link")
                        walkTheTree(fil)
                    elif os.path.isdir(fil):
                        print("Directory-Name: ", fil)
                        walkTheTree(fil)
                except PermissionError:
                    print('\033[95m' + 'Permission denied (probably because of cat content):', fil)
        except PermissionError:
            print('\033[95m' + 'Permission denied (probably because of cat content):', htap)
        except Exception:
            print('\033[95m' + 'Something went terribly wrong. '
                               '\nFor the life of me I cannot figure out what it is, '
                               '\nbut it happened here:', htap)
    elif os.path.isfile(htap):
        print("\033[95m" + "This is a file!")
    else:
        print("\033[95m" + "Sorry, this directory does not exist!")

    directoryStack.pop()


if __name__ == '__main__':
    testdir = "/Users/deniseengert/Studium/7FS_ooScriptsprachen/Testdirectory"
    walkTheTree(testdir)
    # walkTheTree(sys.argv[1])
