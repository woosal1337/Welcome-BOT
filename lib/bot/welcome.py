from PIL import ImageFont, ImageDraw, Image
import cv2
import numpy as np
import time
from os import listdir
from os.path import isfile, join


def welcomeXD(nickname="WOOSAL"):
    text_to_show = "Welcome"

    W, H = (1000, 400)
    image = cv2.imread("Backgrounds/templatefaded.png")
    cv2_im_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pil_im = Image.fromarray(cv2_im_rgb)

    font = ImageFont.truetype("Fonts/KDA.ttf", 25)
    Font = ImageFont.truetype("Fonts/KDA.ttf", 85)
    draw = ImageDraw.Draw(pil_im)

    w, h = draw.textsize(text_to_show, font=font)
    nickNamew, nickNameh = draw.textsize(nickname, font=Font)

    draw.text(((W - w) / 2, (H - h - 200) / 2), text_to_show, fill="black", font=font)
    draw.text(((W - nickNamew) / 2, (H - nickNameh + 50) / 2), nickname, fill="black", font=Font)

    cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)
    cv2.imwrite(f"Output/{nickname}.png", cv2_im_processed)
    cv2.imshow('Fonts', cv2_im_processed)
    #cv2.waitKey(0)

    cv2.destroyAllWindows()