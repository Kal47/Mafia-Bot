import discord

print('Program Start')

print('Discord.py version ' + discord.__version__)

print('Opening token file')
try:
	token = open("token.txt","r").read()
except:
	print('Error: Token File Not Found!')
	raise SystemExit(0)
	
print('Success!')
print('Waiting for Ready Event')

class MyClient(discord.Client):

	purgeInProgress = False
	
	async def on_ready(self):
		print('Logged on as {0}!'.format(self.user))
		print('------------------------------------------------------')

	async def on_message_delete(self, message):	
		#checks if purge is going on and disables the delete message
		if self.purgeInProgress:
			return
		
		print('Message Deleted!')
		if message.author == client.user:
			return		
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
		#if message was sent by bot ignore
		if message.author == client.user:
			return	
			
		#Help command
		if message.content.startswith('!help'):
			await message.channel.send(
			'''!help: Opens Help text			
			
		!purge: Deletes 500 of the most recent messages in a channel
			-Requires User to have Administrator Privileges 			
			''')
			
		#Purge command. Has to be exactly that phrase to reduce the change of accidentally activating	
		if message.content == ('!purge'):
			print("Purge command sent!")
			#checks if user who sent the command has permissions to manage messages which includes deleting messages
			if message.author.permissions_in(message.channel).administrator == True:
				#set purgeInProgress to true, this disable the delete message feature
				self.purgeInProgress = True;				
				#grab history of channel and turn it into a list
				history = await message.channel.history(limit=500).flatten()
				#iterate through list calling delete() 
				for x in history:
					try:
						await x.delete()
					except:
						#bot does not have permissions to execute this command, enables delete message, informs the server it has an issue
						self.purgeInProgress = False;
						await message.channel.send('Error: Forbidden: Unable to delete messages due to lack of permissions')
						return
				#turns re-enables delete messages when purge is done
				message.delete()
				self.purgeInProgress = False;
			else:
				#yell at whoever tried to 
				await message.channel.send('Error: You do not have permissions to use this command')
				
			
client = MyClient()
client.run(token)