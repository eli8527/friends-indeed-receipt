# Friends Indeed Receipt Script

## Setup
1. Connect and turn on the receipt printer.
2. Set up receipt printer as generic printer using [CUPS](https://support.vendhq.com/hc/en-us/articles/205052024-Enabling-CUPS-Printer-Interface-for-Mac). Name it `THERMAL`.
3. Install `sudo /usr/bin/python -m pip install python-escpos --pre`.
4. Place all files in `~/dev/friends-indeed-receipt/`.

## Running
1. Download the receipt image and move it to `~/dev/friends-indeed-receipt/`. Remove all spaces in the name. It should be 384 pixels wide at 300dpi if making your own.
2. Double click `receipt.app`. Give it the image you downloaded.

## Other
To run just the script, replace the name of the image with the one you want to print.
```python
python print.py test.png
```
