from tkinter import ttk
from Celular import *
import pandas as pd
from tkinter import *
import os


janela = Tk()

class Aplication():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames_da_tela()
        self.botoes_frame1()
        self.lista_frame2()
        self.get_phones()
        self.marca()
        self.arquivo()
        janela.mainloop() #manter janela

    def tela(self):
        self.janela.title("LOJA DO MECÂNICO - CELULARES")
        self.janela.configure(background= 'white') #cor de fundo da minha tela
        self.janela.geometry("600x550") #tamanho da minha tela
        #responsivo
        self.janela.resizable(True, True ) #permitir que mexa no tamanho da tela
        self.janela.maxsize(width=900, height=700)  #maximo que quero da minha tela (largura/altura)
        self.janela.minsize(width=300, height=200) #minimo que irei permitir
    def frames_da_tela(self):
        self.frame_1 = Frame(self.janela, bd= 4, bg= '#6eeef2',
                             highlightbackground='white', highlightthickness= 4)
        #bd =          bg = background highlightback = cor da borda do frame / highlighttth = largura da borda
        #place = posição especifica/fica estático
        self.frame_1.place(relx= 0.02, rely= 0.02, relwidth= 0.96, relheight= 0.46)
        #RELX = largura (esquerdo > direito)
        #RELXY = altura
        #RELWIDTH = largura da tela
        #RELHEIGHT = altura da tela

        self.frame_2 = Frame(self.janela, bd=4, bg='#6eeef2',
                             highlightbackground='white', highlightthickness=4)
        self.frame_2.place(relx= 0.02, rely= 0.5, relwidth= 0.96, relheight= 0.46)

    def botoes_frame1(self):
        ###########botão limpar
        self.bt_limpar = Button(self.frame_1, text="Limpar",
                                bd=3, bg='#0d6efd', fg='white', command=self.limpa_tela)
        self.bt_limpar.place(relx= 0.5, rely=0.1, relwidth=0.1, relheight=0.15)
        #botão buscar tudo
        self.bt_buscar = Button(self.frame_1, text="Read",
                                bd=3, bg='#3db0f7', fg='white', command=self.get_phones)
        self.bt_buscar.place(relx=0.35, rely=0.1, relwidth=0.1, relheight=0.15)

#label escolha

        marcas = [
            "positivo",
            "nokia",
            "motorola",
            "multilaser",
            "xiaomi",
        ]

        self.marca_selecionada = StringVar(self.frame_1)
        self.marca_selecionada.set(marcas[0]) #Começa na posição [0] (positivo)

        self.selectMarcas = OptionMenu(self.frame_1, self.marca_selecionada, *marcas) #Cria botão de marcas

        self.selectMarcas.place(relx=0.2, rely=0.4, relwidth=0.4, relheight=0.2)

        self.bt_escolha = Button(self.frame_1, text="Escolher marca",bd=3, bg='#3db0f7', fg='white', command=self.marca)
        self.bt_escolha.place(relx=0.70, rely=0.44, relwidth=0.2, relheight=0.1)

        # listMarcas = ["Multilaser", "Motorola", "Xiaomi", "Nokia", "Positivo"]
        # self.cb_marcas= ttk.Combobox(self.frame_1, values=listMarcas)
        # self.cb_marcas.set("ESCOLHA A MARCA DE CELULAR")
        # self.cb_marcas.pack()
        # self.cb_marcas.place(relx=0.20, rely=0.55, relwidth=0.6, relheight=0.1)


#utilizar pandas para baixar os dados pro excel (csv/xlsx)

        arquivos = [
            "download em CSV",
            "download em XLSX"
        ]

        self.arquivo_selecionado = StringVar(self.frame_1)
        self.arquivo_selecionado.set(arquivos[0])

        self.selectArquivo = OptionMenu(self.frame_1, self.arquivo_selecionado, *arquivos)

        self.selectArquivo. place(relx=0.2, rely=0.65, relwidth=0.4, relheight=0.2)

        self.bt_arquivo = Button(self.frame_1, text="Escolher arquivo",bd=3, bg='#3db0f7', fg='white', command=self.arquivo)
        self.bt_arquivo.place(relx=0.70, rely=0.70, relwidth=0.2, relheight=0.1)


    def lista_frame2(self):
        #Treeview = tabelinha com rolagem
        self.listaCli = ttk.Treeview(self.frame_2, height=3, columns=("col1", "col2", "col3", "col4"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Marca")
        self.listaCli.heading("#2", text="Modelo")
        self.listaCli.heading("#3", text="Preço")



    #tamanho
        self.listaCli.column("#0", width=15)
        self.listaCli.column("#1", width=270)
        self.listaCli.column("#2", width=150)
        self.listaCli.column("#3", width=80)



        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight= 0.85)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscrollcommand=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)

    def get_phones(self):
        self.listaCli.delete(*self.listaCli.get_children()) #apaga
        celulares = get_all_phones() #pega todos os celulares que tem no bd
        for celular in celulares:
            self.listaCli.insert("", END, values=celular) #percorre e adiciona na lista do tkinter



    def marca(self):
        marca = self.marca_selecionada.get()
        celulares = get_all_marca(marca) #Pega todos os celulares da marca selecionada
        self.listaCli.delete(*self.listaCli.get_children())  # apaga
        for celular in celulares:
            self.listaCli.insert("", END, values=celular)


    def arquivo(self):
        celulares = []
        for linha in self.listaCli.get_children():
            valores = []
            for coluna in self.listaCli.item(linha)['values']:
                valores.append(coluna)
            celulares.append(valores)

        novo_arquivo = pd.DataFrame(celulares, columns=["Marca", "Modelo", "Preço"]) #cria um df e define o nome das colunas

        if self.arquivo_selecionado.get() == "download em XLSX":
            try:
                os.remove('./arquivo.xlsx')
            except:
                print('Arquivo inexistente')
            novo_arquivo.to_excel('arquivo.xlsx', index=False)
        elif self.arquivo_selecionado.get() == "download em CSV":
            try:
                os.remove('./arquivo.csv')
            except:
                print('Arquivo inexistente')
            novo_arquivo.to_csv('arquivo.csv', sep=' ', index=False)


        # celularess = pd.read_excel("dados_celularess.csv", engine="openpyxl")
        # arquivo = self.arquivo_selecionado.get()
        # arquivos = self.marca #Pega todos os celulares da marca selecionada
        # self.listaCli.delete(*self.listaCli.get_children())  # apagar)
        # celularess = pd.read_excel("dados_celularess.csv", engine="openpyxl")
        # novo_arquivo = pd.DataFrame(self.listaCli, columns=['Index', 'Marca', 'Modelo', 'Preco'])
        # new_arquivo = celularess.append(novo_arquivo, ignore_index=True)

        # #ler meu excel/transformar
        # celularess.to_excel('dados_celularess.csv', index=False)


    def limpa_tela(self):
        """
        Pegando a lista e deletando a própria lista e os filhos dela (itens)
        * = pega todos
        """
        self.listaCli.delete(*self.listaCli.get_children())




Aplication()


#READ = LER TUDO
#LIMPAR = LIMPAR TABELA
#GRÁFICO = GERAR O GRÁFICO DOS MAIS E MENOS VENDIDOS
#IMPORTAR ARQUIVO COMO CSV E XLSX
