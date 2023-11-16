import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Playlist():
    def __init__ (self, nome):
        self.__nome = nome
        self.__musicas = []
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def musicas(self):
        return self.__musicas
    
class LimiteInserePlaylist(tk.Toplevel):
    def __init__ (self, controle):

        tk.Toplevel.__init__(self)
        self.geometry("300x250")
        self.title("Playlist")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameArtista = tk.Frame(self)
        self.frameMusicas = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameArtista.pack()
        self.frameMusicas.pack()
        self.frameButton.pack()

        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.inputNome = tk.Entry(self.frameNome,width=20)
        self.labelNome.pack(side="left")
        self.inputNome.pack(side="left")

        self.listaArtista = self.controle.ctrlPrincipal.ctrlArtista.getListaNomeArtista()
        self.listaMusicas = []

        self.labelArtista = tk.Label(self.frameArtista,text="Escolha o artista: ")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameArtista, width=15, values=self.listaArtista, textvariable=self.escolhaCombo)
        self.labelArtista.pack(side="left")
        self.combobox.pack(side="left")
        self.combobox.bind("<<ComboboxSelected>>", self.atualizaListaMusicas)

        self.labelMusicas = tk.Label(self.frameMusicas,text="Escolha a musica")
        self.musicas = tk.StringVar()
        self.listbox = tk.Listbox(self.frameMusicas, listvariable=self.musicas)
        self.labelMusicas.pack(side="left")
        self.listbox.pack(side="left")
        
        self.buttonInsere = tk.Button(self.frameButton, text="Inserir Musica")
        self.buttonCria = tk.Button(self.frameButton, text="Criar Playlist")
        self.buttonFecha = tk.Button(self.frameButton, text="Concluido!")
        self.buttonInsere.pack(side="left")
        self.buttonCria.pack(side="left")
        self.buttonFecha.pack(side="left")

        self.buttonInsere.bind("<Button>", controle.insereHandlerI)
        self.buttonCria.bind("<Button>", controle.criaHandlerI)
        self.buttonFecha.bind("<Button>", controle.fechaHandlerI)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

    def atualizaListaMusicas(self, event):
        listaMusicas = []
        artEscolhido = self.combobox.get()
        for art in self.listaArtista:
            if art == artEscolhido:
                objetoArt = self.controle.ctrlPrincipal.ctrlArtista.getArtista(art)
                for music in objetoArt.listaMusicas:
                    listaMusicas.append(music.titulo)
        self.musicas.set(listaMusicas)

class LimiteMostraPlaylist(tk.Toplevel):
    def __init__ (self, controle):
        self.controle = controle
        tk.Toplevel.__init__(self)
        self.geometry("250x100")
        self.title("Playlist")

        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameButton.pack()

        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.labelNome.pack(side="left")
        self.inputNome.pack(side="left")

        self.enterButton = tk.Button(self.frameButton, text="Enter")
        self.clearButton = tk.Button(self.frameButton, text="Clear")
        self.closeButton = tk.Button(self.frameButton, text="Concluido")
        self.enterButton.pack(side="left")
        self.clearButton.pack(side="left")
        self.closeButton.pack(side="left")

        self.enterButton.bind("<Button>", controle.enterHandlerM)
        self.clearButton.bind("<Button>", controle.clearHandlerM)
        self.closeButton.bind("<Button>", controle.closeHandlerM)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class CtrlPlaylist():
    def __init__ (self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaPlaylist = []
        self.listaMusicasPlaylist = []

    def inserePlaylist(self):
        self.limiteIns = LimiteInserePlaylist(self)

    def criaHandlerI(self, event):
        nome = self.limiteIns.inputNome.get()
        playlist = Playlist(nome)
        for msc in self.listaMusicasPlaylist:
            playlist.musicas.append(msc)
        self.listaPlaylist.append(playlist)
        self.listaMusicasPlaylist = []
        self.limiteIns.destroy()
        #feedback
        self.limiteIns.mostraJanela("Sucesso", "Playlist criada!")

    def insereHandlerI(self, event):
        musicaSel = self.limiteIns.listbox.get(tk.ACTIVE)
        art = self.limiteIns.combobox.get()
        musica = self.ctrlPrincipal.ctrlArtista.getMusica(art, musicaSel)   
        self.listaMusicasPlaylist.append(musica)
        self.limiteIns.listbox.delete(tk.ACTIVE)
        #feedback
        self.limiteIns.mostraJanela("Sucesso", "Musica adicionada!")

    def fechaHandlerI(self, event):
        self.limiteIns.destroy()

    def mostraPlaylist(self):
        self.limiteMostra = LimiteMostraPlaylist(self)

    def enterHandlerM(self, event):
        titulo = self.limiteMostra.inputNome.get()
        msg = "Musicas: \n"
        for playlist in self.listaPlaylist:
            if playlist.nome == titulo:
                for mus in playlist.musicas:
                    msg += " " + mus.titulo + "\n"
        self.limiteMostra.mostraJanela(titulo, msg)


    def clearHandlerM(self, event):
        self.limiteMostra.inputNome.delete(0, len(self.limiteMostra.inputNome.get()))

    def closeHandlerM(self, event):
        self.limiteMostra.destroy()