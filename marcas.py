from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from Celular import inserir_modelos

class Marcas:
    def __init__(self):
        self.marca = ''
        """
        Site oficial
        """
        self.site = 'https://www.lojadomecanico.com.br/'

        """
        Caminho de cada marca (modelo e valor)
        """
        self.map = {
            'positivo': {
                'desc': { 'xpath': '/html/body/div[6]/div/div/div[4]/div[3]/div/div/div/div/div/div[%marca%]/div/div[2]/h3'},
                'valor': {'xpath': '/html/body/div[6]/div/div/div[4]/div[3]/div/div/div/div/div/div[$valor$]/div/div[2]/div[1]/p'}
            },
            'nokia': {
                'desc': { 'xpath': '/html/body/div[6]/div/div/div[4]/div[3]/div/div/div/div/div/div[%marca%]/div/div[2]/h3'},
                'valor': {'xpath': '/html/body/div[6]/div/div/div[4]/div[3]/div/div/div/div/div/div[$valor$]/div/div[2]/div[1]/p'}
            },
            'xiaomi': {
                'desc': { 'xpath': '/html/body/div[6]/div/div/div[4]/div[3]/div/div/div/div/div/div[%marca%]/div/div[2]/h3'},
                'valor': {'xpath': '/html/body/div[6]/div/div/div[4]/div[3]/div/div/div/div/div/div[$valor$]/div/div[2]/div[1]/p'}
            },
            'motorola': {
                'desc': { 'xpath': '/html/body/div[6]/div/div/div[4]/div[3]/div/div/div/div/div/div[%marca%]/div/div[2]/h3'},
                'valor': {'xpath': '/html/body/div[6]/div/div/div[4]/div[3]/div/div/div/div/div/div[$valor$]/div/div[2]/div[1]/p'}
            },
            'multilaser': {
                'desc':{'xpath': '/html/body/div[6]/div/div/div[4]/div[3]/div/div/div/div/div/div[%marca%]/div/div[2]/h3'},
                'valor': {'xpath': '/html/body/div[6]/div/div/div[4]/div[3]/div/div/div/div/div/div[$valor$]/div/div[2]/div[1]/p'}
            }
        }
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.abrir()

    def abrir(self):
        """
        Faz webscraping e manda inserir no banco de dados.
        """
        print(f'{self.marca}')
        marcas = ['positivo', 'nokia', 'xiaomi', 'motorola', 'multilaser']
        for marca in marcas:
            self.driver.get('https://www.lojadomecanico.com.br/busca?q=smartphone%20marca'.replace("marca",marca))
            sleep(20)
            for i in range(1, 10):
               modelo = self.driver.find_element(By.XPATH,
                                                 self.map[f'{marca}']['desc']['xpath'].replace('%marca%',
                                                                                                       f'{i}')).text
               valor = self.driver.find_element(By.XPATH,
                                                self.map[f'{marca}']['valor']['xpath'].replace('$valor$',
                                                                                                       f'{i}')).text
               print("MODELO: ", modelo, end='\t')
               sleep(1)
               print("VALOR: ", valor, end=' ')
               print("")
               """
               Insere no banco de dados
               """
               inserir_modelos(marca, modelo, valor)


p = Marcas()