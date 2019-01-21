# -*- coding: utf-8 -*-
import os
import sys
def homebrew():
    cmd = """/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"""
    os.system(cmd)
def verif_root():
    if os.geteuid() != 0:
        sys.exit("[!] Veuillez lancer l'application en mode root!")
    else:
        pass

verif_root()
homebrew()


def package():
    cmd1 = "brew install nmap whois git python3 ruby-dev wget"
    os.system(cmd1)
    
    cmd2 = "pip3 install terminaltables tabulate bs4 colorama requests"
    os.system(cmd2)

try:
    package()
except KeyboardInterrupt:
    pass