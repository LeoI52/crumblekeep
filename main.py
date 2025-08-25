"""
@author : Léo Imbert
@created : 25/08/2025
@updated : 25/08/2025
"""

import random
import pyxel
import math
import sys
import os

# -------------------- UTILS -------------------- #

PALETTE = [0xFFFFFF, 0xFFD19D, 0xAEB5BD, 0x4D80C9, 0x054494, 0x511E43, 0x100820, 0x823E2C, 0xE93841, 0xF1892D, 0xFFE947, 0xFFA9A9, 0xEB6C82, 0x7D3EBF, 0x1E8A4C, 0x5AE150]

characters_matrices = {
    " ":[[0,0,0,0]],
    "A":[[0,0,0,0,0,0],[0,0,1,1,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,1,1,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1]],
    "B":[[0,0,0,0,0,0,0],[1,1,1,1,1,1,0],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,1,1,1,0],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[1,1,1,1,1,1,0]],
    "C":[[0,0,0,0,0,0,0],[0,0,1,1,1,1,0],[0,1,1,0,0,1,1],[1,1,0,0,0,0,0],[1,1,0,0,0,0,0],[1,1,0,0,0,0,0],[0,1,1,0,0,1,1],[0,0,1,1,1,1,0]],
    "D":[[0,0,0,0,0,0,0],[1,1,1,1,1,0,0],[0,1,1,0,1,1,0],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,0,1,1,0],[1,1,1,1,1,0,0]],
    "E":[[0,0,0,0,0,0,0],[1,1,1,1,1,1,1],[0,1,1,0,0,0,1],[0,1,1,0,1,0,0],[0,1,1,1,1,0,0],[0,1,1,0,1,0,0],[0,1,1,0,0,0,1],[1,1,1,1,1,1,1]],
    "F":[[0,0,0,0,0,0,0],[1,1,1,1,1,1,1],[0,1,1,0,0,0,1],[0,1,1,0,1,0,0],[0,1,1,1,1,0,0],[0,1,1,0,1,0,0],[0,1,1,0,0,0,0],[1,1,1,1,0,0,0]],
    "G":[[0,0,0,0,0,0,0],[0,0,1,1,1,1,0],[0,1,1,0,0,1,1],[1,1,0,0,0,0,0],[1,1,0,0,0,0,0],[1,1,0,0,1,1,1],[0,1,1,0,0,1,1],[0,0,1,1,1,1,1]],
    "H":[[0,0,0,0,0,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,1,1,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1]],
    "I":[[0,0,0,0,0,0],[1,1,1,1,1,1],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[1,1,1,1,1,1]],
    "J":[[0,0,0,0,0,0,0],[0,0,0,1,1,1,1],[0,0,0,0,1,1,0],[0,0,0,0,1,1,0],[0,0,0,0,1,1,0],[1,1,0,0,1,1,0],[1,1,0,0,1,1,0],[0,1,1,1,1,0,0]],
    "K":[[0,0,0,0,0,0,0],[1,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,0,1,1,0],[0,1,1,1,1,0,0],[0,1,1,0,1,1,0],[0,1,1,0,0,1,1],[1,1,1,0,0,1,1]],
    "L":[[0,0,0,0,0,0,0],[1,1,1,1,0,0,0],[0,1,1,0,0,0,0],[0,1,1,0,0,0,0],[0,1,1,0,0,0,0],[0,1,1,0,0,0,1],[0,1,1,0,0,1,1],[1,1,1,1,1,1,1]],
    "M":[[0,0,0,0,0,0,0],[1,1,0,0,0,1,1],[1,1,1,0,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,0,1,0,1,1],[1,1,0,0,0,1,1],[1,1,0,0,0,1,1]],
    "N":[[0,0,0,0,0,0,0],[1,1,0,0,0,1,1],[1,1,1,0,0,1,1],[1,1,1,1,0,1,1],[1,1,0,1,1,1,1],[1,1,0,0,1,1,1],[1,1,0,0,0,1,1],[1,1,0,0,0,1,1]],
    "O":[[0,0,0,0,0,0,0],[0,0,1,1,1,0,0],[0,1,1,0,1,1,0],[1,1,0,0,0,1,1],[1,1,0,0,0,1,1],[1,1,0,0,0,1,1],[0,1,1,0,1,1,0],[0,0,1,1,1,0,0]],
    "P":[[0,0,0,0,0,0,0],[1,1,1,1,1,1,0],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,1,1,1,0],[0,1,1,0,0,0,0],[0,1,1,0,0,0,0],[1,1,1,1,0,0,0]],
    "Q":[[0,0,0,0,0,0,0],[0,0,1,1,1,0,0],[0,1,1,0,1,1,0],[1,1,0,0,0,1,1],[1,1,0,0,0,1,1],[1,1,0,1,1,0,1],[1,1,0,0,1,1,0],[0,1,1,1,0,1,1]],
    "R":[[0,0,0,0,0,0,0],[1,1,1,1,1,1,0],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,1,1,1,0],[0,1,1,0,1,1,0],[0,1,1,0,0,1,1],[1,1,1,0,0,1,1]],
    "S":[[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,0,0],[0,1,1,1,1,0],[0,0,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "T":[[0,0,0,0,0,0],[1,1,1,1,1,1],[1,0,1,1,0,1],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,1,1,1,1,0]],
    "U":[[0,0,0,0,0,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "V":[[0,0,0,0,0,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0],[0,0,1,1,0,0]],
    "W":[[0,0,0,0,0,0,0],[1,1,0,0,0,1,1],[1,1,0,0,0,1,1],[1,1,0,0,0,1,1],[1,1,0,1,0,1,1],[1,1,1,1,1,1,1],[1,1,1,0,1,1,1],[1,1,0,0,0,1,1]],
    "X":[[0,0,0,0,0,0,0],[1,1,0,0,0,1,1],[0,1,1,0,1,1,0],[0,0,1,1,1,0,0],[0,0,1,1,1,0,0],[0,1,1,0,1,1,0],[1,1,0,0,0,1,1],[1,1,0,0,0,1,1]],
    "Y":[[0,0,0,0,0,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,1,1,1,1,0]],
    "Z":[[0,0,0,0,0,0,0],[1,1,1,1,1,1,1],[1,1,0,0,0,1,1],[1,0,0,0,1,1,0],[0,0,0,1,1,0,0],[0,0,1,1,0,0,1],[0,1,1,0,0,1,1],[1,1,1,1,1,1,1]],
    "a":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,1,1,1,1,0,0],[0,0,0,0,1,1,0],[0,1,1,1,1,1,0],[1,1,0,0,1,1,0],[0,1,1,1,0,1,1]],
    "b":[[0,0,0,0,0,0,0],[1,1,1,0,0,0,0],[0,1,1,0,0,0,0],[0,1,1,1,1,1,0],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[1,1,0,1,1,1,0]],
    "c":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,0,0],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "d":[[0,0,0,0,0,0,0],[0,0,0,1,1,1,0],[0,0,0,0,1,1,0],[0,1,1,1,1,1,0],[1,1,0,0,1,1,0],[1,1,0,0,1,1,0],[1,1,0,0,1,1,0],[0,1,1,1,0,1,1]],
    "e":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,1,1,1,1],[1,1,0,0,0,0],[0,1,1,1,1,0]],
    "f":[[0,0,0,0,0,0],[0,0,1,1,1,0],[0,1,1,0,1,1],[0,1,1,0,0,0],[1,1,1,1,0,0],[0,1,1,0,0,0],[0,1,1,0,0,0],[1,1,1,1,0,0]],
    "g":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,1,1,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,1],[0,0,0,0,1,1],[1,1,1,1,1,0]],
    "h":[[0,0,0,0,0,0,0],[1,1,1,0,0,0,0],[0,1,1,0,0,0,0],[0,1,1,0,1,1,0],[0,1,1,1,0,1,1],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[1,1,1,0,0,1,1]],
    "i":[[0,0,0,0],[0,1,1,0],[0,0,0,0],[1,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0],[1,1,1,1]],
    "j":[[0,0,0,0,0,0],[0,0,0,0,1,1],[0,0,0,0,0,0],[0,0,0,1,1,1],[0,0,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "k":[[0,0,0,0,0,0,0],[1,1,1,0,0,0,0],[0,1,1,0,0,0,0],[0,1,1,0,0,1,1],[0,1,1,0,1,1,0],[0,1,1,1,1,0,0],[0,1,1,0,1,1,0],[1,1,1,0,0,1,1]],
    "l":[[0,0,0,0],[1,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0],[1,1,1,1]],
    "m":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,1,1,0,1,1,0],[1,1,1,1,1,1,1],[1,1,0,1,0,1,1],[1,1,0,1,0,1,1],[1,1,0,0,0,1,1]],
    "n":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,1,0,1,1,1,0],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1]],
    "o":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "p":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,1,0,1,1,1,0],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,1,1,1,0],[0,1,1,0,0,0,0],[1,1,1,1,0,0,0]],
    "q":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,1,1,1,0,1,1],[1,1,0,0,1,1,0],[1,1,0,0,1,1,0],[0,1,1,1,1,1,0],[0,0,0,0,1,1,0],[0,0,0,1,1,1,1]],
    "r":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,1,0,1,1,1,0],[0,1,1,1,0,1,1],[0,1,1,0,0,0,0],[0,1,1,0,0,0,0],[1,1,1,1,0,0,0]],
    "s":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,0,0],[0,1,1,1,1,0],[0,0,0,0,1,1],[1,1,1,1,1,0]],
    "t":[[0,0,0,0,0,0],[0,1,1,0,0,0],[0,1,1,0,0,0],[1,1,1,1,1,0],[0,1,1,0,0,0],[0,1,1,0,0,0],[0,1,1,0,1,1],[0,0,1,1,1,0]],
    "u":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,1]],
    "v":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0],[0,0,1,1,0,0]],
    "w":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,1,0,0,0,1,1],[1,1,0,1,0,1,1],[1,1,0,1,0,1,1],[1,1,1,1,1,1,1],[0,1,1,0,1,1,0]],
    "x":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,1,0,0,0,1,1],[0,1,1,0,1,1,0],[0,0,1,1,1,0,0],[0,1,1,0,1,1,0],[1,1,0,0,0,1,1]],
    "y":[[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,1],[0,0,0,0,1,1],[1,1,1,1,1,0]],
    "z":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,1,1,1,1],[1,0,0,1,1,0],[0,0,1,1,0,0],[0,1,1,0,0,1],[1,1,1,1,1,1]],
    "1":[[0,0,0,0,0,0],[0,0,1,1,0,0],[0,1,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[1,1,1,1,1,1]],
    "2":[[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[0,0,0,0,1,1],[0,1,1,1,1,0],[1,1,0,0,0,0],[1,1,0,0,1,1],[1,1,1,1,1,1]],
    "3":[[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[0,0,0,0,1,1],[0,0,1,1,1,0],[0,0,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "4":[[0,0,0,0,0,0,0],[0,0,0,1,1,1,0],[0,0,1,1,1,1,0],[0,1,1,0,1,1,0],[1,1,0,0,1,1,0],[1,1,1,1,1,1,1],[0,0,0,0,1,1,0],[0,0,0,1,1,1,1]],
    "5":[[0,0,0,0,0,0],[1,1,1,1,1,1],[1,1,0,0,0,1],[1,1,0,0,0,0],[1,1,1,1,1,0],[0,0,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "6":[[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,0,0],[1,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "7":[[0,0,0,0,0,0],[1,1,1,1,1,1],[1,1,0,0,1,1],[0,0,0,0,1,1],[0,0,0,1,1,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0]],
    "8":[[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "9":[[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,1],[0,0,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "0":[[0,0,0,0,0,0,0],[0,1,1,1,1,1,0],[1,1,0,0,0,1,1],[1,1,0,0,1,1,1],[1,1,0,1,0,1,1],[1,1,1,0,0,1,1],[1,1,0,0,0,1,1],[0,1,1,1,1,1,0]],
    "?":[[0,0,0,0],[1,1,1,0],[1,0,1,1],[0,0,1,1],[0,1,1,0],[0,0,0,0],[0,1,1,0],[0,1,1,0]],
    ",":[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,1,1,0],[0,1,1,0],[1,1,0,0]],
    ".":[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[1,1,0],[1,1,0]],
    ";":[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0],[0,1,1,0],[0,1,1,0],[1,1,0,0]],
    "/":[[0,0,0,0,0,0],[0,0,0,0,1,1],[0,0,0,0,1,0],[0,0,0,1,1,0],[0,0,1,1,0,0],[0,0,1,0,0,0],[0,1,1,0,0,0],[1,1,0,0,0,0]],
    ":":[[0,0],[0,0],[1,1],[1,1],[0,0],[1,1],[1,1],[0,0]],
    "!":[[0,0],[1,1],[1,1],[1,1],[1,1],[0,0],[1,1],[1,1]],
    "&":[[0,1,1,1,0,0,0],[1,0,0,0,1,0,0],[1,0,0,0,1,0,0],[0,1,1,1,0,0,0],[1,1,0,1,1,0,0],[1,0,0,0,1,0,1],[1,1,0,0,0,1,0],[0,1,1,1,1,0,1]],
    "é":[[0,0,0,1,1,0],[0,1,1,0,0,0],[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,1,1,1,1],[1,1,0,0,0,0],[0,1,1,1,1,0]],
    "~":[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,1,1,0,1],[1,0,0,1,0]],
    '"':[[0,0,0,0],[0,1,0,1],[0,1,0,1],[1,0,1,0],[1,0,1,0]],
    "#":[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,1,0,1,0],[1,1,1,1,1],[0,1,0,1,0],[1,1,1,1,1],[0,1,0,1,0]],
    "'":[[0,0,0,0,0],[0,0,1,1,0],[0,0,1,1,0],[0,1,1,0,0],[0,1,1,0,0]],
    "{":[[0,0,0],[0,0,1],[0,1,0],[0,1,0],[1,0,0],[0,1,0],[0,1,0],[0,0,1]],
    "(":[[0,0,0],[0,0,1],[0,1,0],[1,0,0],[1,0,0],[1,0,0],[0,1,0],[0,0,1]],
    "[":[[0,0,0],[1,1,1],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,1,1]],
    "-":[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,1,1,1],[1,1,1,1],[0,0,0,0],[0,0,0,0]],
    "|":[[1],[1],[1],[1],[1],[1],[1],[1]],
    "è":[[0,1,1,0,0,0],[0,0,0,1,1,0],[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,1,1,1,1],[1,1,0,0,0,0],[0,1,1,1,1,0]],
    "_":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,1,1,1,1]],
    "ç":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,0,0],[1,1,0,0,1,1],[0,1,1,1,1,0],[0,0,0,1,0,0],[0,0,1,0,0,0]],
    "à":[[0,0,1,1,0,0,0],[0,0,0,0,1,1,0],[0,0,0,0,0,0,0],[0,1,1,1,1,0,0],[0,0,0,0,1,1,0],[0,1,1,1,1,1,0],[1,1,0,0,1,1,0],[0,1,1,1,0,1,1]],
    "@":[[0,0,0,0,0,0,0],[0,0,1,1,1,1,0],[0,1,0,0,0,0,1],[1,0,0,1,1,0,1],[1,0,1,0,0,1,1],[1,0,1,0,0,1,1],[1,0,0,1,1,0,0],[0,1,0,0,0,0,1],[0,0,1,1,1,1,0]],
    "°":[[1,1,1],[1,0,1],[1,1,1]],
    ")":[[0,0,0],[1,0,0],[0,1,0],[0,0,1],[0,0,1],[0,0,1],[0,1,0],[1,0,0]],
    "]":[[0,0,0],[1,1,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[1,1,1]],
    "+":[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[1,1,1,1,1],[0,0,1,0,0],[0,0,1,0,0]],
    "=":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,1,1,1,1],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,1,1,1,1],[0,0,0,0,0,0]],
    "}":[[0,0,0],[1,0,0],[0,1,0],[0,1,0],[0,0,1],[0,1,0],[0,1,0],[1,0,0]],
    "*":[[0,0,0],[1,0,1],[0,1,0],[1,0,1]],
    "%":[[0,1,0,0,0,0,0],[1,0,1,0,1,1,0],[0,1,0,0,1,0,0],[0,0,0,1,1,0,0],[0,0,1,1,0,0,0],[0,0,1,0,0,1,0],[0,1,1,0,1,0,1],[1,1,0,0,0,1,0]],
    "€":[[0,0,0,0,0,0],[0,0,1,1,1,0],[0,1,0,0,0,1],[0,1,1,1,0,0],[1,0,0,0,0,0],[0,1,1,1,0,0],[0,1,0,0,0,1],[0,0,1,1,1,0]],
    "$":[[0,0,1,0,0],[0,1,1,1,0],[1,0,1,0,1],[1,0,1,0,0],[0,1,1,1,0],[0,0,1,0,1],[1,0,1,0,1],[0,1,1,1,0],[0,0,1,0,0]]
}

