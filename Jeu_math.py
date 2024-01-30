import random 
NOMBRE_MIN=1
NOMBRE_MAX=10
NB_QUESTION=5
nb_point=0


def poser_question():
    a=random.randint(NOMBRE_MIN,NOMBRE_MAX)
    b=random.randint(NOMBRE_MIN,NOMBRE_MAX)
    operateur=random.randint(0,1)
    if operateur==0:
      operateur="+"
    elif operateur==1:
      operateur="*"

    reponse_str=input(f"Calculer {a} {operateur} {b} = ")
    reponse_int=int(reponse_str)
    global nb_point
    if reponse_int==a+b and operateur=="+":
     print("Reponse correct!")
     nb_point+=1
    elif reponse_int==a*b and operateur=="*":
      print("Reponse correct!")
      nb_point+=1
    else:
     print("Reponse incorrect!")
    
     
    
for i in range(1,NB_QUESTION):
  print(f"Question n {i}/4")
  poser_question()
  i+=1
MOYENNE=int(nb_point/NB_QUESTION)

print(f"Votre point est: {nb_point}/{NB_QUESTION-1}")
if nb_point==4 :
  print("Excellent!")
elif nb_point==0 :
  print("aller reviser!")
elif nb_point<MOYENNE:
  print("Aller reviser!")
elif nb_point>MOYENNE:
  print("Pas mal!")
