from bs4 import BeautifulSoup
import requests
import random
import keyboard
import pyperclip



ls = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"]

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

while True:


    link = ''.join(random.choices(ls, k=5))
    url = r"https://prnt.sc/" + link



    req = requests.get(url, headers=headers)

    soup = BeautifulSoup(req.text, "html.parser")
    x=soup.find_all('img')

    ss = '//st.prntscr.com/2021/04/08/1538/img/0_173a7b_211be8ff.png' in str(x)

    if link[0] == '0':
        ss=True
        


    if  ss == False:


        file=open("images.txt","r")
        contenu=" ".join(file.read().split('\n')).split(" ")
        file.close()

        if url not in contenu:

            f = open('images.txt', "a")
            f.write(url)
            f.write('\n')
            f.close()
            print(url)
            pyperclip.copy(url)
