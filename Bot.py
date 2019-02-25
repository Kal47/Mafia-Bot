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
	async def on_ready(self):
		print('Logged on as {0}!'.format(self.user))
		print('------------------------------------------------------')

	async def on_message_delete(self, message):
		print('Message Deleted!')
		try:
			await message.channel.send(message.author.mention + ' deleted a message! Its was \n"' + message.content + '"')
		except:
			print('Error Sending Deleted Message!')

	def compare( str_1, str_2 ):
		if len(str_1) != len(str_2):
			return 0
		i = 0
		for x in str_1:	
			if str_1[i] != str_2[i]:
				return 0
		i = i + 1
		return 1
	
	async def on_message_edit(self, before, after):
		print('Message Edited!')
		if compate(before.content, after.content) == 0:
			try:
				await before.channel.send(before.author.mention + ' Edited a message! It was \n"' + before.content + '"')
			except:
				print('Error Sending Edit Message!')

client = MyClient()
client.run(token)