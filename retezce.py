def nacti_cislo():
    while True :
        odpoved = input ("Zvol cislo: ")
        try:
            return int(odpoved)
        except ValueError:
            print("Musi to byt cislo!")
        

print("cislo je : ", nacti_cislo())
print("byl to těžky úkol")