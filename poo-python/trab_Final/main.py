import tkinter as tk
import produto
import cliente
import venda
import consulta
import faturamento
import pickle as pk
import os.path
from tkinter import messagebox
import model as md


class LimitePrincipal():

  def __init__(self, root, controle):
    self.controle = controle
    self.root = root
    self.root.geometry("400x300")
    self.menubar = tk.Menu(self.root)
    self.menuProd = tk.Menu(self.root)
    self.menuCliente = tk.Menu(self.root)
    self.menuVenda = tk.Menu(self.root)
    self.menuFaturamento = tk.Menu(self.root)
    self.menuConsulta = tk.Menu(self.root)

    self.menuProd.add_command(label="Cadastrar", command=self.controle.addProd)
    self.menuProd.add_command(label="Consultar",
                              command=self.controle.consultaProd)
    self.menuProd.add_command(label='Editar/Excluir', command=self.controle.editProd)
    self.menubar.add_cascade(label="Produto", menu=self.menuProd)

    self.menuCliente.add_command(label="Cadastrar",
                                 command=self.controle.addCliente)
    self.menuCliente.add_command(label="Consultar",
                                 command=self.controle.consultaCliente)
    self.menubar.add_cascade(label="Cliente", menu=self.menuCliente)

    self.menuVenda.add_command(label="Inserir", command=self.controle.addVenda)
    self.menuVenda.add_command(label="Consultar",
                               command=self.controle.consultaVenda)
    self.menubar.add_cascade(label="Venda", menu=self.menuVenda)

    self.menuFaturamento.add_command(label="Produto",
                                     command=self.controle.fatProd)
    self.menuFaturamento.add_command(label="Cliente",
                                     command=self.controle.fatCliente)
    self.menuFaturamento.add_command(label="Periodo",
                                     command=self.controle.fatPeriodo)
    self.menubar.add_cascade(label="Faturamento", menu=self.menuFaturamento)

    self.menuConsulta.add_command(label='Vendas por período'\
                                  ,command=self.controle.vendas_periodo)
    self.menuConsulta.add_command(label='Produtos mais vendidos'\
                                  ,command=self.controle.prod_vendidos)
    self.menubar.add_cascade(label='Consulta',menu=self.menuConsulta)

    self.menubar.add_command(label="Salvar", command=self.controle.salvar)

    self.root.config(menu=self.menubar)


class ControlePrincipal():

  def __init__(self):
    self._load_files()
    self.root = tk.Tk()

    self.ctrlProduto = produto.ctrlProduto(self)
    self.ctrlCliente = cliente.CtrlCliente(self)
    self.ctrlVenda = venda.CtrlVenda(self)
    self.ctrlConsuta = consulta.CtrlConsulta(self)
    self.ctrlFaturamento = faturamento.CtrlFaturamento(self)

    self.limite = LimitePrincipal(self.root, self)

    self.root.title("Açougue")

    self.root.mainloop()

  def _input_produtos(self):
    self.produtos.append(md.Produto('101','Patinho bovino',35.5))
    self.produtos.append(md.Produto('102','Contra-filé bovino',34.3))
    self.produtos.append(md.Produto('103','Lombo suíno',24.8))
    self.produtos.append(md.Produto('104','Peito de frango',20.6))
    self.produtos.append(md.Produto('105','Acém bovino',31.9))

  def _input_clientes(self):
    self.clientes.append(md.Cliente('Jaime Gil',\
                                    'Rua Consolação',\
                                    'jaime@email.com',\
                                    44977197070))
    self.clientes.append(md.Cliente('Frantz Fanon',\
                                    'Rua Argelina',\
                                    'frantz@email.com',\
                                    31251650082))

  def _load_files(self):
    if not os.path.isfile('clientes.pickle'):
      self.clientes = []
      self._input_clientes()
    else:
      with open('clientes.pickle', 'rb') as file:
        self.clientes = pk.load(file)

    if not os.path.isfile('produtos.pickle'):
      self.produtos = []
      self._input_produtos()
    else:
      with open('produtos.pickle','rb') as file:
        self.produtos = pk.load(file)

    if not os.path.isfile('vendas.pickle'):
      self.vendas = []
    else:
      with open('vendas.pickle','rb') as file:
        self.vendas = pk.load(file)

  #chamar salva de todos os controladores
  def salvar(self):
    if len(self.clientes) != 0:
      with open('clientes.pickle','wb') as file:
        pk.dump(self.clientes, file)
    if len(self.produtos) != 0:
      with open('produtos.pickle','wb') as file:
        pk.dump(self.produtos, file)
    if len(self.vendas) != 0:
      with open('vendas.pickle','wb') as file:
        pk.dump(self.vendas, file)

    messagebox.showinfo('Atenção','As informações foram salvas')

  def addProd(self):
    self.ctrlProduto.cadastraProduto()

  def consultaProd(self):
    self.ctrlProduto.BuscaProduto()

  def editProd(self):
    self.ctrlProduto.EditProduto()

  def addCliente(self):
    self.ctrlCliente.cadastraCliente()

  def consultaCliente(self):
    self.ctrlCliente.buscaCliente()

  def addVenda(self):
    self.ctrlVenda.inserir_venda()

  def consultaVenda(self):
    self.ctrlVenda.buscar_venda()

  def fatProd(self):
    self.ctrlFaturamento.faturamentoProd()

  def fatCliente(self):
    self.ctrlFaturamento.faturamentoCliente()

  def fatPeriodo(self):
    self.ctrlFaturamento.faturamentoPeriodo()

  def vendas_periodo(self):
    self.ctrlConsuta.vendas_periodo()

  def prod_vendidos(self):
    self.ctrlConsuta.prod_vendidos()

if __name__ == "__main__":
  c = ControlePrincipal()