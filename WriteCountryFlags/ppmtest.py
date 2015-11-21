__author__ = 'Nadia Aly'
from ppmimageadt import PPMImage
import os

def main():
    """main method for flag and console interactions; could call each individually but
       using book code
    """
    print("We are using this tool to make some country flags!")
    print("Flag code: 0 -- French flag, 1 -- German flag, 2 -- Lithuanian Flag")
    cc = int(input("Entry the flag code: "))
    width = int(input("Image width in pixels (such as 300): "))
    make_flag(cc, width)


def make_flag(cc, width):
    assert width > 100, "Flag width needs to be at least 100 pixels"
    if cc == 0:
        make_french_flag(width)
    elif cc == 1:
        make_german_flag(width)
    elif cc == 2:
        make_lithuanian_flag(width)
    else:
        print("Not a valid country flag code")


def make_french_flag(width):
    height = width * 2 // 3
    # print(width, height)
    flag = PPMImage(width, height)
    for i in range(height):
        for j in range(width):
            if j < width // 3:
                flag[i, j] = 0, 85, 164  # r,g,b
            elif j < 2 * width // 3:
                flag[i, j] = 255, 255, 255
            else:
                flag[i, j] = 250, 60, 50
    flag.writeToFile("france.ppm")


def make_german_flag(width):
    height = width * 2 // 3
    flag = PPMImage(width, height)
    for i in range(height):
        for j in range(width):
            if j < width // 3:
                flag[i, j] = 0, 0, 0
            elif j < 2 * width // 3:
                flag[i, j] = 255, 0, 0
            else:
                flag[i, j] = 250, 204, 50
    flag.writeToFile("german.ppm")


def make_lithuanian_flag(width):
    height = width * 2 // 3
    flag = PPMImage(width, height)
    for i in range(height):
        for j in range(width):
            if j < width // 3:
                flag[i, j] = 253, 106, 19  # r, g, b
            elif j < 2 * width // 3:
                flag[i, j] = 0, 106, 68
            else:
                flag[i, j] = 193, 68, 45
    flag.writeToFile("lithuanian.ppm")

main()