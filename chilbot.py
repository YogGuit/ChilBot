import discord
from pprint import pprint 
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    pprint(message.author.name)
    pprint(message)
    if message.author == client.user:
        return
    if message.author.bot==True:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    if (message.content.upper())=="おいChilBOT".upper():
        await message.channel.send('うるせえ！！！！')
    
    if (message.content=="マクドね"):
        repeat+=1
        if(repeat<3):
            await message.channel.send('マクナルね')
    #await message.channel.send(message.author.name)

client.run('NzUzMjQyOTIwMjgyNDg4ODUy.X1jWIg.pzTavEbrjImctu1dC5HFyIri9ac')