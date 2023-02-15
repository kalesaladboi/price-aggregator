from bs4 import BeautifulSoup
from pprint import pprint
import json
import requests
import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *

urls = [
'https://www.sanmar.com/p/2716_CloverGrn?text=s608',
'https://www.sanmar.com/p/648_AthlGold?text=s608es',
'https://www.sanmar.com/p/751_UltramrnBl?text=tls608',
'https://www.sanmar.com/p/1694_DeepBerry?text=l608',
'https://www.sanmar.com/p/2383_RoyClsNvy?text=s508',
'https://www.sanmar.com/p/5682_DkGreenNv?text=tls508',
'https://www.sanmar.com/p/1441_UltramrnBl?text=l508',
'https://www.sanmar.com/p/2949_Charcoal?text=sp14',
'https://www.sanmar.com/p/5745_PetrolBlue?text=sp14long',
'https://www.sanmar.com/p/7_LightBlue?text=sp24',
'https://www.sanmar.com/p/5746_LightBlue?text=sp24long',
'https://www.sanmar.com/p/3832_Royal?text=k510',
'https://www.sanmar.com/p/5623_Navy?text=tlk510',
'https://www.sanmar.com/p/1225_StrongBlue?text=k500',
'https://www.sanmar.com/p/2274_Navy?text=tlk500',
'https://www.sanmar.com/p/1407_DeepBerry?text=l500',
'https://www.sanmar.com/p/112_CoolGrey?text=k500p',
'https://www.sanmar.com/p/5736_Royal?text=tlk500p',
'https://www.sanmar.com/p/1557_Burgundy?text=k500ls',
'https://www.sanmar.com/p/5735_CoolGrey?text=tlk500ls',
'https://www.sanmar.com/p/1362_Royal?text=l500ls',
'https://www.sanmar.com/p/3859_TrueNavy?text=st650',
'https://www.sanmar.com/p/5656_KellyGreen?text=tst650',
'https://www.sanmar.com/p/5494_Maroon?text=st651',
'https://www.sanmar.com/p/4042_Royal?text=cs410',
'https://www.sanmar.com/p/5687_DarkNavy?text=tlcs410',
'https://www.sanmar.com/p/4043_DarkNavy?text=cs411',
'https://www.sanmar.com/p/9068_DarkNavy?text=cs420',
'https://www.sanmar.com/p/5002_Tan?text=cs410ls',
'https://www.sanmar.com/p/8581_Scarlet?text=nea201',
'https://www.sanmar.com/p/4121_SnrklBlBk?text=j304',
'https://www.sanmar.com/p/4122_BlkBlk?text=l304',
'https://www.sanmar.com/p/1890_KhkTrBlk',
'https://www.sanmar.com/p/2874_TrBlkGrey?text=tlj754',
'https://www.sanmar.com/p/657_TNvGyHRf?text=j754r',
'https://www.sanmar.com/p/5214_CharChar?text=ne1020'
]

my_data= []



for url in urls:

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    prices = soup.find(class_='price').get_text()
    price = prices[15:20]
    newprice = "=" + price + "+8"
    colors = soup.find_all('span', attrs={'class':'swatch-name'})
    swatches = [color.get_text() for color in colors]
    style = soup.find(class_= 'product-style-number').get_text()
    my_data.append({"Style": style, "Color": swatches,"Price": price, "Newprice": newprice})
    pprint (style + " retrieved" )

path = "./pricing"

isExist = os.path.exists(path)
if not isExist:
    os.makedirs("./pricing")
    pprint("Pricing folder made")

json_object = json.dumps(my_data, indent=4)

with open(os.path.join("./pricing", "Clerk-Prices.json"), "w") as file:
    file.write(json_object)
    pprint("completed")