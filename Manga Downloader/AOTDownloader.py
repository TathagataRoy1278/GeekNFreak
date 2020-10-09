
site = "https://readshingekinokyojin.com/manga/shingeki-no-kyojin-chapter-"

import os
import requests
import bs4
from urllib.request import urlopen
import urllib.request
import traceback

try:
    for i in range(5):
        ctr = i+1
        link = site+str(ctr)
        page = requests.get(link)
        soup = bs4.BeautifulSoup(page.content,"html.parser")
        imgs = soup.find_all("img")
        save_directory = "/home/tatan/Desktop/Godot/Test/AOT/"+str(ctr)+"/"
        print("changing directory to "+save_directory)
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)
        for i in imgs:
            src = i['src']
            if("?" in src):
               src = src[:src.index('?')]
               imgname = src.split("/")[-1]
               if(len(imgname)==12):
                   print(src)
                   if not os.path.exists(save_directory+imgname):
                       req = requests.get(src, headers={'User-Agent': 'Mozilla/5.0'})
                       im = req.content
                       file = open(save_directory+imgname,"wb")
                       file.write(im)
                       file.flush()
                   print("done")
except:
    traceback.print_exc()
    pass
