import tkinter as tk
from tkinter import messagebox
import model as md


class LimiteInsProd(tk.Toplevel):
  def __init__(self, controle):

    tk.Toplevel.__init__(self,controle.main.root)
    self.geometry("200x200")
    self.title("Produto")
    self.controle = controle

    self.frameCod = tk.Frame(self)
    self.frameDes = tk.Frame(self)
    self.framePreco = tk.Frame(self)
    self.frameButton = tk.Frame(self)
    self.frameCod.pack()
    self.frameDes.pack()
    self.framePreco.pack()
    self.frameButton.pack()

    self.labelCod = tk.Label(self.frameCod, text="Código: ")
    self.inputCod = tk.Entry(self.frameCod, width=20)
    self.labelCod.pack(side="left")
    self.inputCod.pack(side="left")

    self.labelDes = tk.Label(self.frameDes, text="Descrição: ")
    self.inputDes = tk.Entry(self.frameDes, width=20)
    self.labelDes.pack(side="left")
    self.inputDes.pack(side="left")

    self.labelPreco = tk.Label(self.framePreco, text="Preço: ")
    self.inputPreco = tk.Entry(self.framePreco, width=20)
    self.labelPreco.pack(side="left")
    self.inputPreco.pack(side="left")

    self.buttonEnter = tk.Button(self.frameButton, text="Enter")
    self.buttonClear = tk.Button(self.frameButton, text="Clear")
    self.buttonClose = tk.Button(self.frameButton, text="Concluído")
    self.buttonEnter.pack(side="left")
    self.buttonClear.pack(side="left")
    self.buttonClose.pack(side="left")

    self.buttonEnter.bind("<Button>", controle.InsSubmitHandler)
    self.buttonClear.bind("<Button>", controle.InsClearHandler)
    self.buttonClose.bind("<Button>", controle.InsCloseHandler)

  def mostraJanela(self, titulo, msg):
    messagebox.showinfo(titulo, msg)


class LimiteBuscaProd(tk.Toplevel):

  def __init__(self, controle):

    tk.Toplevel.__init__(self,controle.main.root)
    self.geometry("250x100")
    self.title("Produto")
    self.controle = controle

    self.frameCod = tk.Frame(self)
    self.frameButton = tk.Frame(self)
    self.frameButton2 = tk.Frame(self)
    self.frameCod.pack()
    self.frameButton.pack()
    self.frameButton2.pack()

    self.labelCod = tk.Label(self.frameCod, text="Código: ")
    self.inputCod = tk.Entry(self.frameCod, width=18)
    self.labelCod.pack(side="left")
    self.inputCod.pack(side="left")

    # self.buttonEnter = tk.Button(self.frameButton, text="Editar")
    self.buttonConsulta = tk.Button(self.frameButton, text="Consultar")
    # self.buttonDel = tk.Button(self.frameButton, text="Excluir")
    self.buttonClear = tk.Button(self.frameButton2, text="Clear")
    self.buttonClose = tk.Button(self.frameButton2, text="Concluído")
    # self.buttonEnter.pack(side="left")
    self.buttonConsulta.pack(side="left")
    # self.buttonDel.pack(side="left")
    self.buttonClear.pack(side="left")
    self.buttonClose.pack(side="left")

    # self.buttonEnter.bind("<Button>", controle.buscaSubmitHandler)
    self.buttonConsulta.bind("<Button>", controle.buscaConsHandler)
    # self.buttonDel.bind("<Button>", controle.buscaDelHandler)
    self.buttonClear.bind("<Button>", controle.buscaClearHandler)
    self.buttonClose.bind("<Button>", controle.buscaCloseHandler)

  def mostraJanela(self, titulo, msg):
    messagebox.showinfo(titulo, msg)


class LimiteEditProd(tk.Toplevel):
  def __init__(self, controle):
    tk.Toplevel.__init__(self,controle.main.root)
    self.geometry('200x200')
    self.title('Editar/Excluir')
    self.controle = controle

  def input_cod(self):
    self.frameCod = tk.Frame(self)
    self.frameButton = tk.Frame(self)

    tk.Label(self.frameCod,text='Código: ').pack(side='left')
    self.inputCod = tk.Entry(self.frameCod, width=20)

    self.buttonEdit = tk.Button(self.frameButton, text="Editar")
    self.buttonDel = tk.Button(self.frameButton, text='Excluir')
    self.buttonClose = tk.Button(self.frameButton, text="Fechar")


    self.buttonEdit.pack(side='left')
    self.buttonDel.pack(side='left')
    self.buttonClose.pack(side='left')

    self.inputCod.pack(side='left')

    self.frameCod.pack(pady=20)
    self.frameButton.pack()

    self.buttonEdit.bind("<Button>", self.controle.edit_prod)
    self.buttonDel.bind("<Button>", self.controle.del_produto)
    self.buttonClose.bind("<Button>", self.controle.close_editLimite)

  def edit(self):
    self.frameCod.pack_forget()
    self.frameButton.pack_forget()
    self.buttonEdit.pack_forget()
    self.buttonDel.pack_forget()
    self.buttonClose.pack_forget()

    self.frameDes = tk.Frame(self)
    self.framePreco = tk.Frame(self)
    self.frameButton = tk.Frame(self)

    tk.Label(self.frameDes, text="Descrição: ").pack(side='left')
    tk.Label(self.framePreco, text="Preço Kg: ").pack(side='left')

    self.inputDes = tk.Entry(self.frameDes, width=20)
    self.inputPreco = tk.Entry(self.framePreco, width=20)

    self.buttonEnter = tk.Button(self.frameButton,text='Enter')
    self.buttonClear = tk.Button(self.frameButton,text='Limpar')
    self.buttonClose = tk.Button(self.frameButton,text='Fechar')

    self.inputDes.pack(side='left')
    self.inputPreco.pack(side="left")
    self.buttonEnter.pack(side="left")
    self.buttonClear.pack(side='left')
    self.buttonClose.pack(side="left")

    self.buttonEnter.bind("<Button>", self.controle.submit_editLimite)
    self.buttonClear.bind('<Button>', self.controle.clear_editLimite)
    self.buttonClose.bind("<Button>", self.controle.close_editLimite)

    self.frameCod.pack()
    self.frameDes.pack()
    self.framePreco.pack()
    self.frameButton.pack()

  def mostraJanela(self, titulo, msg):
    messagebox.showinfo(titulo, msg)


