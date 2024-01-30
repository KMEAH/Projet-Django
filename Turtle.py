import turtle
def fonction_escalier(taille,nb):
    for i in range(nb):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
    t.forward(taille)

t=turtle.Turtle()

fonction_escalier(60,4)




turtle.done()
