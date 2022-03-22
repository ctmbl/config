#!/usr/bin/python3
# coding: utf-8

import pytesseract
import os
import argparse

from requests_html import HTMLSession
import base64
from operator import itemgetter

try:
    import Image, ImageOps, ImageEnhance, imread
except ImportError:
    from PIL import Image, ImageOps, ImageEnhance

def solve_captcha(path):

    """
    Convert a captcha image into a text, 
    using PyTesseract Python-wrapper for Tesseract

    Arguments:
        path (str):
            path to the image to be processed
    Return:
        'textualized' image

    """
    image = Image.open(path).convert('RGB')
    image = ImageOps.autocontrast(image)
    image = image.convert("P")

    filename = "{}.png".format("/tmp/treated_img")
    image.save(filename)
    
    cleaned_img_path = "/tmp/recolored_img.png"

    print("Image size: ",image._size)
    
    ## CLEANING img
    hist =  image.histogram()
    #print(hist)
    values = {}
    
    for i in range(len(hist)):
        values[i] = hist[i]
    
    print("Top 10 colours")
    for j,k in sorted(values.items(), key=itemgetter(1), reverse=True)[:10]:
        print(j,k)

    ## new image
    image_cleaned = image.copy()
    for x in range(image_cleaned.size[0]):
        for y in range(image_cleaned.size[1]):
            if image.getpixel((x,y)) == 0:
                image_cleaned.putpixel((x,y),225)

    image_cleaned.save(cleaned_img_path)


    conf = r'-c tessedit_char_whitelist="azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN0123456789" --psm 6'

    text = pytesseract.image_to_string(Image.open(cleaned_img_path), config=conf)
    print(bytes(text,'utf-8'))
    print(text)
    return text

def pwn_it(url):
    session = HTMLSession()
    resp = session.get(url)
    html = resp.html.html
    #print(html)

    ## GETTING
    if "base64," not in html:
        print("[-] something went wrong, EXIT")
        exit(1)
    print("[+] eliminating trash to keep img")

    img_b64 = html.split("base64,")[1].split('"')[0]

    #print(img_b64)
    with open("/tmp/b64_img","w") as img_file:
        img_file.write(img_b64)
        img_file.close()
    print("[+] b64 ENcoded img written in /tmp/b64_img")

    ## DECODING
    img = base64.b64decode(bytes(img_b64,'utf_8'))
    #img = bytes(img_b64,'utf-8').decode('base64')

    with open("/tmp/decoded_img","wb") as img_file:
        img_file.write(img)
        img_file.close()
    print("[+] b64 DEcoded img written in /tmp/decoded_img")
    
    ## SOLVING
    text = solve_captcha("/tmp/decoded_img")
    print("[+] CAPTCHA solved")
    print("Text is: " + text)
    #text = input()
    #print(text)
    
    ## CLEANING
    print("[+] cleaning the text from pytesseract")
    cleaned_text = ""
    alphabet = 'azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN0123456789'
    for c in text:
        if c in alphabet:
           cleaned_text += c
    text = cleaned_text
    print(text,bytes(text,'utf-8'))

    ## RESPONDING
    post_data = {'cametu': text[:]}
    resp = session.post(url,data=post_data)
    print("[+] POST sent")
    if html == resp.html.html:
        print("[-] POST returned same object, EXIT")
        exit(1)
    
    ## PWNING
    print("[+] we had a response ! :")
    html = resp.html.html
    if "retente ta chance" in html:
        print(html.split("p>")[1])
    else:
        print(html)
    #print(pytesseract.image_to_osd(Image.open("/tmp/treated_img.png")))


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-u", "--url", help="url of the chall with the captcha")
    argparser.add_argument("-i", "--img", help="specified a path to an img")
    args = vars(argparser.parse_args())
    url = args["url"]
    path = args["img"]
    if path:
        print('-- Resolving')
        captcha_text = solve_captcha(path)
        print('-- Result: {}'.format(captcha_text))
    elif url:
        print("[+] url is: " + url)
        pwn_it(url)
    else:
        print("[+] give at least a path (-i <path>) or an url (-u <url>)")
