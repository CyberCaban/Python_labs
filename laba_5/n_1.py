import os
from typing import Tuple, Any

from PIL import Image, ImageEnhance, ImageDraw


def is_file(path):
    if not os.path.exists(path):
        raise Exception(f"File {path} not found")


try:
    is_file(img_src := input("Enter path to image: "))
except Exception as inst:
    exit(inst)

def addFigure(image: Image) -> Image:
    while True:
        draw = ImageDraw.Draw(im)
        figure = input("Enter figure(ellipse, rectangle, line, arc or exit): ")
        match figure:
            case "ellipse":
                coords = inputCoords()
                draw.ellipse(coords, fill="red", width=5)
            case "rectangle":
                coords = inputCoords()
                draw.rectangle(coords, fill="red", width=5)
            case "line":
                coords = inputCoords()
                draw.line(coords, fill="red", width=5)
            case "arc":
                coords = inputCoords()
                draw.arc(coords, start=0, end=180, fill="red", width=5)
            case "exit":
                return image
            case _:
                print("Invalid figure")

def addText(image: Image) -> Image:
    pos = input("Enter position: ").split(" ")
    pos = tuple(map(int, pos))

    if len(pos) != 2:
        print("Invalid input")
        addText(image)

    text = input("Enter text: ")
    ImageDraw.Draw(im).text(pos, text, fill="red")
    return image
    
def inputCoords():
    try:
        coords = tuple(map(int, input("Enter coords: ").split()))
        if len(coords) != 4 or coords[0] > coords[2] or coords[1] > coords[3]:
            print("Invalid coords")
            return inputCoords()
        return coords
    except Exception as inst:
        exit(inst)


def sepia(image: Image) -> Image:
    pixels = image.load()
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = pixels[i, j]
            new_r = int((r * 0.393) + (g * 0.769) + (b * 0.189))
            new_g = int((r * 0.349) + (g * 0.686) + (b * 0.168))
            new_b = int((r * 0.272) + (g * 0.534) + (b * 0.131))
            pixels[i, j] = (new_r, new_g, new_b)
    return image


def median(image: Image) -> tuple[int | Any, int | Any, int | Any]:
    pixels = image.load()
    pixels_amount = image.size[0] * image.size[1]
    rs, gs, bs = 0, 0, 0
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = pixels[i, j]
            rs += r
            gs += g
            bs += b

    return rs // pixels_amount, gs // pixels_amount, bs // pixels_amount


while True:
    act = input("\n1 - mirror vertical\n"
                "2 - mirror horizontal\n"
                "3 - mirror diagonal\n"
                "4 - mirror secondary diagonal\n"
                "5 - sepia\n"
                "6 - brightness\n"
                "7 - median color \n"
                "8 - add text\n"
                "9 - add figure\n"
                "10 - exit\n")

    match act:
        case "1":
            im = Image.open(img_src)
            im = im.transpose(Image.FLIP_TOP_BOTTOM)
            im.save("new_img.jpg")
        case "2":
            im = Image.open(img_src)
            im = im.transpose(Image.FLIP_LEFT_RIGHT)
            im.save("new_img.jpg")
        case "3":
            im = Image.open(img_src)
            im = im.transpose(Image.ROTATE_90)
            im.save("new_img.jpg")
        case "4":
            im = Image.open(img_src)
            im = im.transpose(Image.ROTATE_270)
            im.save("new_img.jpg")
        case "5":
            im = Image.open(img_src)
            im = sepia(im)
            im.save("new_img.jpg")
        case "6":
            im = Image.open(img_src)
            br_level = input("Enter brightness(0.0 is black, 1.0 is original): ")
            im = ImageEnhance.Brightness(im).enhance(float(br_level))
            im.save("new_img.jpg")
        case "7":
            im = Image.open(img_src)
            new_img = Image.new("RGB", im.size, (median(im)))
            new_img.save("new_img.jpg")
        case "8":
            im = Image.open(img_src)
            im = addText(im)
            im.save("new_img.jpg")
        case "9":
            im = Image.open(img_src)
            im = addFigure(im)
            im.save("new_img.jpg")
        case "10":
            exit()
        case _:
            print("Invalid input")
