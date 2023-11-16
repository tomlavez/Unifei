import tkinter as tk
from tkinter import messagebox

class Artista():
    def __init__ (self, nome):
        self.__nome = nome

        self.__listaAlbuns = []
        self.__listaMusicas = []

    @property
    def nome(self):
        return self.__nome
    
    @property
    def listaAlbuns(self):
        return self.__listaAlbuns
    
    @property
    def listaMusicas(self):
        return self.__listaMusicas
    
    def insereAlbum(self, album):
        self.__listaAlbuns.append(album)

    def insereMusica(self, musica):
        self.__listaMusicas.append(musica)

class LimiteInsereArtista(tk.Toplevel): #Contrutor da Janela
    def __init__ (self, controle):

        tk.Toplevel.__init__(self)
        self.geometry("200x200")
        self.title("Artista")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameButton.pack()

        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.inputNome = tk.Entry(self.frameNome,width=20)
        self.labelNome.pack(side="left")
        self.inputNome.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton,text="Enter")
        self.buttonClear = tk.Button(self.frameButton,text="Clear")
        self.buttonClose = tk.Button(self.frameButton,text="Concluido")
        self.buttonSubmit.pack(side="left")
        self.buttonClear.pack(side="left")
        self.buttonClose.pack(side="left")

        self.buttonSubmit.bind("<Button>", controle.submitHandler)
        self.buttonClear.bind("<Button>", controle.clearHandler)
        self.buttonClose.bind("<Button>", controle.closeHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMostraArtista():
    def __init__ (self, str):
        messagebox.showinfo("Lista de artistas", str)

class CtrlArtista():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaArtistas = []

    def insereArtista(self):
        self.limiteIns = LimiteInsereArtista(self)

    def mostraArtista(self):
        str = "Nome: \n"
        for art in self.listaArtistas:
            str += art.nome + "\n"
            for alb in art.listaAlbuns:
                str += " " + alb.titulo + ":\n"
                for music in alb.listaMusicas:
                    str += "  " + music.titulo + " - " + music.nroFaixa + "\n"
        self.limiteIns = LimiteMostraArtista(str)

    def submitHandler(self, event):
        nome = self.limiteIns.inputNome.get()
        artista = Artista(nome)
        self.listaArtistas.append(artista)
        self.clearHandler(event)
        #feedback
        self.limiteIns.mostraJanela("Sucesso", "Artista cadastrado!")

    def clearHandler(self, event):
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))

    def closeHandler(self, event):
        self.limiteIns.destroy()

    def addAlbum(self, art, album):
        for x in self.listaArtistas:
            if x.nome == art:
                x.insereAlbum(album)

    def addMusica(self, art, musica):
        for x in self.listaArtistas:
            if x.nome == art:
                x.insereMusica(musica)

    def getListaNomeArtista(self):
        lista = []
        for art in self.listaArtistas:
            lista.append(art.nome)
        return lista
    
    def getArtista(self, art):
        for x in self.listaArtistas:
            if x.nome == art:
                return x
            
    def getMusica(self, art, musica):
        for x in self.listaArtistas:
            if x.nome == art:
                for mus in x.listaMusicas:
                    if mus.titulo == musica:
                        return mus