from tkinter import *
 
fenetre1 = Tk()
fenetre1.title('Tic Tac Toe')
fenetre1['bg']='white' # couleur de fond
 
#création lancement
Frame1 = Frame(fenetre1,bg="red",borderwidth=2,relief=GROOVE)
Frame1.pack(side=LEFT,padx=10,pady=10)
Label(Frame1,text="Bonjour et bienvenue",fg="white",bg="red").pack(padx=10,pady=10)
Button(Frame1,text="C'est parti!",fg='navy',command=fenetre1.destroy).pack(padx=10,pady=10)
fenetre1.mainloop ()
 
#création séléction joueurs
fenetre2 = Tk()
fenetre2.title('Séléction joueurs')
fenetre2['bg']='white'
Frame2 = Frame(fenetre2, bg='purple',borderwidth=3,relief=GROOVE)
Frame2.pack(padx=10,pady=10)
Label(Frame2,text="Veuillez saisir le nom de votre joueur\n quand vous aurez terminer, cliquez sur jouer!",fg="white",bg="purple").pack(padx=10,pady=10)
Label(Frame2,text="Joueur 1",fg="red",bg="white").pack(side=LEFT,padx=0,pady=1)
import tkinter
texte0=tkinter.Text(Frame2, width=10, height=0)
texte0.insert("end","       ")
texte0.pack(side=tkinter.RIGHT,padx=2,pady=0)
state=tkinter.DISABLED
Label(Frame2,text="Joueur 2",fg="blue",bg="white").pack(side=RIGHT,padx=0,pady=0)
texte1=tkinter.Text(Frame2, width=10, height=0)
texte1.insert("end","       ")
texte1.pack(side=tkinter.LEFT,padx=2,pady=3)
state=tkinter.DISABLED
Button(Frame2, text="Jouer",command=fenetre2.destroy).pack(padx=15,pady=15)
fenetre2.mainloop()
 
