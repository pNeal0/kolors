#!/usr/bin/env python

import argparse
from colorthief import ColorThief
from sty import fg, rs

parser = argparse.ArgumentParser(
    prog = "kolors",
    description = "Generate a color palette from an image"
)
parser.add_argument("-d", "--decimal", action = "store_true",
                    help = "present colors in decimal form instead of hex")
parser.add_argument("-t", "--text", action = "store_true",
                    help = "don't display graphical representation of colors")
parser.add_argument("-p", "--precision", required = True)
parser.add_argument("-f", "--file", required = True)
args = parser.parse_args()

color_thief = ColorThief(args.file)
for clr in color_thief.get_palette(color_count = int(args.precision)):
    r, g, b = clr
    if not args.text:
        print(f"{fg(r, g, b)}██{fg.rs}", end="    ")
    if args.decimal:
        print(f"rgb({r}, {g}, {b})")
    else:
        print(f"#{r:02x}{g:02x}{b:02x}")
