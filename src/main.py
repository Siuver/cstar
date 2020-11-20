import os
import tkinter as tk

from map import MAP_CONFIG
from mytk import MyTk

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
IMG_PATH = os.path.join(ROOT_DIR, "../img/cao.png")

def main():
    window = MyTk(MAP_CONFIG)

if __name__ == "__main__":
    main()