# Recherche insensible à la casse
'''def recherche_element(element,collection):
    element_new=element.lower()    
    collection_new=[nom.lower() for nom in collection]
    collection=collection_new
    if element_new in collection_new:
        print("Element trouvé")
    else:
        print("Element introuvable")
noms=["Jean","Sophie","Martin","Christophe","Zoe","Martin"]
recherche_element("JEAN",noms)'''

# Exercice , extraire les extensions
fichiers=["notepad.exe","mon.fichiers.perso.doc","note.TXT","vacances.jpg","planning","data.dat"]

definition_extensions=[("exe","Excecutable"),
("doc","Document Word"),
("txt","Document Texte"),
("jpg","Image JPEG")]


def extraction_des_extensions(file):
    global a_new
    a_new=[]
    for i in file:
        list=i.split(".")
        if len(list)>1:
            a_new.append(list[-1])
        else:
            a_new.append("pas d'extension")

    return a_new


def obtenir_definition_extension(extension,fichiers):
    for d in definition_extensions:
        if d[0].lower==extension.lower():
            return d[1]
        return None

for fichier in fichiers:
    l=extraction_des_extensions(fichiers)
    if l:
        defintion=obtenir_definition_extension(l,definition_extensions)
    else:
        defintion="Aucune extension" 







    




    

