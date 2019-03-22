print('Program Start')
import discord

print('Discord.py version ' + discord.__version__)

print('Opening token file')
try:
	token = open("token.txt","r").read()
except:
	print('Error: Token File Not Found!')
	raise SystemExit(0)
	
print('Waiting for Ready Event')

class MyClient(discord.Client):

	purgeInProgress = False
	history = []
	
	async def on_ready(self):
		print('Logged on as {0}!'.format(self.user))
		print('------------------------------------------------------')

		
	async def on_message_delete(self, message):	
		print('Message Deleted!')
		#checks if message was in purge and ignores it	
		for x in self.history:
			if x.id == message.id:
				print('Deleted Massage was in purge')		
				return
		
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
		
		#fun little easter egg		
		if message.content.find("<@" + str(self.user.id) + ">") != -1:				
			if message.content.lower().find("i accuse") != -1:
				responces = ["no u", 
				"Imposable! You have no evidence!", 
				"You wouldn't accuse me unless you are part of the mafia!", 
				"What! I never did anything!", 
				"Don't believe them! I'm innocent!", 
				"Where did this come from! I'm just an innocent townie", 
				"You may have found one, but you will never find us all!", 
				"What no! I did nothing!",
				"I'm not mafia! I'm just a bot!",
				"Oh OK, well I accuse " + message.author.name,
				]
				await message.channel.send(responces[message.id % 10])
				print(str(message.id % 10))
		
		#Help command
		if message.content == '!help':
			await message.channel.send(
'''!help: Opens Help text			
			
		!purge: Deletes 500 of the most recent messages in a channel
			-Requires User to have Administrator Privileges 
			-Bot Needs to have manage message privileges
			-ONLY USE ON ONE CHANNEL AT A TIME
			''')
		
		#Purge command. Has to be exactly that phrase to reduce the change of accidentally activating	
		if message.content == ('!purge'):
			print("Purge command sent!")
			#checks if user who sent the command has permissions to manage messages which includes deleting messages
			if message.author.permissions_in(message.channel).administrator == True:
				#set purgeInProgress to true, this disable the delete message feature
				#self.purgeInProgress = True;				
				#grab history of channel and turn it into a list using .flatten()
				self.history = await message.channel.history(limit=500).flatten()				
				try:
					await message.channel.delete_messages(self.history)
				except:
					#bot does not have permissions to execute this command, enables delete message, informs the server it has an issue					
					await message.channel.send('Error: Forbidden: Unable to delete messages due to lack of permissions')
					self.purgeInProgress = False;
					return
				#turns re-enables delete messages when purge is done				
			else:
				#yell at whoever tried to 
				await message.channel.send('Error: You do not have permissions to use this command')
				self.purgeInProgress = False;
		
client = MyClient()
client.run(token)