import sys
import subprocess
import os
from escpos.printer import File, Dummy

# python print.py file.png
def main():
    imageIn = sys.argv[1]
    fileOut = imageIn + "_tmp.txt"

    p = Dummy()
    p.image(imageIn)
    f = File(fileOut)
    f._raw(p.output)
    f.cut()

    subprocess.call("lpr -P THERMAL -o raw " + fileOut, shell=True)

    os.remove(fileOut)

if __name__ == '__main__':
    main()
