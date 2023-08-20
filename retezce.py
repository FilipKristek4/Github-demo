slovo = input("vlož slovo: ")
print(slovo)
pozice = int(input("zadej pozici písmena: "))
print(pozice)
nove_pismeno = input("vlož nove písmeno: ")
print(nove_pismeno)
nove_slovo = slovo[:pozice]+nove_pismeno + slovo[pozice +1:]
print(nove_slovo)