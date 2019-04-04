print('Program Start')
import discord
import random

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

	async  def on_member_join(self, member):
		await member.guild.system_channel.send(member.name + " has wondered into town!")
	
	async def on_message_delete(self, message):	
		print('Message Deleted!')
		#checks if message was in purge and ignores it	
		for x in self.history:
			if x.id == message.id:
				print('Deleted Massage was in purge')		
				return
		
		if message.author == client.user:
			return		
		
		#ree on delete
		if message.author.permissions_in(message.channel).administrator != True:
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
				responses = ["no u", 
				"This is all part of my 'Potato Play' I swear. :PotatoPlay:", 
				"After all I've done for you this is the thanks I get?!", 
				"Where's you will, huh? Wheres your PrOoF?", 
				"do it you wont", 
				"*Actually,* I'm Sheriff, and you're evil! ", 
				"I claim Jester", 
				"Noted",
				"Someone in deadchat is reeing so hard right now",
				"Oh OK, well I accuse " + message.author.name,
				"I have not been paying attention at all this game...",
				"Wait I already made a deal with town!",
				"**REEEEEEEEEEEEEEEEEEEEEEEE**",
				"can someone give me a small rundown on what the fuck just happened?",
				"Hold on, I need to write my will first.",
				"Wait! I have notes!",
				"I have a will.. but it doesn't fit in one message, so give me a second..",
				"Sooner or later we all knew this day was coming",
				"Hold my beer",
				"I've been roleblocked literally every single night, what do you want from me?",
				"*muffled screaming*",
				"*notices ur accusation* uwu what's this?"
				]
				await message.channel.send(responses[random.randint(0, len(responses)-1)])

		#Help command
		if message.content == '!help':
			await message.channel.send(
'''!help: Opens Help text			
			
!purge: Deletes the most recent messages in a channel
	-Requires User to have Administrator Privileges 
	-Bot Needs to have manage message privileges
	-ONLY USE ON ONE CHANNEL AT A TIME
			''')
		
		#Purge command. Has to be exactly that phrase to reduce the change of accidentally activating	
		if message.content == ('!purge'):
			print("Purge command sent!")
			#checks if user who sent the command has permissions to manage messages which includes deleting messages
			if message.author.permissions_in(message.channel).administrator == True:
				#grab history of channel and turn it into a list using .flatten()
				self.history = await message.channel.history(limit=300).flatten()				
				try:
					await message.channel.delete_messages(self.history[0: 99])
					print("0-99")
					await message.channel.delete_messages(self.history[100: 199])
					print("100-199")
					await message.channel.delete_messages(self.history[200: 300])	
					print("200-300")
				except:
					#bot does not have permissions to execute this command, enables delete message, informs the server it has an issue					
					await message.channel.send('Error: Deleting Messages')					
					return
				#turns re-enables delete messages when purge is done				
			else:
				#yell at whoever tried to run it without permissions
				await message.channel.send('Error: You do not have permissions to use this command')
					
client = MyClient()
client.run(token)
client.max_messages = 10000