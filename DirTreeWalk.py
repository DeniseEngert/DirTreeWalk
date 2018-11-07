import os
import sys
import hashlib
from os.path import join


def walkTheTree(htap):
    if os.path.isdir(htap):
        try:
            for item in os.listdir(htap):
                fil = join(htap, item)
                try:
                    if os.path.isfile(fil):
                        md5hash = hashlib.md5(open(fil, 'rb').read()).hexdigest()
                        print("File-Name: ", item, "\tDirectory: ", htap, "\tHash-Sum: ", md5hash)
                    elif os.path.isdir(fil):
                        print("Directory-Name: ", fil)
                        walkTheTree(fil)
                except PermissionError:
                    print('\033[95m' + 'Permission denied (probably because of cat content):', htap)
        except FileNotFoundError:  # TODO: evtl. loeschen, ersetzen durch Directory Not Found
            print('\033[95m' + 'File not found:', htap)
        except PermissionError:
            print('\033[95m' + 'Permission denied (probably because of cat content):', htap)
        except Exception:
            print('\033[95m' + 'Something went terribly wrong. '
                               '\nFor the life of me I cannot figure out what it is, '
                               '\nbut it happened here:', htap)
    else:
        print("\033[95m" + "Sorry, this directory does not exist!")


if __name__ == '__main__':
    walkTheTree(sys.argv[1])
