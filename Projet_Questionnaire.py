def Poser_question(question,r1,r2,r3,r4,choix_bonne_reponse):
    global score
    print(question)
    print(f"(a) {r1}")
    print(f"(b) {r2}")
    print(f"(c) {r3}")
    print(f"(d) {r4}")
   
    reponse=input("Votre reponse : ")
    
    if reponse==choix_bonne_reponse :
        print("reponse correct!")
        score+=1
    else:
        print("Mauvaise reponse!")
    

score=0     
Poser_question("quelle est la capitale de la CI ?", "Yamoussoukro","Abidjan","San-pedro","Bouake","a")
Poser_question("quelle est la capitale de la France ?", "Marseille","paris","Monaco","Nice","b")
Poser_question("quelle est la capitale de l'angleterre ?", "Manchester","Leicester","Londre","Everton","c")
Poser_question("quelle est la capitale de l'espagne ?", "Valence","Barcelone","Celta Vigo","Madrid","d")


print(f"Votre score fonal est: {score}")