CARDINAL_OPPOSITE = {"N":"S", "S":"N", "W":"E", "E":"W"}

NORMAL_COLOR_MODE = 0
ROTATING_COLOR_MODE = 1
RANDOM_COLOR_MODE = 2

ANCHOR_TOP_LEFT = 0
ANCHOR_TOP_RIGHT = 1
ANCHOR_BOTTOM_LEFT = 2
ANCHOR_BOTTOM_RIGHT = 3
ANCHOR_LEFT = 4
ANCHOR_RIGHT = 5
ANCHOR_TOP = 6
ANCHOR_BOTTOM = 7
ANCHOR_CENTER = 8

class PyxelManager:

    def __init__(self, width:int, height:int, scenes:list, default_scene_id:int=0, fps:int=60, fullscreen:bool=False, mouse:bool=False, quit_key:int=pyxel.KEY_ESCAPE, camera_x:int=0, camera_y:int=0):
        
        self.__fps = fps
        self.__scenes_dict = {scene.id:scene for scene in scenes}
        self.__current_scene = self.__scenes_dict.get(default_scene_id, 0)
        self.__transition = {}

        self.__cam_x = self.__cam_tx = camera_x
        self.__cam_y = self.__cam_ty = camera_y
        self.__shake_amount = 0
        self.__sub_shake_amount = 0

        pyxel.init(width, height, fps=self.__fps, quit_key=quit_key)
        pyxel.fullscreen(fullscreen)
        pyxel.mouse(mouse)

        if self.__current_scene.pyxres_path:
            pyxel.load(os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), self.__current_scene.pyxres_path))
        pyxel.title(self.__current_scene.title)
        pyxel.screen_mode(self.__current_scene.screen_mode)
        pyxel.colors.from_list(self.__current_scene.palette)

    @property
    def camera_x(self)-> int:
        return self.__cam_x
    
    @property
    def camera_y(self)-> int:
        return self.__cam_y

    @property
    def mouse_x(self)-> int:
        return self.__cam_x + pyxel.mouse_x
    
    @property
    def mouse_y(self)-> int:
        return self.__cam_y + pyxel.mouse_y
    
    @property
    def fps(self)-> int:
        return self.__fps
    
    def set_camera(self, new_camera_x:int, new_camera_y:int):
        self.__cam_x = self.__cam_tx = new_camera_x
        self.__cam_y = self.__cam_ty = new_camera_y

    def move_camera(self, new_camera_x:int, new_camera_y:int):
        self.__cam_tx = new_camera_x
        self.__cam_ty = new_camera_y

    def shake_camera(self, amount:int, sub_amount:float):
        self.__shake_amount = amount
        self.__sub_shake_amount = sub_amount

    def change_scene(self, new_scene_id:int, new_camera_x:int=0, new_camera_y:int=0, action=None):
        self.set_camera(new_camera_x, new_camera_y)

        self.__current_scene = self.__scenes_dict.get(new_scene_id, 0)
        if action:
            action()

        if self.__current_scene.pyxres_path:
            pyxel.load(os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), self.__current_scene.pyxres_path))
        pyxel.title(self.__current_scene.title)
        pyxel.screen_mode(self.__current_scene.screen_mode)
        pyxel.colors.from_list(self.__current_scene.palette)

    def change_scene_dither(self, new_scene_id:int, speed:float, transition_color:int, new_camera_x:int=0, new_camera_y:int=0, action=None):
        self.__transition = {
            "type":"dither",
            "direction":1,
            "new_scene_id":new_scene_id,
            "speed":speed,
            "transition_color":transition_color,
            "new_camera_x":new_camera_x,
            "new_camera_y":new_camera_y,
            "dither":0,
            "action":action
        }

    def change_scene_circle(self, new_scene_id:int, speed:int, transition_color:int, new_camera_x:int=0, new_camera_y:int=0, action=None):
        self.__transition = {
            "type":"circle",
            "direction":1,
            "new_scene_id":new_scene_id,
            "speed":speed,
            "transition_color":transition_color,
            "new_camera_x":new_camera_x,
            "new_camera_y":new_camera_y,
            "radius":0,
            "max_radius":((pyxel.width ** 2 + pyxel.height ** 2) ** 0.5) / 2,
            "action":action
        }

    def change_scene_closing_doors(self, new_scene_id:int, speed:int, transition_color:int, new_camera_x:int=0, new_camera_y:int=0, action=None):
        self.__transition = {
            "type":"closing_doors",
            "direction":1,
            "new_scene_id":new_scene_id,
            "speed":speed,
            "transition_color":transition_color,
            "new_camera_x":new_camera_x,
            "new_camera_y":new_camera_y,
            "w":0,
            "x":self.__cam_x + pyxel.width,
            "action":action
        }

    def change_scene_rectangle_right_left(self, new_scene_id:int, speed:int, transition_color:int, new_camera_x:int=0, new_camera_y:int=0, action=None):
        self.__transition = {
            "type":"rectangle_right_left",
            "direction":1,
            "new_scene_id":new_scene_id,
            "speed":speed,
            "transition_color":transition_color,
            "new_camera_x":new_camera_x,
            "new_camera_y":new_camera_y,
            "x":self.__cam_x + pyxel.width,
            "w":0,
            "action":action
        }

    def change_scene_rectangle_left_right(self, new_scene_id:int, speed:int, transition_color:int, new_camera_x:int=0, new_camera_y:int=0, action=None):
        self.__transition = {
            "type":"rectangle_left_right",
            "direction":1,
            "new_scene_id":new_scene_id,
            "speed":speed,
            "transition_color":transition_color,
            "new_camera_x":new_camera_x,
            "new_camera_y":new_camera_y,
            "x":self.__cam_x,
            "w":0,
            "action":action
        }

    def change_scene_outer_circle(self, new_scene_id:int, speed:int, transition_color:int, new_camera_x:int=0, new_camera_y:int=0, action=None):
        self.__transition = {
            "type":"outer_circle",
            "direction":1,
            "new_scene_id":new_scene_id,
            "speed":speed,
            "transition_color":transition_color,
            "new_camera_x":new_camera_x,
            "new_camera_y":new_camera_y,
            "start_end":int(((pyxel.width ** 2 + pyxel.height ** 2) ** 0.5) / 2) + 1,
            "end":int(((pyxel.width ** 2 + pyxel.height ** 2) ** 0.5) / 2) + 1,
            "action":action
        }

    def change_scene_triangle(self, new_scene_id:int, speed:int, transition_color:int, rotation_speed:int, new_camera_x:int=0, new_camera_y:int=0, action=None):
        self.__transition = {
            "type":"triangle",
            "direction":1,
            "new_scene_id":new_scene_id,
            "speed":speed,
            "transition_color":transition_color,
            "rotation_speed":rotation_speed,
            "new_camera_x":new_camera_x,
            "new_camera_y":new_camera_y,
            "size":0,
            "angle":270,
            "action":action
        }

    def apply_palette_effect(self, effect_function, **kwargs):
        pyxel.colors.from_list(effect_function(self.__current_scene.palette, kwargs))

    def reset_palette(self):
        pyxel.colors.from_list(self.__current_scene.palette)

    def handle_transitions(self):

        if self.__transition.get("type") == "dither":
            self.__transition["dither"] += self.__transition["speed"] * self.__transition["direction"]

            if self.__transition["dither"] > 1 and self.__transition["direction"] == 1:
                self.__transition["direction"] = -1
                self.change_scene(self.__transition["new_scene_id"], self.__transition["new_camera_x"], self.__transition["new_camera_y"], self.__transition["action"])
            if self.__transition["dither"] < 0 and self.__transition["direction"] == -1:
                self.__transition = {}
                return
            pyxel.dither(self.__transition["dither"])
            pyxel.rect(self.__cam_x, self.__cam_y, pyxel.width, pyxel.height, self.__transition["transition_color"])
            pyxel.dither(1)

        elif self.__transition.get("type") == "circle":
            self.__transition["radius"] += self.__transition["speed"] * self.__transition["direction"]

            if self.__transition["radius"] > self.__transition["max_radius"] and self.__transition["direction"] == 1:
                self.__transition["direction"] = -1
                self.change_scene(self.__transition["new_scene_id"], self.__transition["new_camera_x"], self.__transition["new_camera_y"], self.__transition["action"])
            if self.__transition["radius"] < 0 and self.__transition["direction"] == -1:
                self.__transition = {}
                return
            pyxel.circ(self.__cam_x + pyxel.width / 2, self.__cam_y + pyxel.height / 2, self.__transition["radius"], self.__transition["transition_color"])

        elif self.__transition.get("type") == "closing_doors":
            self.__transition["w"] += self.__transition["speed"] * self.__transition["direction"]
            self.__transition["x"] -= self.__transition["speed"] * self.__transition["direction"]

            if self.__transition["w"] > pyxel.width // 2 and self.__transition["direction"] == 1:
                self.__transition["direction"] = -1
                self.change_scene(self.__transition["new_scene_id"], self.__transition["new_camera_x"], self.__transition["new_camera_y"], self.__transition["action"])
            if self.__transition["w"] < 0 and self.__transition["direction"] == -1:
                self.__transition = {}
                return
            pyxel.rect(self.__cam_x, self.__cam_y, self.__transition["w"], pyxel.height, self.__transition["transition_color"])
            pyxel.rect(self.__transition["x"], self.__cam_y, self.__transition["w"], pyxel.height, self.__transition["transition_color"])

        elif self.__transition.get("type") == "rectangle_right_left":
            self.__transition["w"] += self.__transition["speed"] * self.__transition["direction"]
            if self.__transition["direction"] == 1:
                self.__transition["x"] -= self.__transition["speed"]

            if self.__transition["w"] > pyxel.width and self.__transition["direction"] == 1:
                self.__transition["direction"] = -1
                self.change_scene(self.__transition["new_scene_id"], self.__transition["new_camera_x"], self.__transition["new_camera_y"], self.__transition["action"])
            if self.__transition["w"] < 0 and self.__transition["direction"] == -1:
                self.__transition = {}
                return
            pyxel.rect(self.__transition["x"], self.__cam_y, self.__transition["w"], pyxel.height, self.__transition["transition_color"])

        elif self.__transition.get("type") == "rectangle_left_right":
            self.__transition["w"] += self.__transition["speed"] * self.__transition["direction"]
            if self.__transition["direction"] == -1:
                self.__transition["x"] += self.__transition["speed"]

            if self.__transition["w"] > pyxel.width and self.__transition["direction"] == 1:
                self.__transition["direction"] = -1
                self.change_scene(self.__transition["new_scene_id"], self.__transition["new_camera_x"], self.__transition["new_camera_y"], self.__transition["action"])
            if self.__transition["w"] < 0 and self.__transition["direction"] == -1:
                self.__transition = {}
                return
            pyxel.rect(self.__transition["x"], self.__cam_y, self.__transition["w"], pyxel.height, self.__transition["transition_color"])

        elif self.__transition.get("type") == "outer_circle":
            self.__transition["end"] -= self.__transition["speed"] * self.__transition["direction"]

            if self.__transition["end"] < 0 and self.__transition["direction"] == 1:
                self.__transition["direction"] = -1
                self.change_scene(self.__transition["new_scene_id"], self.__transition["new_camera_x"], self.__transition["new_camera_y"], self.__transition["action"])
            if self.__transition["end"] > self.__transition["start_end"] and self.__transition["direction"] == -1:
                self.__transition = {}
                return
            
            for radius in range(self.__transition["start_end"], self.__transition["end"], -1):
                pyxel.ellib(self.__cam_x + pyxel.width / 2 - radius, self.__cam_y + pyxel.height / 2 - radius, radius * 2, radius * 2, self.__transition["transition_color"])
                pyxel.ellib(self.__cam_x + pyxel.width / 2 - radius + 1, self.__cam_y + pyxel.height / 2 - radius, radius * 2, radius * 2, self.__transition["transition_color"])

        elif self.__transition.get("type") == "triangle":
            self.__transition["size"] += self.__transition["speed"] * self.__transition["direction"]
            self.__transition["angle"] += self.__transition["rotation_speed"] * self.__transition["direction"]

            if self.__transition["size"] / 2.5 > max(pyxel.width, pyxel.height) and self.__transition["direction"] == 1:
                self.__transition["direction"] = -1
                self.change_scene(self.__transition["new_scene_id"], self.__transition["new_camera_x"], self.__transition["new_camera_y"], self.__transition["action"])
            if self.__transition["size"] < 0 and self.__transition["direction"] == -1:
                self.__transition = {}
                return
            d = math.sqrt(3) / 3 * self.__transition["size"]
            x1, y1 = self.__cam_x + pyxel.width / 2 + d * math.cos(math.radians(0 + self.__transition["angle"])), self.__cam_y + pyxel.height / 2 + d * math.sin(math.radians(0 + self.__transition["angle"]))
            x2, y2 = self.__cam_x + pyxel.width / 2 + d * math.cos(math.radians(120 + self.__transition["angle"])), self.__cam_y + pyxel.height / 2 + d * math.sin(math.radians(120 + self.__transition["angle"]))
            x3, y3 = self.__cam_x + pyxel.width / 2 + d * math.cos(math.radians(240 + self.__transition["angle"])), self.__cam_y + pyxel.height / 2 + d * math.sin(math.radians(240 + self.__transition["angle"]))
            pyxel.tri(x1, y1, x2, y2, x3, y3, self.__transition["transition_color"])

    def update(self):
        self.__cam_x += (self.__cam_tx - self.__cam_x) * 0.1
        self.__cam_y += (self.__cam_ty - self.__cam_y) * 0.1

        if self.__shake_amount > 0:
            amount = int(self.__shake_amount)
            pyxel.camera(self.__cam_x + random.uniform(-amount, amount), self.__cam_y + random.uniform(-amount, amount))
            self.__shake_amount -= self.__sub_shake_amount
        else:
            pyxel.camera(self.__cam_x, self.__cam_y)

        if not self.__transition.get("type"):
            self.__current_scene.update()

    def draw(self):
        self.__current_scene.draw()
        if self.__transition:
            self.handle_transitions()

    def run(self):
        pyxel.run(self.update, self.draw)

