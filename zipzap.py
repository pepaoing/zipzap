from colors import green, red, blue, yellow, purple, white

import os, time

#   <--Menu-->

red()

banner = """
 ________    __       _______       ________        __         _______   
("      "\  |" \     |   __ "\     ("      "\      /""\       |   __ "\  
 \___/   :) ||  |    (. |__) :)     \___/   :)    /    \      (. |__) :) 
   /  ___/  |:  |    |:  ____/        /  ___/    /' /\  \     |:  ____/  
  //  \__   |.  |    (|  /           //  \__    //  __'  \    (|  /      
 (:   / "\  /\  |\  /|__/ \         (:   / "\  /   /  \\  \  /|__/ \     
  \_______)(__\_|_)(_______)         \_______)(___/    \___)(_______)    
                                                                                                                        
"""

def  decoracion():
    red()
    # hola
    print("                                  1 > Brutal")
    print("                                  2 > Phishing")
    print("                                  3 > Ngrok")
    print("                                  99 > Exit")    
    option = input("              > ")

    if option == "1":
        payload()

    if option == "2":
       phishing()
        
    if option == "3":
        ngrok()
    
    if option == "99":
        print (":C")
        os.system("clear")
        exit()

#   <--Return to Menu-->
def start_menu():
    os.system("clear")
    red()
    print(banner)
    red()
    decoracion()

#<--brutal-->
def payload():
    os.system("clear")
    red()
    print(banner)
    red()
    print("                                 1 > Download And Execute")
    print("                                 3 > Exit")
    x = input("              ↳ ")

    print("")          
    if x == "1":
        print("")
        os.system("sudo rm -r Brutal")
        os.system("sudo git clone https://github.com/Screetsec/Brutal.git && cd Brutal && sudo bash Brutal.sh")
        red()

    if x == "3":
        start_menu()

#<--zphisher-->
def phishing():
    os.system("clear")

    red()
    print(banner)
    red()
    print("                                  1 > Download And Execute")
    print("                                  3 > Exit")
    x = input("              ↳ ")


    if x == "1":
        print("")
        os.system("sudo rm -r BlackPhish ")
        os.system("sudo git clone https://github.com/iinc0gnit0/BlackPhish.git &&cd BlackPhish && bash install.sh &&  sudo python3 blackphish.py")
    if x == "2":
        start_menu()
      
      
#<--ngrok->
def ngrok():
    os.system("clear")

    red()
    print(banner)
    red()
    print("                                  1 > Download 1")
    print("                                  2 > Download 2")
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
            ngrok()

    if x == "2":
        print("")
      
        os.system("mv BlackPhish/*")
        os.system("mv BlackPhish/* .")
        os.system("sudo python3 BlackPhish.py")
    
    if x == "3":
        start_menu()

      #    <---Start the tool-->
start_menu()
