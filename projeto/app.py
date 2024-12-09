import discord
import mysql.connector
from discord import app_commands
from .db import secret_token
from .banco.querys import *


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
            case "!help":
                resposta = '----------------------------------------------------------------------\n\n'
                for c in objComandos:
                    resposta += f'{c["comando"]} : {c["descricao"]}\n'
                resposta+='\n----------------------------------------------------------------------'
                await message.channel.send(resposta)

            case "!addJogo":
                jogo = ' '.join(msg[1:])
                inserir_jogo(jogo)
                await message.channel.send(f"O jogo {jogo.title()} foi inserido com sucesso")
            
            case "!addMDX":
                resposta = '----------------------------------------------------------------------\n\n'

            case "!mostrarJogos":
                resposta = '----------------------------------------------------------------------\n\n'
                jogos = consultar_jogos()
                if len(jogos) > 0:
                    for c in jogos:
                        resposta += f'{c[1]}\n'
                else:
                    resposta += "O BOT ainda não possui jogos cadastrados\n"
                resposta+='\n----------------------------------------------------------------------'
                await message.channel.send(resposta)


            
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

# Cria a instância do cliente
# tree = app_commands.CommandTree(aclient)

# @tree.command(guild=discord.Object(id=id_do_servidor), name='teste', description='Testando') # Comando específico para seu servidor
# async def slash2(interaction: discord.Interaction):
#     await interaction.response.send_message(f'{interaction.type} ', ephemeral=False)



# Inicia o bot com o token fornecido
client.run(secret_token)


