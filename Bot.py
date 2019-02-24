import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	client.send_message(548917655462084630, 'Bot On!')

@client.event
async def on_message_delete(message):
	print('Message Deleted!')
	try:
		await client.send_message(message.channel, message.author.mention + ' ' + message.content)
	except HTTPException:
		print('HTTPException – Sending the message failed.')
	except Forbidden:
		print('Forbidden – You do not have the proper permissions to send the message..')
	except NotFound:
		print('NotFound – The destination was not found and hence is invalid.')
	except InvalidArgument:
		print('InvalidArgument – The destination parameter is invalid.')
	except:
		print('Unknown Error')
		
@client.event
async def on_message_edit(message, after):
	print('Message Edited!')
	try:
		await client.send_message(message.channel, message.author.mention + ' ' + message.content)
	except HTTPException:
		print('HTTPException – Sending the message failed.')
	except Forbidden:
		print('Forbidden – You do not have the proper permissions to send the message..')
	except NotFound:
		print('NotFound – The destination was not found and hence is invalid.')
	except InvalidArgument:
		print('InvalidArgument – The destination parameter is invalid.')
	except:
		print('Unknown Error')
client.run('NTQ4OTIwMjQ4NDkzOTMyNTU1.D1MVhg.arCU5IxCbE9vNE4AcJU6LDKrLdc')