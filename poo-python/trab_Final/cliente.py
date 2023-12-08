import tkinter as tk
from tkinter import messagebox
import model as md


class LimiteInsCliente(tk.Toplevel):

  def __init__(self, controle):

    tk.Toplevel.__init__(self,controle.main.root)
    self.geometry("250x250")
    self.title("Criar Cliente")
    self.control = controle

    self.frameNome = tk.Frame(self)
    self.frameEndereco = tk.Frame(self)
    self.frameEmail = tk.Frame(self)
    self.frameCpf = tk.Frame(self)
    self.frameButton = tk.Frame(self)
    self.frameNome.pack()
    self.frameEndereco.pack()
    self.frameEmail.pack()
    self.frameCpf.pack()
    self.frameButton.pack()

    self.labelNome = tk.Label(self.frameNome, text="Nome: ")
    self.inputNome = tk.Entry(self.frameNome, width=20)
    self.labelNome.pack(side="left")
    self.inputNome.pack(side="left")

    self.labelEndereco = tk.Label(self.frameEndereco, text="Endereço: ")
    self.inputEndereco = tk.Entry(self.frameEndereco, width=20)
    self.labelEndereco.pack(side="left")
    self.inputEndereco.pack(side="left")

    self.labelEmail = tk.Label(self.frameEmail, text="E-mail: ")
    self.inputEmail = tk.Entry(self.frameEmail, width=20)
    self.labelEmail.pack(side="left")
    self.inputEmail.pack(side="left")

    self.labelCpf = tk.Label(self.frameCpf, text="CPF: ")
    self.inputCpf = tk.Entry(self.frameCpf, width=20)
    self.labelCpf.pack(side="left")
    self.inputCpf.pack(side="left")

    self.enterButton = tk.Button(self.frameButton, text="Enter")
    self.clearButton = tk.Button(self.frameButton, text="Clear")
    self.closeButton = tk.Button(self.frameButton, text="Concluído")
    self.enterButton.pack(side="left")
    self.clearButton.pack(side="left")
    self.closeButton.pack(side="left")

    self.enterButton.bind("<Button>", controle.InsSubmitHandler)
    self.clearButton.bind("<Button>", controle.InsClearHandler)
    self.closeButton.bind("<Button>", controle.InsCloseHandler)

  def mostraJanela(self, titulo, msg):
    messagebox.showinfo(titulo, msg)


class LimiteBuscaCliente(tk.Toplevel):

  def __init__(self, controle):

    tk.Toplevel.__init__(self,controle.main.root)
    self.geometry("250x100")
    self.title("Buscar Cliente")
    self.controle = controle

    self.frameCpf = tk.Frame(self)
    self.frameButton = tk.Frame(self)
    self.frameCpf.pack()
    self.frameButton.pack()

    self.labelCpf = tk.Label(self.frameCpf, text="CPF: ")
    self.inputCpf = tk.Entry(self.frameCpf, width=18)
    self.labelCpf.pack(side="left")
    self.inputCpf.pack(side="left")

    self.buttonEnter = tk.Button(self.frameButton, text="Buscar")
    self.buttonClear = tk.Button(self.frameButton, text="Clear")
    self.buttonClose = tk.Button(self.frameButton, text="Concluído")
    self.buttonEnter.pack(side="left")
    self.buttonClear.pack(side="left")
    self.buttonClose.pack(side="left")

    self.buttonEnter.bind("<Button>", controle.buscaSubmitHandler)
    self.buttonClear.bind("<Button>", controle.buscaClearHandler)
    self.buttonClose.bind("<Button>", controle.buscaCloseHandler)

  def mostraJanela(self, msg):
    messagebox.showinfo("Cliente", msg)


class CtrlCliente():
  def __init__(self, mainCtrl):
    self.main = mainCtrl

  def cadastraCliente(self):
    self.limiteIns = LimiteInsCliente(self)

  def InsSubmitHandler(self, event):
    try:
      nome = self.limiteIns.inputNome.get()
      endereco = self.limiteIns.inputEndereco.get()
      email = self.limiteIns.inputEmail.get()
      cpf = self.limiteIns.inputCpf.get()
      cliente = md.Cliente(nome, endereco, email, cpf)

      self.main.clientes.append(cliente)
      self.limiteIns.mostraJanela("Sucesso", "Cliente Cadastrado")
      self.InsCloseHandler(event)

    except ValueError as error:
      messagebox.showerror('Erro',str(error))

  def InsClearHandler(self, event):
    self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
    self.limiteIns.inputEndereco.delete(0, len(self.limiteIns.inputEndereco.get()))
    self.limiteIns.inputEmail.delete(0, len(self.limiteIns.inputEmail.get()))
    self.limiteIns.inputCpf.delete(0, len(self.limiteIns.inputCpf.get()))

  def InsCloseHandler(self, event):
    self.limiteIns.destroy()

  def buscaCliente(self):
    self.limiteBusca = LimiteBuscaCliente(self)

  def buscaSubmitHandler(self, event):
    cpf = self.limiteBusca.inputCpf.get()

    for cliente in self.main.clientes:
      # print(cliente.cpf)
      if str(cliente.cpf) == str(cpf):
        cpf = cpf[0:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:11]
        msg = cliente.nome + " - " + cliente.endereco + " - " + cliente.email + "\n"
        self.limiteBusca.mostraJanela(msg)
        self.limiteBusca.destroy()
        return
    messagebox.showerror('Erro','Cpf inválido')

  def buscaClearHandler(self, event):
    self.limiteBusca.inputCpf.delete(0, len(self.limiteBusca.inputCpf.get()))

  def buscaCloseHandler(self, event):
    self.limiteBusca.destroy()