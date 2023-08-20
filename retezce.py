def zamen (slovo, pozice, novy_znak):
    """V daném slově zamění znak na dané pozici za daný nový znak."""
    zacatek = slovo [:pozice]
    stred = novy_znak
    konec = slovo [pozice +1:]
    nove_slovo = zacatek + stred + konec
    return nove_slovo


print(zamen("filip", 1, "e"))
print (zamen("Lucik", 0, "p"))