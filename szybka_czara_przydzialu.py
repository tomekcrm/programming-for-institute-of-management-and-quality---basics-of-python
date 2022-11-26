import random 
import time

domy = ["DOM HARREGO", "TEN ZIELONY", "TEN ŻÓŁTY", "I JAKIŚ OSTATNI"]
kto_w_dom = {}

for dom in domy:
    dodac_dom = {str(dom):[]}
    kto_w_dom.update(dodac_dom)

while True:
    print("Kim jesteś przybyszu?")
    imie = input()
    jaki_dom = random.choice(domy)
    
    for i in range(2):
        print(".")
        time.sleep(0.5)
        print("..")
        time.sleep(0.5)
        print("...")
        time.sleep(0.5)
    
    time.sleep(1)
    print("coś czuję, że nie spodobac Ci się to")
    time.sleep(1)

    print(f"{imie} zostałeś przypisany do {jaki_dom}")
    
    lista_stara = kto_w_dom[jaki_dom]
    lista_stara.append(imie)

    kto_w_dom[jaki_dom] = lista_stara
    
    time.sleep(3)

    print("w domach są już:")
    for dom in domy:
        print(f"{dom} -> {kto_w_dom[dom]}")
    
    time.sleep(3)

    print("***************************")
    print("*******MIŁEJ PODRUŻY*******")
    print("***************************")
    print("")
    print("")
    print("")


