from tkinter import *
from model import *



notaConfig = {
    'bg': 'lemon chiffon',
    'font': ('TimesNewToman',10)
}



class PrintNotaFiscal(Toplevel):
    def __init__(self, root, nota:NotaFiscal):
        Toplevel.__init__(self, root)
        self.geometry('330x590')
        self.resizable(False,False)
        self._nf = nota

        self.config(bg='lemon chiffon')
        self.title('')

        self._mainFrame = Frame(self,bg='lemon chiffon')
        self._mainFrame.pack(fill='both',expand=1)

        self._canvas = Canvas(self._mainFrame,bg='lemon chiffon',width=150)
        self._canvas.pack(side='left',fill='both',expand=1)

        self._scrollbar = Scrollbar(self._mainFrame, orient=VERTICAL,command=self._canvas.yview)
        self._scrollbar.pack(side='right',fill=Y)

        self._canvas.config(yscrollcommand=self._scrollbar.set)
        self._canvas.bind('<Configure>', lambda e: self._canvas.config(scrollregion=self._canvas.bbox('all')))

        self._frameCanvas = Frame(self._canvas,width=150,padx=50,bg='lemon chiffon')

        self._canvas.create_window((0,0),window=self._frameCanvas,anchor=NW)


        self._head = Frame(self._frameCanvas,bg='lemon chiffon')
        self._nota = Frame(self._frameCanvas,bg='lemon chiffon')
        self._cliente = Frame(self._frameCanvas,bg='lemon chiffon')
        self._produto = Frame(self._frameCanvas,bg='lemon chiffon')
        self._total = Frame(self._frameCanvas,bg='lemon chiffon')


        Label(self._head, text='Nota Fiscal',font=('TimesNewRoman',13,'bold')\
              ,cnf=notaConfig).pack(fill='x')
        Label(self._head, text='Açougue SA',\
              cnf=notaConfig).pack(fill='x')

        Label(self._nota,text='- - - - - - - - - - - - - - - - - - - - - - - - - - -'\
              ,font=('TimesNewRoman',10,'bold'),cnf=notaConfig).pack(fill='x')
        Label(self._nota,text='Identificador: '+str(self._nf.identificador)\
              ,cnf=notaConfig,anchor=W).pack(fill='x',padx=27)
        Label(self._nota,cnf=notaConfig,anchor=W,\
              text='Data: '+ self._nf.dataFormatada).pack(fill='x',padx=27)

        Label(self._cliente,text='- - - - - - - - - - - - - - - - - - - - - - - - - - -',\
              font=('TimesNewRoman',10,'bold'),cnf=notaConfig).pack(fill='x')
        Label(self._cliente,text='Cliente: '+str(self._nf.cliente.nome),\
              cnf=notaConfig,anchor=W).pack(fill='x',padx=27)
        cpf = self._nf.cliente.cpf
        cpf = cpf[0:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:11]
        Label(self._cliente,text='CPF: '+ cpf,\
              cnf=notaConfig,anchor=W).pack(fill='x',padx=27)
        ## Label endereço
        Label(self._cliente,text='Email: '+str(self._nf.cliente.email),\
              cnf=notaConfig,anchor=W).pack(fill='x',padx=27)
        Label(self._cliente,text='Endereço: '+str(self._nf.cliente.endereco),\
              cnf=notaConfig,anchor=W).pack(fill='x',padx=27)

        for prod in self._nf.produtos.keys():
            Label(self._produto,\
                  text='- - - - - - - - - - - - - - - - - - - - - - - - - - -',\
                  font=('TimesNewRoman',10,'bold'),cnf=notaConfig).pack(fill='x')
            Label(self._produto,text=str(prod.codigo)+' - '+str(prod.descricao),\
                  cnf=notaConfig,anchor=W).pack(fill='x',padx=27)
            Label(self._produto,text='R$'+str('%.2f' % prod.precoKg)+' * '+\
                  str(self._nf.get_qtdProduto(prod.codigo))+\
                  'kg = R$'+str('%.2f' % self._nf.calcular_valorProduto(prod.codigo)),\
                  cnf=notaConfig,anchor=E).pack(fill='x',padx=27)

        Label(self._total,text='- - - - - - - - - - - - - - - - - - - - - - - - - - -',\
                  font=('TimesNewRoman',10,'bold'),cnf=notaConfig).pack(fill='x')
        Label(self._total,text='Valor total da nota: R$'\
              + str('%.2f' % self._nf.calcular_valorNota()),\
              cnf=notaConfig,anchor=E).pack(fill='x',padx=27)

        self._head.pack(fill='both')
        self._nota.pack(fill='both')
        self._cliente.pack(fill='both')
        self._produto.pack(fill='both')
        self._total.pack(fill='both')