class Scene:

    def __init__(self, id:int, title:str, update, draw, pyxres_path:str=None, palette:list=PALETTE, screen_mode:int=0):
        self.id = id
        self.title = title
        self.update = update
        self.draw = draw
        self.pyxres_path = pyxres_path
        self.palette = palette
        self.screen_mode = screen_mode

class Text:

    def __init__(self, text:str, x:int, y:int, text_colors:int|list, font_size:int=0, anchor:int=ANCHOR_TOP_LEFT, relative:bool=False, color_mode:int=NORMAL_COLOR_MODE, color_speed:int=5, wavy:bool=False, wave_speed:int=10, amplitude:int=3, shadow:bool=False, shadow_color:int=0, shadow_offset:int=1, glitch_intensity:int=0):
        self.text = text
        self.x, self.y = x, y
        self.__font_size = font_size
        self.__anchor = anchor
        self.__relative = relative
        self.__wavy = wavy
        self.__wave_speed = wave_speed
        self.__amplitude = amplitude
        self.__shadow = shadow
        self.__shadow_color = shadow_color
        self.__shadow_offset = shadow_offset
        self.__glitch_intensity = glitch_intensity

        self.__text_colors = [text_colors] if isinstance(text_colors, int) else text_colors
        self.__original_text_colors = [x for x in self.__text_colors]
        self.__color_mode = color_mode
        self.__color_speed = color_speed
        self.__last_change_color_time = pyxel.frame_count

        _, text_height = text_size(text, font_size)
        _, self.y = get_anchored_position(0, y, 0, text_height, anchor)

    def __draw_line(self, text:str, y:int, camera_x:int=0, camera_y:int=0):
        text_width, _ = text_size(text, self.__font_size)
        x, _ = get_anchored_position(self.x, 0, text_width, 0, self.__anchor)

        if self.__relative:
            x += camera_x
            y += camera_y

        if self.__shadow:
            Text(text, x + self.__shadow_offset, y + self.__shadow_offset, self.__shadow_color, self.__font_size, wavy=self.__wavy, wave_speed=self.__wave_speed, amplitude=self.__amplitude).draw()

        if self.__font_size > 0:
            for char_index, char in enumerate(text):
                    x += random.uniform(-self.__glitch_intensity, self.__glitch_intensity)
                    char_y = y + math.cos(pyxel.frame_count / self.__wave_speed + char_index * 0.3) * self.__amplitude if self.__wavy else y
                    char_y += random.uniform(-self.__glitch_intensity, self.__glitch_intensity)

                    if char in characters_matrices:
                        char_matrix = characters_matrices[char]
                        char_width = len(char_matrix[0]) * self.__font_size
                        
                        for row_index, row in enumerate(char_matrix):
                            for col_index, pixel in enumerate(row):
                                if pixel:
                                    pyxel.rect(x + col_index * self.__font_size, char_y + row_index * self.__font_size + (1 * self.__font_size if char in "gjpqy" else 0), self.__font_size, self.__font_size, self.__text_colors[char_index % len(self.__text_colors)])
                        
                        x += char_width + 1
        else:
            for char_index, char in enumerate(text):
                x += random.uniform(-self.__glitch_intensity, self.__glitch_intensity)
                char_y = y + math.cos(pyxel.frame_count / self.__wave_speed + char_index * 0.3) * self.__amplitude if self.__wavy else y
                char_y += random.uniform(-self.__glitch_intensity, self.__glitch_intensity)
                pyxel.text(x, char_y, char, self.__text_colors[char_index % len(self.__text_colors)])
                x += 4

    def update(self):
        if self.__color_mode != NORMAL_COLOR_MODE and pyxel.frame_count - self.__last_change_color_time >= self.__color_speed:
            if self.__color_mode == ROTATING_COLOR_MODE:
                self.__last_change_color_time = pyxel.frame_count
                self.__text_colors = [self.__text_colors[-1]] + self.__text_colors[:-1]
            elif self.__color_mode == RANDOM_COLOR_MODE:
                self.__last_change_color_time = pyxel.frame_count
                self.__text_colors = [random.choice(self.__original_text_colors) for _ in range(len(self.text))]

    def draw(self, camera_x:int=0, camera_y:int=0):
        if "\n" in self.text:
            lines = self.text.split("\n")
            for i, line in enumerate(lines):
                if self.__font_size > 0:
                    self.__draw_line(line, self.y + i * (9 * self.__font_size), camera_x, camera_y)
                else:
                    self.__draw_line(line, self.y + i * 6, camera_x, camera_y)
        else:
            self.__draw_line(self.text, self.y, camera_x, camera_y)

