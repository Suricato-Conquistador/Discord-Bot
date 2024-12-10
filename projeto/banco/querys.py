import mysql.connector
from projeto.db import get_database_connection


# Jogos

def consultar_jogos():
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM jogos"
    try:
        cursor.execute(query)
        resultado = cursor.fetchall()
    except mysql.connector.Error as error:
            print(f'Erro ao consultar os jogos: {error}', 'error')
    finally:
        cursor.close()
        connection.close()
    return resultado


def inserir_jogo(nome):
    connection = get_database_connection()
    cursor = connection.cursor()
    query_insert = "INSERT INTO jogos(nome) VALUES (%s)"
    values = (nome,)
    try:
        cursor.execute(query_insert, values)
        connection.commit()
        print("DEU SERTO :)")
    except mysql.connector.Error as error:
            print(f'Erro ao inserir o jogo: {error}', 'error')
    finally:
        cursor.close()
        connection.close()


# Users


def consultar_users():
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM users"
    try:
        cursor.execute(query)
        resultado = cursor.fetchall()
    except mysql.connector.Error as error:
            print(f'Erro ao consultar os users: {error}', 'error')
    finally:
        cursor.close()
        connection.close()
    return resultado


def inserir_users(nome):
    connection = get_database_connection()
    cursor = connection.cursor()
    query_insert = "INSERT INTO users(nome) VALUES (%s)"
    values = (nome,)
    try:
        cursor.execute(query_insert, values)
        connection.commit()
        print("DEU SERTO :)")
    except mysql.connector.Error as error:
            print(f'Erro ao inserir o user: {error}', 'error')
    finally:
        cursor.close()
        connection.close()
