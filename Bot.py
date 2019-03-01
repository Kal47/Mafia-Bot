import discord

print('Program Start')

print('Discord.py version ' + discord.__version__)

print('Opening token file')
try:
	token = open("token.txt","r").read()
except:
	print('Error: Token File Not Found!')
	raise SystemExit(0)
	
print('Opening Jail and Jailcell files')
try:	
	jail = read(open("jail.txt", "r"))		
	jailcell = read(open("jailcell.txt", "r"))
except:
	print("Error: Opening jail.txt or jailcell.txt")
	raise SystemExit(0)


	
print('Success!')
print('Waiting for Ready Event')

class MyClient(discord.Client):
	jail = read(open("jail.txt", "r"))		
	jailcell = read(open("jailcell.txt", "r"))
	

	async def on_ready(self):
		print('Logged on as {0}!'.format(self.user))
		print('------------------------------------------------------')
		

	async def on_message_delete(self, message):
		print('Message Deleted!')
		try:
			await message.channel.send(message.author.mention + ' deleted a message! Its was \n"' + message.content + '"')
		except:
			print('Error Sending Deleted Message!')
			
	
	async def on_message_edit(self, before, after):
		print('Message Edited!')
		if before.content != after.content:
			try:
				await before.channel.send(before.author.mention + ' Edited a message! It was \n"' + before.content + '"')
			except:
				print('Error Sending Edit Message!')
				
	
	async def on_message(self, message):
		if message.author == client.user:
			return
		if message.content.startswith('.help'):
			await message.channel.send('''Mafia Bot!
			.jailer - channel where jailer talks to the jailed
			.jail   - channel where jailed are kept.
			''')
		if message.content.startswith('.jail'):
			f = open("jail.txt", "a")
			f.write(message.channel)
			jail = message.channel
		if message.content.startswith('.jailcell'):
			f = open("jailcell.txt", "a")
			f.write(message.channel)
			jailcell = message.channel
		if message.channel == jail:
			await jailcell.send(message.content)
			
			
client = MyClient()
client.run(token)