class Button:

    def __init__(self, text:str, x:int, y:int, background_color:int, text_colors:list|int, hover_background_color:int, hover_text_colors:list|int, font_size:int=1, border:bool=False, border_color:int=0, color_mode:int=NORMAL_COLOR_MODE, color_speed:int=10, relative:bool=True, anchor:int=ANCHOR_TOP_LEFT, command=None):
        self.__x = x
        self.__y = y
        self.__width, self.__height = text_size(text, font_size)
        self.__width += 4 if border else 2
        self.__height += 4 if border else 2
        self.__background_color = background_color
        self.__hover_background_color = hover_background_color
        self.__border = border
        self.__border_color = border_color
        self.__relative = relative
        self.__command = command

        self.__x, self.__y = get_anchored_position(self.__x, self.__y, self.__width, self.__height, anchor)

        self.__text = Text(text, self.__x + 2 if border else self.__x + 1, self.__y + 2 if border else self.__y + 1, text_colors, font_size, color_mode=color_mode, color_speed=color_speed, relative=relative)
        self.__hover_text = Text(text, self.__x + 2 if border else self.__x + 1, self.__y + 2 if border else self.__y + 1, hover_text_colors, font_size, color_mode=color_mode, color_speed=color_speed, relative=relative)

    def is_hovered(self, camera_x:int=0, camera_y:int=0)-> bool:
        if self.__x <= pyxel.mouse_x < self.__x + self.__width and self.__y <= pyxel.mouse_y < self.__y + self.__height and self.__relative:
            return True
        if self.__x <= camera_x + pyxel.mouse_x < self.__x + self.__width and self.__y <= camera_y + pyxel.mouse_y < self.__y + self.__height and not self.__relative:
            return True
        
    def update(self, camera_x:int=0, camera_y:int=0):
        self.__text.update()
        self.__hover_text.update()
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and self.is_hovered(camera_x, camera_y) and self.__command:
            self.__command()

    def draw(self, camera_x:int=0, camera_y:int=0):
        x = camera_x + self.__x if self.__relative else self.__x
        y = camera_y + self.__y if self.__relative else self.__y
        if self.is_hovered(camera_x, camera_y):
            pyxel.rect(x, y, self.__width, self.__height, self.__hover_background_color)
            self.__hover_text.draw(camera_x, camera_y)
        else:
            pyxel.rect(x, y, self.__width, self.__height, self.__background_color)
            self.__text.draw(camera_x, camera_y)
        if self.__border:
            pyxel.rectb(x, y, self.__width, self.__height, self.__border_color)

