y_a = "ý"
osloveni = "Filipe"
podpis = "Váš program"
vysledek = 15

print(f"""Mil{y_a} {osloveni},
Váš výsledek je {vysledek}.
S pozdravem,
{podpis}.""")

sablona = "Ahoj {jmeno}, tvé číslo je {cislo}."

print(sablona.format(jmeno = "Filipe", cislo = 4))
print(sablona.format(jmeno = "Lucie", cislo = 19))
print(sablona.format(jmeno = "Milane", cislo = 10))

vypis = "{} krát {} je {}"
print(vypis.format(3,4,3*4))