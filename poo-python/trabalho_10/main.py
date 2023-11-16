import tkinter as tk
from tkinter import messagebox
import album
import artista
import playlist

class LimitePrincipal():    #Construtor da janela
    def __init__ (self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry("300x300")
        self.menubar = tk.Menu(self.root)
        self.artistaMenu = tk.Menu(self.menubar)
        self.albumMenu = tk.Menu(self.menubar)
        self.playlistMenu = tk.Menu(self.menubar)

        self.artistaMenu.add_command(label="Cadastrar", command=self.controle.insereArtista)
        self.artistaMenu.add_command(label="Consultar", command=self.controle.mostraArtista)
        self.menubar.add_cascade(label="Artista", menu=self.artistaMenu)

        self.albumMenu.add_command(label="Cadastrar", command=self.controle.insereAlbum)
        self.albumMenu.add_command(label="Consultar", command=self.controle.mostraAlbum)
        self.menubar.add_cascade(label="Album", menu=self.albumMenu)

        self.playlistMenu.add_command(label="Cadastrar", command=self.controle.inserePlaylist)
        self.playlistMenu.add_command(label="Consultar", command=self.controle.mostraPlaylist)
        self.menubar.add_cascade(label="Playlist", menu=self.playlistMenu)

        self.root.config(menu=self.menubar)

class ControlePrincipal():
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlAlbum = album.CtrlAlbum(self)
        self.ctrlArtista = artista.CtrlArtista(self)
        self.ctrlPlaylist = playlist.CtrlPlaylist(self)

        self.limite = LimitePrincipal(self.root, self)

        self.root.title("Exemplo MVC")

        self.root.mainloop()

    def insereArtista(self):
        self.ctrlArtista.insereArtista()

    def mostraArtista(self):
        self.ctrlArtista.mostraArtista()
    
    def insereAlbum(self):
        self.ctrlAlbum.insereAlbum()

    def mostraAlbum(self):
        self.ctrlAlbum.mostraAlbum()

    def inserePlaylist(self):
        self.ctrlPlaylist.inserePlaylist()

    def mostraPlaylist(self):
        self.ctrlPlaylist.mostraPlaylist()

if __name__ == '__main__':
    c = ControlePrincipal()
