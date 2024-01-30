noms=["Jean","Sophie","Martin","Christophe","Zoe","Martin"]

# 1--for / len

'''nombre=0
for nom in noms:
    nombre+=len(nom)

print(nombre)'''

# Complétion de liste + la fonction sum
'''new_nom=[len(nom) for nom in noms]

nombre=sum(new_nom)
print(f"Le nombre total de nom est: {nombre}")'''

# La fonction join et len 

new_nom="".join(noms)
print(new_nom)