def get_anchored_position(x:int, y:int, width:int, height:int, anchor:int)-> tuple:
    if anchor in [ANCHOR_TOP_RIGHT, ANCHOR_BOTTOM_RIGHT, ANCHOR_RIGHT]:
        x -= width
    if anchor in [ANCHOR_BOTTOM_LEFT, ANCHOR_BOTTOM_RIGHT, ANCHOR_BOTTOM]:
        y -= height
    if anchor in [ANCHOR_TOP, ANCHOR_BOTTOM, ANCHOR_CENTER]:
        x -= width // 2
    if anchor in [ANCHOR_LEFT, ANCHOR_RIGHT, ANCHOR_CENTER]:
        y -= height // 2

    return x, y

def text_size(text:str, font_size:int=1)-> tuple:
    lines = text.split("\n")
    if font_size == 0:
        return (max(len(line) * 4 for line in lines), 6 * len(lines))
    text_width = max(sum(len(characters_matrices[char][0]) * font_size + 1 for char in line) - 1 for line in lines)
    text_height = (9 * font_size + 1) * len(lines)

    return (text_width, text_height)

def rounded_rect(x:int, y:int, width:int, height:int, corner_radius:int, color:int):
    corner_radius = min(corner_radius, min(width, height) // 2)
    corner_radius = int(corner_radius)

    pyxel.rect(x + corner_radius, y, width - 2 * corner_radius, height, color)
    pyxel.rect(x, y + corner_radius, width, height - 2 * corner_radius, color)
    
    for cx, cy, sx, sy in [(x + corner_radius, y + corner_radius, -1, -1), (x + width - corner_radius - 1, y + corner_radius, 1, -1), (x + corner_radius, y + height - corner_radius - 1, -1, 1), (x + width - corner_radius - 1, y + height - corner_radius - 1, 1, 1)]:
        for i in range(corner_radius + 1):
            for j in range(corner_radius + 1):
                if i*i + j*j <= corner_radius*corner_radius:
                    pyxel.pset(cx + sx * i, cy + sy * j, color)

def rounded_rectb(x:int, y:int, width:int, height:int, corner_radius:int, color:int):
    corner_radius = min(corner_radius, min(width, height) // 2)

    pyxel.line(x + corner_radius, y, x + width - corner_radius - 1, y, color)
    pyxel.line(x + corner_radius, y + height - 1, x + width - corner_radius - 1, y + height - 1, color)
    pyxel.line(x, y + corner_radius, x, y + height - corner_radius - 1, color)
    pyxel.line(x + width - 1, y + corner_radius, x + width - 1, y + height - corner_radius - 1, color)
    
    for cx, cy, sx, sy in [(x + corner_radius, y + corner_radius, -1, -1), (x + width - corner_radius - 1, y + corner_radius, 1, -1), (x + corner_radius, y + height - corner_radius - 1, -1, 1), (x + width - corner_radius - 1, y + height - corner_radius - 1, 1, 1)]:
        for i in range(corner_radius + 1):
            for j in range(corner_radius + 1):
                dist = math.sqrt(i*i + j*j)
                if corner_radius - 0.5 <= dist <= corner_radius + 0.5:
                    pyxel.pset(cx + sx * i, cy + sy * j, color)

# -------------------- CLASSES -------------------- #

class Room:

    def __init__(self, width:int, height:int, tiles:list):
        self.width = width
        self.height = height
        self.tiles = tiles

class Player:

    def __init__(self):
        pass

# -------------------- FUNCTIONS -------------------- #

def make_basic_room(width:int, height:int, wall_tile:tuple, floor_tile:tuple)-> Room:
    tiles = []
    for y in range(height):
        row = []
        for x in range(width):
            if x == 0 or y == 0 or x == width-1 or y == height-1:
                row.append(wall_tile)
            else:
                row.append(floor_tile)
        tiles.append(row)
    return Room(width, height, tiles)

def mark_room(room:Room, ox:int, oy:int, occupied_tiles:set)-> set:
    ox += 1
    oy += 1
    for y in range(room.height - 2):
        for x in range(room.width - 2):
            occupied_tiles.add((ox + x, oy + y))

    return occupied_tiles

def check_room_collision(room:Room, ox:int, oy:int, occupied_tiles:set):
    for y in range(room.height):
        for x in range(room.width):
            pos = (ox + x, oy + y)
            if pos in occupied_tiles:
                return True
    return False

def draw_room(room:Room, ox:int, oy:int, direction:str=""):
    for y in range(room.height):
        for x in range(room.width):
            u, v = room.tiles[y][x]
            pyxel.tilemaps[0].pset(ox + x, oy + y, (u, v))

    if direction == "N":
        cx = ox + room.width // 2
        for dx in (-1, 0, 1):
            pyxel.tilemaps[0].pset(cx + dx, oy, (0, 2))
    elif direction == "S":
        cx = ox + room.width // 2
        for dx in (-1, 0, 1):
            pyxel.tilemaps[0].pset(cx + dx, oy + room.height - 1, (0, 2))
    elif direction == "W":
        cy = oy + room.height // 2
        for dy in (-1, 0, 1):
            pyxel.tilemaps[0].pset(ox, cy + dy, (0, 2))
    elif direction == "E":
        cy = oy + room.height // 2
        for dy in (-1, 0, 1):
            pyxel.tilemaps[0].pset(ox + room.width - 1, cy + dy, (0, 2))

def place_next_room(curr_room:Room, curr_pos:tuple, next_room:Room, direction:str):
    x, y = curr_pos
    x_diff = (curr_room.width - next_room.width) // 2
    y_diff = (curr_room.height - next_room.height) // 2

    if direction == "E":
        return (x + curr_room.width - 1, y + y_diff)
    if direction == "W":
        return (x - next_room.width + 1, y + y_diff)
    if direction == "S":
        return (x + x_diff, y + curr_room.height - 1)
    if direction == "N":
        return (x + x_diff, y - next_room.height + 1)

def generate_dungeon(start_room:Room, end_room:Room, fill_rooms:list, special_rooms:list, num_main_rooms:int, num_branches:int, branch_length:int, ox:int=100, oy:int=100):
    x, y = ox, oy
    curr_room = start_room
    curr_dir = ""
    draw_room(start_room, x, y)
    next_dir = ""
    occupied_tiles = set()
    occupied_tiles = mark_room(curr_room, x, y, occupied_tiles)

    xs = [x, x + curr_room.width]
    ys = [y, y + curr_room.height]

    placed_rooms = 1
    placed = [(curr_room, x, y, "")]
    count_1 = 0
    while placed_rooms < num_main_rooms and count_1 < 50:
        count_1 += 1

        next_dir = random.choice([d for d in ["N","S","E","W"] if d != CARDINAL_OPPOSITE.get(curr_dir)])
        next_room = random.choice(fill_rooms) if placed_rooms < num_main_rooms - 1 else end_room
        next_x, next_y = place_next_room(curr_room, (x, y), next_room, next_dir)

        count_2 = 0
        while check_room_collision(next_room, next_x, next_y, occupied_tiles) and count_2 < 10:
            next_dir = random.choice([d for d in ["N","S","E","W"] if d != CARDINAL_OPPOSITE.get(curr_dir)])
            next_room = random.choice(fill_rooms) if placed_rooms < num_main_rooms - 1 else end_room
            next_x, next_y = place_next_room(curr_room, (x, y), next_room, next_dir)
            count_2 += 1

        if check_room_collision(next_room, next_x, next_y, occupied_tiles):
            continue

        x, y = next_x, next_y
        xs += [x, x + curr_room.width]
        ys += [y, y + curr_room.height]
        draw_room(next_room, x, y, CARDINAL_OPPOSITE.get(next_dir))
        curr_room = next_room
        curr_dir = next_dir
        occupied_tiles = mark_room(curr_room, x, y, occupied_tiles)
        placed.append((curr_room, x, y, curr_dir))
        placed_rooms += 1

    placed_branches = 0
    count_3 = 0
    while placed_branches < num_branches and count_3 < 50:
        count_3 += 1
        anchor_room, ax, ay, anchor_dir = random.choice(placed[1:-1])

        branch_dir = random.choice([d for d in ["N","S","E","W"] if d not in (anchor_dir, CARDINAL_OPPOSITE.get(anchor_dir))])

        bx, by = ax, ay
        curr_branch_room = anchor_room
        curr_branch_dir = branch_dir

        branch_placed = False
        for i in range(branch_length):
            if i == branch_length - 1:
                next_room = random.choice(special_rooms)
            else:
                next_room = random.choice(fill_rooms)

            next_bx, next_by = place_next_room(curr_branch_room, (bx, by), next_room, curr_branch_dir)

            if check_room_collision(next_room, next_bx, next_by, occupied_tiles):
                continue

            bx, by = next_bx, next_by
            draw_room(next_room, bx, by, CARDINAL_OPPOSITE.get(curr_branch_dir))
            occupied_tiles = mark_room(next_room, bx, by, occupied_tiles)

            xs += [bx, bx + next_room.width]
            ys += [by, by + next_room.height]

            curr_branch_room = next_room
            if i < branch_length - 1:
                curr_branch_dir = random.choice([d for d in ["N","S","E","W"] if d != CARDINAL_OPPOSITE.get(curr_branch_dir)])

            branch_placed = True

        placed_branches += 1 if branch_placed else 0

    return (min(xs), min(ys), max(xs), max(ys))

def get_neighbors(x:int, y:int):
    n = 0
    if pyxel.tilemaps[0].pget(x, y - 1) == (1, 0):
        n += 1
    if pyxel.tilemaps[0].pget(x + 1, y) == (1, 0):
        n += 2
    if pyxel.tilemaps[0].pget(x, y + 1) == (1, 0):
        n += 4
    if pyxel.tilemaps[0].pget(x - 1, y) == (1, 0):
        n += 8

    return n

def place_walls(min_x:int, min_y:int, max_x:int, max_y:int):
    walls = []
    for y in range(min_y, max_y):
        for x in range(min_x, max_x):
            neighbors = get_neighbors(x, y)
            if pyxel.tilemaps[0].pget(x, y) == (1, 0):
                walls.append((x, y, neighbors))

    for x, y, neighbors in walls:
        pyxel.tilemaps[0].pset(x, y, (neighbors, 1))

# -------------------- GAME -------------------- #

class Game:

    def __init__(self):
        main_menu_scene = Scene(0, "CrumbleKeep - Main Menu", self.update_main_menu, self.draw_main_menu, "assets.pyxres")
        credits_scene = Scene(1, "CrumbleKeep - Credits", self.update_credits, self.draw_credits, "assets.pyxres")
        lobby_scene = Scene(2, "CrumbleKeep - Lobby", self.update_lobby, self.draw_lobby, "assets.pyxres")
        game_scene = Scene(3, "CrumbleKeep - Game", self.update_game, self.draw_game, "assets.pyxres")
        scenes = [main_menu_scene, credits_scene, lobby_scene, game_scene]

        self.pyxel_manager = PyxelManager(228, 128, scenes, 3, fullscreen=True, mouse=True, camera_x=800 - 228 // 2, camera_y=800 - 128 // 2)

        self.title = Text("CrumbleKeep", 50, 10, 6, 1, ANCHOR_TOP)
        self.play_button = Button("Play", 50, 50, 0, 6, 6, 0, 1, True, 6, anchor=ANCHOR_TOP, command=self.play_action)
        self.credits_button = Button("Credits", 50, 70, 0, 6, 6, 0, 1, True, 6, anchor=ANCHOR_TOP, command=self.credit_action)

        self.credits_title = Text("Credits", 55, 7, 6, 1, ANCHOR_TOP)
        self.credits_text = Text("This game was\nmade for the\nBrackeys game\njam 2025 by\nLéo Imbert\nand\nHugochavez\nwith Pyxel.", 55, 70, 6, 1, anchor=ANCHOR_CENTER)
        self.back_button = Button("Back", 55, 121, 0, 6, 6, 0, 1, True, 6, anchor=ANCHOR_BOTTOM, command=self.back_action)

        self.start_room = make_basic_room(5, 5, (1, 0), (1, 2))
        self.end_room = make_basic_room(5, 5, (1, 0), (2, 2))
        self.special_room = make_basic_room(5, 5, (1, 0), (3, 2))
        self.rooms = [make_basic_room(7, 7, (1, 0), (0, 2)), make_basic_room(15, 7, (1, 0), (0, 2)), make_basic_room(17, 13, (1, 0), (0, 2))]
        self.min_x, self.min_y, self.max_x, self.max_y = generate_dungeon(self.start_room, self.end_room, self.rooms, [self.special_room], 10, 3, 4)
        place_walls(self.min_x, self.min_y, self.max_x + 10, self.max_y + 10)

        self.pyxel_manager.run()

    def play_action(self):
        self.pyxel_manager.change_scene_dither(2, 0.05, 0)

    def credit_action(self):
        self.pyxel_manager.change_scene_dither(1, 0.05, 0)

    def back_action(self):
        self.pyxel_manager.change_scene_dither(0, 0.05, 0)

    def update_main_menu(self):
        self.title.update()
        self.play_button.update()
        self.credits_button.update()

    def draw_main_menu(self):
        pyxel.cls(6)

        rounded_rect(5, 5, 90, 118, 10, 0)
        self.title.draw()
        self.play_button.draw()
        self.credits_button.draw()

    def update_credits(self):
        self.credits_title.update()
        self.credits_text.update()
        self.back_button.update()

    def draw_credits(self):
        pyxel.cls(6)

        rounded_rect(5, 5, 100, 118, 10, 0)
        self.credits_title.draw()
        self.credits_text.draw()
        self.back_button.draw()

    def update_lobby(self):
        pass

    def draw_lobby(self):
        pyxel.cls(0)

    def update_game(self):
        if pyxel.btnp(pyxel.KEY_R):
            self.pyxel_manager.change_scene(3, 800 - 228 // 2, 800 - 128 // 2)
            self.min_x, self.min_y, self.max_x, self.max_y = generate_dungeon(self.start_room, self.end_room, self.rooms, [self.special_room], 10, 3, 4)
            place_walls(self.min_x, self.min_y, self.max_x + 10, self.max_y + 10)

        if pyxel.btn(pyxel.KEY_LEFT):
            self.pyxel_manager.set_camera(self.pyxel_manager.camera_x - 5, self.pyxel_manager.camera_y)
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.pyxel_manager.set_camera(self.pyxel_manager.camera_x + 5, self.pyxel_manager.camera_y)
        if pyxel.btn(pyxel.KEY_UP):
            self.pyxel_manager.set_camera(self.pyxel_manager.camera_x, self.pyxel_manager.camera_y - 5)
        if pyxel.btn(pyxel.KEY_DOWN):
            self.pyxel_manager.set_camera(self.pyxel_manager.camera_x, self.pyxel_manager.camera_y + 5)

    def draw_game(self):
        pyxel.cls(1)

        pyxel.bltm(0, 0, 0, 0, 0, (self.max_x + 10) * 8, (self.max_y + 10) * 8, 0)

if __name__ == "__main__":
    Game()