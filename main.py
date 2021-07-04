import discord, json


client = discord.Client()

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_mesg = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_mesg} in {channel}')

    if message.author == client.user:
        return 
    
    if message.channel.name == 'test':
        if message.content.startswith('$hello'):
            await message.channel.send(f'Hello {username}!')

        elif message.content.startswith('$newr'):
            await message.channel.send("What is the reminder: ")
            

        elif message.content.startswith('$bye'):
            await client.logout()
            quit()

with open('config.json', 'r') as f:
    config = json.load(f)

client.run(config["token"])
