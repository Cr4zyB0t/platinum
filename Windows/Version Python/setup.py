#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

def verif_root():
    if os.name == "nt":
        pass
    else:
        if os.geteuid() != 0:
            sys.exit("[!] Veuillez lancer l'application en mode root!")

verif_root()
def verif_python3():
    version = sys.version[:1]
    if int(version) == 3:
        pass
    else:
        sys.exit("[!] Veuillez lancer la version 3 de python!")
verif_python3()


def pip_installer():
    cmd1 = "sudo pip3 install tabulate"
    cmd2 = "sudo pip3 install terminaltables"
    cmd3 = "sudo pip3 install colorama"

    os.system(cmd1)
    os.system(cmd2)
    os.system(cmd3)

def apt_installer():
    cmd = """sudo apt-get install python-pip python3-pip nmap hping3 build-essential ruby-dev libpcap-dev libgmp3-dev python3-bs4 python3-requests -y"""
    if os.name == "nt":
        pass
    else:
        os.system(cmd)
def apt_whois():
    cmd = "sudo apt-get install whois -y"
    os.system(cmd)
apt_installer()
pip_installer()
apt_whois()
apt_installer()
