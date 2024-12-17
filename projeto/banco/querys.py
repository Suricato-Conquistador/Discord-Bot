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
        # print("DEU SERTO :)")
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


def inserir_users(nome, disc_id=0):
    connection = get_database_connection()
    cursor = connection.cursor()
    query_insert = "INSERT INTO users(nome, id_discord) VALUES (%s, %s)"
    values = (nome, disc_id)
    try:
        cursor.execute(query_insert, values)
        connection.commit()
        # print("DEU SERTO :)")
    except mysql.connector.Error as error:
            print(f'Erro ao inserir o user: {error}', 'error')
    finally:
        cursor.close()
        connection.close()


# MDX


def consultar_mdx():
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM mdx WHERE mdx/2 > placar1 AND mdx/2 > placar2"
    try:
        cursor.execute(query)
        resultado = cursor.fetchall()
    except mysql.connector.Error as error:
        print(f'Erro ao consultar os users: {error}', 'error')
    finally:
        cursor.close()
        connection.close()
    return resultado
    

def inserir_mdx(mdx, jogo, user1, user2):
    connection = get_database_connection()
    cursor = connection.cursor()
    id_jogo = consultar_id_jogo(jogo)
    id_u1, id_u2 = consultar_id_user(user1), consultar_id_user(user2)
    query_insert = "INSERT INTO mdx(mdx, id_jogo, id_user1, id_user2) VALUES (%s, %s, %s, %s)"
    values = (mdx, id_jogo, id_u1, id_u2)
    try:
        cursor.execute(query_insert, values)
        connection.commit()
        # print("DEU SERTO :)")
    except mysql.connector.Error as error:
            print(f'Erro ao inserir o user: {error}', 'error')
    finally:
        cursor.close()
        connection.close()


def consultar_id_jogo(jogo):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "SELECT id FROM jogos WHERE nome = %s"
    values = (jogo,)
    try:
        cursor.execute(query, values)
        resultado = cursor.fetchone()
    except mysql.connector.Error as error:
            print(f'Erro ao consultar os users: {error}', 'error')
    finally:
        cursor.close()
        connection.close()
    return resultado[0]


def consultar_id_user(user):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "SELECT id FROM users WHERE nome = %s"
    values = (user,)
    try:
        cursor.execute(query, values)
        resultado = cursor.fetchone()
    except mysql.connector.Error as error:
            print(f'Erro ao consultar os users: {error}', 'error')
    finally:
        cursor.close()
        connection.close()
    return resultado[0]


# Partida


def consultar_partida():
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM partidas"
    try:
        cursor.execute(query)
        resultado = cursor.fetchall()
    except mysql.connector.Error as error:
            print(f'Erro ao consultar os users: {error}', 'error')
    finally:
        cursor.close()
        connection.close()
    return resultado


def inserir_partida(placar1, placar2, id_mdx):
    connection = get_database_connection()
    cursor = connection.cursor()
    query_insert = "INSERT INTO partidas(placar1, placar2, id_mdx) VALUES (%s, %s, %s)"
    values = (placar1, placar2, id_mdx)
    try:
        cursor.execute(query_insert, values)
        connection.commit()
        # print("DEU SERTO :)")
    except mysql.connector.Error as error:
            print(f'Erro ao inserir o user: {error}', 'error')
    finally:
        cursor.close()
        connection.close()
