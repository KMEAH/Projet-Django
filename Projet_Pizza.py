'''def Pizza_Existe(collection):
    for i in collection:
        if reponse==i:
            return True
    return False'''
# On pouvait faire autrement sans l'utlisation de la fonction!!! 
    
def Ajouter_Pizza_Utilisateur(collection):
    global reponse
    reponse=input("Pizza à ajouter : ")
    # if Pizza_Existe(collection):
    if reponse.lower() in collection:
        print("ERREUR: la pizza existe déjà!")
    else:
        collection.append(reponse)

'''def tri_personnalise(e):
    return len(e)'''

def Afficher(collection,nb=-1):
    c=collection
    if not nb==-1:
        c=collection[:nb]
    if collection==():
        print("AUCUNE PIZZA")
        return
   # collection.sort(key=tri_personnalise)
    print(f"LISTE DES PIZZAS ({len(collection)})")
    for i in c:
        print(i)
    print()
    print(f"nom de la première pizza: {collection[0]}")
    print(f"nom de la dernière pizza: {collection[-1]}")

pizzas=["4 fromages","végétarienne","hawai","calzone"]



Ajouter_Pizza_Utilisateur(pizzas)
Afficher(pizzas)