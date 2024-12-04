import discord
from discord import app_commands

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
                   {'comando': '!addPartida', 'descricao': 'Adiciona uma partida a um jogo ja existente'}, 
                   {'comando': '!addMDX', 'descricao': 'Adiciona uma melhor de x e qual foram os vencedores'}]
    msg = message.content.split(' ')[0]
    if message.content.startswith('!'):
        
        match msg:
            case "!help":
                resposta = '----------------------------------------------------------------------\n\n'
                for c in objComandos:
                    resposta += f'{c["comando"]} : {c["descricao"]}\n'
                resposta+='\n----------------------------------------------------------------------'
                await message.channel.send(resposta)
            
            case _:
                await message.channel.send("Comando não existente, tente !help para ver o comandos válido")
                

    
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
client.run('MTI0OTQ3MTIxOTE0MTQ0MzY4Ng.GyhIS4.dNsCKzAJIdwHOVEgG7xnhhWx2xQrFF65bc7bjs')