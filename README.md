# Friends Indeed Receipt Script

1. Connect and turn on the receipt printer.
2. Set up receipt printer as generic printer using [CUPS](https://support.vendhq.com/hc/en-us/articles/205052024-Enabling-CUPS-Printer-Interface-for-Mac). Name it `THERMAL`
3. Download the receipt image. It should be 384 pixels wide at 300dpi if making your own.
4. Run the script, replacing the name of the image with the one you want to print.
```python
python print.py test.png
```

This requires installation of the `escpos` [package](https://github.com/python-escpos/python-escpos).
