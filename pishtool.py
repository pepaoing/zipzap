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
    red()
    # hola
    print("                                  1 > Campish")
    print("                                  2 > Phishing")
    print("              |                   99 > Exit")    
    option = input("              > ")

    if option == "1":
        campish()

    if option == "2":
        phishing()

    if option == "99":
        os.system("clear")
        exit()

#   <--Return to Menu-->
def start_menu():
    os.system("clear")
    red()
    print(banner)
    red()
    decoracion()


#<--campish-->
def campish():
    os.system("clear")
    red()
    print(banner)
    red()
    print("                                 1 > Download Tool")
    print("                                 2 > Execute tool")
    print("                                 3 > Exit")
    x = input("              ↳ ")

    print("")
    if x == "1":
        ()red
        print("")
        print("Descargando pa...")
        os.system("git clone https://github.com/hangetzzu/saycheese.git")
        red()
        print("Downloaded!!")
        time.sleep(2)
        while True:
            campish()

    if x == "2":
        print("")
        os.system("mv saycheese/* .")
        os.system("mv saycheese/.sites .")
        os.system("bash saycheese.sh")

    if x == "3":
        start_menu()

#<--zphisher-->
def phishing():
    os.system("clear")

    red()
    print(banner)
    red()
    print("                                  1 > Download Tool")
    print("                                  2 > Execute tool")
    print("                                  3 > Exit")
    x = input("              ↳ ")

    print("")
    if x == "1":
        
        red()
        os.system("git clone https://github.com/iinc0gnit0/BlackPhish.git")
        print("")
        red()
        print("Fiumba ya esta!!")
        time.sleep(1)
        while True:
            phishing()

    if x == "2":
        print("")
        os.system("mv BlackPishr/* .")
        os.system("mv BlackPish/.sites .")
        os.system("sudo bash zphisher.sh")
    
    if x == "3":
        start_menu()


#    <---Start the tool-->
start_menu()