class LimiteMostraProd():
  def __init__(self, str):
    messagebox.showinfo("Produto", str)


class ctrlProduto():
  def __init__(self, mainCtrl):
    self.main = mainCtrl

  def cadastraProduto(self):
    self.limiteIns = LimiteInsProd(self)

  def InsSubmitHandler(self, event):
    codigo = self.limiteIns.inputCod.get()
    desc = self.limiteIns.inputDes.get()
    preco = self.limiteIns.inputPreco.get()
    produto = md.Produto(codigo, desc, preco)
    self.main.produtos.append(produto)
    self.limiteIns.mostraJanela("Sucesso", "Produto Inserido")
    self.InsClearHandler(event)

  def InsClearHandler(self, event):
    self.limiteIns.inputCod.delete(0, len(self.limiteIns.inputCod.get()))
    self.limiteIns.inputDes.delete(0, len(self.limiteIns.inputDes.get()))
    self.limiteIns.inputPreco.delete(0, len(self.limiteIns.inputPreco.get()))

  def InsCloseHandler(self, event):
    self.limiteIns.destroy()

  def BuscaProduto(self):
    self.limiteBusca = LimiteBuscaProd(self)

  def EditProduto(self):
    self.limiteEdit = LimiteEditProd(self)
    self.limiteEdit.input_cod()

  def buscaSubmitHandler(self, event):
    codigo = self.limiteBusca.inputCod.get()
    if any(prod.codigo == codigo for prod in self.main.produtos):
      for prod in self.main.produtos:
        if prod.codigo == codigo:
          self.limiteEdit = LimiteEditProd(self)
          self.limiteEdit.textCod.set(prod.codigo)
          self.limiteEdit.textDes.set(prod.descricao)
          self.limiteEdit.textPreco.set(prod.preco)
    else:
      self.limiteBusca.mostraJanela("Error", "Código inválido")

  def buscaConsHandler(self, event):
    codigo = self.limiteBusca.inputCod.get()

    if any(prod.codigo == codigo for prod in self.main.produtos):
      for prod in self.main.produtos:
        if prod.codigo == codigo:
          str = "{} - {} - {:.2f}".format(prod.codigo, prod.descricao,
                                          prod.precoKg)
          self.limiteBusca.destroy()
          self.limiteMostra = LimiteMostraProd(str)
    else:
      self.limiteBusca.mostraJanela("Error", "Código inválido")
      self.buscaClearHandler(event)

  def buscaClearHandler(self, event):
    self.limiteBusca.inputCod.delete(0, len(self.limiteBusca.inputCod.get()))

  def buscaCloseHandler(self, event):
    self.limiteBusca.destroy()


  def del_produto(self, event):
    codigo = self.limiteEdit.inputCod.get()

    if len(codigo) != 0:
      if any(prod.codigo == codigo for prod in self.main.produtos):
        for prod in self.main.produtos:
          if prod.codigo == codigo:
            self.main.produtos.remove(prod)
            self.limiteEdit.mostraJanela("Sucesso", "Produto Removido")
      else:
        self.limiteEdit.mostraJanela("Error", "Código inválido")
      self.limiteEdit.inputCod.delete(0,tk.END)

  def edit_prod(self,event):
    codigo = self.limiteEdit.inputCod.get()

    if len(codigo) != 0:
      if any(prod.codigo == codigo for prod in self.main.produtos):
        self.getCodigo = codigo
        self.limiteEdit.edit()
      else:
        self.limiteEdit.mostraJanela("Error", "Código inválido")
      self.limiteEdit.inputCod.delete(0,tk.END)


  def submit_editLimite(self, event):
    codigo = self.limiteEdit.inputCod.get()
    desc = self.limiteEdit.inputDes.get()
    preco = self.limiteEdit.inputPreco.get()

    if len(desc) != 0 or len(preco) != 0 or len(codigo):
      if any(prod.codigo == self.getCodigo for prod in self.main.produtos):
        for prod in self.main.produtos:
          if prod.codigo == self.getCodigo:
            if len(desc) != 0:
              prod.descricao = desc
            if len(preco) != 0:
              prod.precoKg = preco
            if len(codigo) != 0:
              prod.codigo = codigo
            self.limiteEdit.mostraJanela("Sucesso", "Produto atualizado")
      else:
        self.limiteEdit.mostraJanela("Error", "Código inválido")
      self.close_editLimite(event)

  def clear_editLimite(self,event):
    self.limiteEdit.inputCod.delete(0, len(self.limiteIns.inputCod.get()))
    self.limiteEdit.inputDes.delete(0, len(self.limiteIns.inputDes.get()))
    self.limiteEdit.inputPreco.delete(0, len(self.limiteIns.inputPreco.get()))

  def close_editLimite(self, event):
    self.limiteEdit.destroy()