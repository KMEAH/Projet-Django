def Poser_question(question):
    global score
    print(question[0])
    choix=question[1]
    for i in range(len(choix)):
        print(f"{i+1}){choix[i]}")
    reponse=input(f"Votre reponse (Entre 1 et {len(choix)} ) : ")
    bonne_reponse=question[2]
    if reponse.lower()==bonne_reponse :
        print("reponse correct!")
        score+=1
    else:
        print("Mauvaise reponse!")
    

score=0     



questionnaire=(("quelle est la capitale de la CI ?",("yamoussoukro","abidjan","san-pedro","bouake",'Grand-Bassam'),"1"),
               ("quelle est la capitale de l'angleterre ?",("manchester","leicester","londre","everton"),"3"))


def lancement_questionnaire (questionnaire):
    for question in questionnaire:
        Poser_question(question)

lancement_questionnaire(questionnaire)

print(f"Votre score final est: {score}")






