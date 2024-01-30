import random


def demande_nom(NOMBRE_MIN,NOMBRE_MAX):
    reponse_int=0
    while reponse_int==0:
        reponse_str=input(f"Quel est le nombre entre {NOMBRE_MIN} et {NOMBRE_MAX}: ")
        try:
          reponse_int=int(reponse_str)

        except:
            print("ERREUR:Veuillez entrer un nombre!!!")  

        else:
            if reponse_int<NOMBRE_MIN or reponse_int>NOMBRE_MAX:
              print("ERREUR! VEUILLEZ ENTRER UN NOMBRE ENTRE 1 ET 10")
              reponse_int=0

    return reponse_int 

NOMBRE_MAX=10
NOMBRE_MIN=1
NOMBRE_MAGIQUE=random.randint(NOMBRE_MIN,NOMBRE_MAX)
NB_VIES=4

nombre=1
while not nombre==NOMBRE_MAGIQUE and NB_VIES>0:
    nombre=demande_nom(NOMBRE_MIN,NOMBRE_MAX)
    print(f"Il vous reste {NB_VIES} vies")
    if nombre<NOMBRE_MAGIQUE: 
      print("le nombre magique est plus grand")
      NB_VIES-=1
    elif nombre>NOMBRE_MAGIQUE :
       print("le nombre magique est plus petit")
       NB_VIES-=1
    elif nombre==NOMBRE_MAGIQUE:
        print("Vous avez trouvé le nombre ! ")
    
if NB_VIES==0:
   print(f"VOUS AVEZ PERDU!. Le nombre magique était : {NOMBRE_MAGIQUE}")
        
            



