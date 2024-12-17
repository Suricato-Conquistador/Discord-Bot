import discord
import mysql.connector

from discord import app_commands
from .db import secret_token
from .banco.querys import *
from .formatacao.formatacao import *


objComandos = [{'comando':'!help', 'descricao': 'Mostra todos os comandos presentes no BOT'}, 
                   {'comando': '!addJogo', 'descricao': 'Adiciona um jogo ao sistema do BOT'}, 
                   {'comando': '!mostrarJogos', 'descricao': 'Mostra os jogos já adicionados ao BOT'}, 
                   {'comando': '!addUser', 'descricao': 'Adiciona um usuário para a lista'}, 
                   {'comando': '!mostrarUsers', 'descricao': 'Mostra os usuários já adicionados ao BOT'}, 
                   {'comando': '!addMDX', 'descricao': 'Adiciona uma melhor de x e qual foram os vencedores'},
                   {'comando': '!addPartida', 'descricao': 'Adiciona uma partida de uma MDX'}]


id_do_servidor = 1249464842134229013

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Entramos como {client.user}.")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    objComandos = [{'comando':'!help', 'descricao': 'Mostra todos os comandos presentes no BOT'}, 
                   {'comando': '!addJogo', 'descricao': 'Adiciona um jogo ao sistema do BOT'}, 
                   {'comando': '!mostrarJogos', 'descricao': 'Mostra os jogos já adicionados ao BOT'}, 
                   {'comando': '!addUser', 'descricao': 'Adiciona um usuário para a lista'}, 
                   {'comando': '!mostrarUsers', 'descricao': 'Mostra os usuários já adicionados ao BOT'}, 
                   {'comando': '!addMDX', 'descricao': 'Adiciona uma melhor de x e qual foram os vencedores'},
                   {'comando': '!addPartida', 'descricao': 'Adiciona uma partida de uma MDX'}]
    msg = message.content.split(' ')
    if message.content.startswith('!'):
        
        match msg[0]:
            # Caso o usuário digite !help, o bot irá mostrar todos os seus comandos
            case "!help":
                resposta = '----------------------------------------------------------------------\n\n'
                for c in objComandos:
                    resposta += f'{c["comando"]} : {c["descricao"]}\n'
                resposta+='\n----------------------------------------------------------------------'
                await message.channel.send(resposta)

            case "!addJogo":
                jogo = ' '.join(msg[1:]).strip()
                inserir_jogo(jogo)
                await message.channel.send(f"O jogo {jogo.title()} foi inserido com sucesso")
            
            case "!addMDX":
                print("VOU INSEREIR")
                user1, user2 = msg[-2], msg[-1]
                mdx = msg[1]
                jogo = ' '.join(msg[2:-2])
                print(jogo)
                inserir_mdx(mdx, jogo, user1, user2)
                await message.channel.send(f"A melhor de {mdx} entre {user1} e {user2} no {jogo.title()} foi criada com sucesso")

            case "!mostrarMDX":
                mdx_bruto = consultar_mdx()
                resposta = '----------------------------------------------------------------------\n\n'
                resposta += formatar_mdx(mdx_bruto)
                resposta+='\n----------------------------------------------------------------------'
                await message.channel.send(resposta)

            case "!mostrarJogos":
                jogos = consultar_jogos()
                if len(jogos) > 0:
                    resposta = '----------------------------------------------------------------------\n\n'
                    for c in jogos:
                        resposta += f'{c[1]}\n'
                    resposta+='\n----------------------------------------------------------------------'
                else:
                    resposta = "O BOT ainda não possui jogos cadastrados"
                await message.channel.send(resposta)

            case "!addUser":
                user = msg[1].strip()
                inserir_users(user)
                await message.channel.send(f"O user {user} foi inserido com sucesso")

            case "!mostrarUsers":
                users = consultar_users()
                if len(users) > 0:
                    resposta = '----------------------------------------------------------------------\n\n'
                    for c in users:
                        resposta += f'{c[0]} - {c[1]}\n'
                    resposta+='\n----------------------------------------------------------------------'
                else:
                    resposta = "O BOT ainda não possui users cadastrados"
                await message.channel.send(resposta)

            case "!id":
                interaction = discord.Interaction.user
                await message.channel.send(interaction)

            case "!addPartida":
                placar1, placar2 = msg[1], msg[2]
                id_mdx = msg[3]
                inserir_partida(placar1, placar2, id_mdx)
                await message.channel.send(f"A partida terminou com o placar {placar1} x {placar2} e foi inserida com sucesso a MDX {id_mdx}")
            
            case _:
                await message.channel.send("Comando não existente, tente !help para ver o comandos válidos")
                

    
    #     else:
    #         await message.channel.send("Comando não existente, tente !help para ver o comandos válidos")
    # else:
    #     await message.channel.send("Vai tomar no seu cu PORRA")
    


# @client.event
# async def on_message(message):
#     if message.content.startswith('!entrar'):
#         print("oi")

# # Cria a instância do cliente
# tree = app_commands.CommandTree(client)

# @tree.command(guild=discord.Object(id=id_do_servidor), name='help', description='Testando') # Comando específico para seu servidor
# async def slash2(interaction: discord.Interaction):
#     resposta = '----------------------------------------------------------------------\n\n'
#     for c in objComandos:
#         resposta += f'{c["comando"]} : {c["descricao"]}\n'
#     resposta+='\n----------------------------------------------------------------------'
#     await interaction.response.send_message(f'{resposta} ', ephemeral=False)

# @tree.command(guild=discord.Object(id=id_do_servidor), name='teste', description='Mostra os usuários') # Comando específico para seu servidor
# async def slash2(interaction: discord.Interaction):
#     resposta = '----------------------------------------------------------------------\n\n'
#     for c in objComandos:
#         resposta += f'{c["comando"]} : {c["descricao"]}\n'
#     resposta+='\n----------------------------------------------------------------------'
#     # await message.channel.send(resposta)
#     # await interaction.response.send_message(f'{interaction.user.id} ', ephemeral=False)
#     await interaction.response.send_message(f'aaaaa', ephemeral=False)


# Inicia o bot com o token fornecido
client.run(secret_token)


