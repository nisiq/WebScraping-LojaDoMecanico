from bd import cursor, mydb


###### ARQUIVO COM TODAS AS OPERAÇÕES DE BANCO DE DADOS

"""Inserir tudo no banco de dados"""
def inserir_modelos(marca, modelo, valor):
    loja = f"""INSERT INTO infos(marca, modelo, preco)
    values ('{marca}', '{modelo}', '{valor}')"""
    cursor.execute(loja)
    mydb.commit()

"""Pega os modelos e o valor e envia pro tkinter"""
def get_all_phones():
    sql = f"SELECT marca,modelo,preco FROM infos";
    cursor.execute(sql)
    celulares = cursor.fetchall()
    return celulares

"""Te dá opção de select qual marca, modelo e preço deseja visualizar"""
def get_all_marca(marca):
    sql = f"SELECT marca,modelo,preco FROM infos where marca = %s"
    cursor.execute(sql, (marca,))
    celulares = cursor.fetchall()
    return celulares