#création grille
class Morpion(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Plateau ")
 
        self.can = Canvas(self, width = 350, height = 350, bg = "white")
        self.can.pack(padx = 10, pady = 10)
        self.tracer_plateau()
 
        self.bind("<Button>", self.analyser_position_clic)
 
        self.bouton1 = Button(text="Recommencer",fg="white",bg="purple", command=self.recommencer).pack(padx=10,pady=10)
        self.plateau = [0] * 10
        self.joueur = 1
 
 
    def tracer_plateau(self):
        self.can.create_line(123.3, 20, 123.3, 330, width = 4)
        self.can.create_line(226.6 , 20, 226 , 330, width=4)
        self.can.create_line(20, 123.3, 330, 123.3, width=4)
        self.can.create_line(20 ,226.3 ,330 ,226.3, width=4)
        self.can.create_line(20,20,330,20,width=4)
        self.can.create_line(20,20,20,330,width=4)
        self.can.create_line(20,330,330,330,width=4)
        self.can.create_line(330,20,330,330,width=4)
 
    def changement_de_joueurs(self):
        if self.joueur == 1: 
            self.joueur = 2
        else:
            self.joueur = 1
 
    def tracer_croix(self, x, y):
        self.can.create_line(x-45.5, y-45.5, x+45.5, y+45.5, width = 5, fill = "red")
        self.can.create_line(x-45.5, y+45.5, x+45.5, y-45.5, width = 5, fill = "red")
 
    def tracer_rond(self, x, y):
        self.can.create_oval(x-51.5, y-51.5, x +51.5, y+51.5, fill = "blue")
        self.can.create_oval(x-46.5,y-46.5,x+46.5,y+46.5, fill = "ivory")
 
    def analyser_position_clic(self, event):
        #Detection de la position de la souris dans le Canvas en fonction des cases
        # 1 | 2 | 3
        # - + - + -
        # 4 | 5 | 6
        # - + - + -
        # 7 | 8 | 9
 
        if self.plateau[0] == 0:
            if event.x > 20 and event.x < 123:
                if event.y > 20 and event.y < 123:
                    i = 1
                    self.x = 71.5
                    self.y = 71.5
                if event.y > 123 and event.y < 226:
                    i = 4
                    self.x = 71.5
                    self.y = 174.5
                if event.y > 226 and event.y < 330:
                    i = 7
                    self.x = 71.5
                    self.y = 277.5
            elif event.x > 123 and event.x < 226:
                if event.y > 20 and event.y < 123:
                    i = 2
                    self.x = 174.5
                    self.y = 71.5
                if event.y > 123 and event.y < 226:
                    i = 5
                    self.x = 174.5
                    self.y = 174.5
                if event.y > 200 and event.y < 300:
                    i = 8
                    self.x = 174.5
                    self.y = 277.5
            elif event.x > 226 and event.x < 330:
                if event.y > 20 and event.y < 123:
                    i = 3
                    self.x = 277.5
                    self.y = 71.5
                if event.y > 123 and event.y < 226:
                    i = 6
                    self.x = 277.5
                    self.y = 174.5
                if event.y > 226 and event.y < 330:
                    i = 9
                    self.x = 277.5
                    self.y = 277.5
 
        if self.plateau[i] is 0:
            if self.joueur is 1:
                self.plateau[i] = 1
                self.tracer_croix(self.x, self.y)
            else:
                self.plateau[i] = 2
                self.tracer_rond(self.x, self.y)
 
            self.changement_de_joueurs()
            self.test_gagnant()
 
 
    def recommencer(self):
        self.can.delete(ALL)
        self.tracer_plateau()
        self.plateau = [0] * 10
        self.joueur = 1
 
    def test_gagnant(self):
        if self.plateau[1] == self.plateau[2] == self.plateau[3] and self.plateau[1]!= 0:
            self.can.create_line(20,70,330,70,width=20)
            self.plateau[0] = self.plateau[1]
 
        elif self.plateau[4] == self.plateau[5] == self.plateau[6] and self.plateau[4]!= 0:
            self.can.create_line(20,173,330,173,width=20)
            self.plateau[0] = self.plateau[1]
        elif self.plateau[7] == self.plateau[8] == self.plateau[9] and self.plateau[7]!= 0:
            self.can.create_line(20,276,330,276,width=20)
            self.plateau[0] = self.plateau[1]
        elif self.plateau[1] == self.plateau[5] == self.plateau[9] and self.plateau[1]!= 0:
            self.can.create_line(30,30,320,320,width=20)
            self.plateau[0] = self.plateau[1]
        elif self.plateau[3] == self.plateau[5] == self.plateau[7] and self.plateau[3]!= 0:
            self.can.create_line(30,320,320,30,width=20)
            self.plateau[0] = self.plateau[1]
        elif self.plateau[1] == self.plateau[4] == self.plateau[7] and self.plateau[1]!= 0:
            self.can.create_line(70,330,70,20,width=20)
            self.plateau[0] = self.plateau[1]
        elif self.plateau[2] == self.plateau[5] == self.plateau[8] and self.plateau[2]!= 0:
            self.can.create_line(176,330,176,20,width=20)
            self.plateau[0] = self.plateau[1]
        elif self.plateau[3] == self.plateau[6] == self.plateau[9] and self.plateau[3]!= 0:
            self.can.create_line(276,330,276,20,width=20)
            self.plateau[0] = self.plateau[1]
 
 
if __name__ == "__main__":
    fenetre = Morpion()
Frame3 = Frame(fenetre,bg="white",borderwidth=2,relief=GROOVE)
Frame3.pack(side=LEFT,padx=5,pady=5)
Label(Frame3,text="Joueur 1",fg="red",bg="white").pack(side=LEFT,padx=5,pady=5)
Frame4 = Frame(fenetre,bg="white",borderwidth=2,relief=GROOVE)
Frame4.pack(side=RIGHT,padx=5,pady=5)
Label(Frame4,text="Joueur 2",fg="blue",bg="white").pack(side=RIGHT,padx=5,pady=5)
 
 
fenetre.mainloop()