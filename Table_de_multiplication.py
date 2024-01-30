def Afficher_Table_Multiplication(n,min,max):
    
    if min>max:
       print("Erreur le min est supérieur au max")
       return
    for i in range(min,max+1):

     print(f"{i} x {n} = {i*n}")

Afficher_Table_Multiplication(4,1,10)