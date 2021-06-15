import discord, json


client = discord.Client()

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$off'):
        await client.logout()
        quit()

with open('config.json', 'r') as f:
    config = json.load(f)

client.run(config["token"])
