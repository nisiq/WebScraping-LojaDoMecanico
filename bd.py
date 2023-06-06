import mysql.connector

"""Conectar com o banco de dados"""
try:
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='senai',
        database='celulares'
    )
except Exception as e:
    print(f"We can't connected with the server. \033[31m ERROR!: {e} \033[m")
else:
    cursor = mydb.cursor()