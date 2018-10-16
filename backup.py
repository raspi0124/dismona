import subprocess
import discord
print("MONAGE BACKUP MODULE STARTED")
import configparser

config = configparser.ConfigParser()
config.read('/root/dismona.conf')

section1 = 'development'
discord_token = config.get(section1, 'discord_token')
db_user = config.get(section1, 'db_user')
db_password = config.get(section1, 'db_password')
db_host = config.get(section1, 'db_host')
db_name = config.get(section1, 'db_name')
@client.event
async def on_message(message):
	if message.content.startswith("/startfaucet"):
		cmd = "pgrep -a python | grep '/root/dismona/faucet.py'"
		process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
		stderr=subprocess.PIPE)
		my_pid, err = process.communicate()
		if len(my_pid.splitlines()) >0:
			s = 'Faucet Module is already running!'
			await client.send_message(message.channel, s)
			exit()
		else:
			s = 'Starting Faucet Module..'
			await client.send_message(message.channel, s)
			cmd = "startfaucet"
			subprocess.Popen(cmd)
			s = "Started!"
			await client.send_message(message.channel, s)
	if message.content.startswith("/status"):
		cmd = "pgrep -a python | grep '/root/dismona/main.py'"
		process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
		stderr=subprocess.PIPE)
		my_pid, err = process.communicate()
		if len(my_pid.splitlines()) >0:
			s = 'Main Module: Running'
		else:
			s = 'Main Module: Down\nRestarting process is starting..'
			await client.send_message(message.channel, s)
			cmd = "refresh"
			subprocess.Popen(cmd)
			cmd = "pgrep -a python | grep '/root/dismona/faucet.py'"
			process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
			stderr=subprocess.PIPE)
			my_pid, err = process.communicate()
			if len(my_pid.splitlines()) >0:
				s = 'Faucet Module: Running'
				await client.send_message(message.channel, s)
			else:
				s = 'Faucet Module: Down\nTo start this, please use /startfaucet. '
				await client.send_message(message.channel, s)
	if message.content.startswith("/start"):
		cmd = "pgrep -a python | grep '/root/dismona/main.py'"
		process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
		stderr=subprocess.PIPE)
		my_pid, err = process.communicate()
		if len(my_pid.splitlines()) >0:
			a = "null"
		else:
			s = 'Main Module: Down\nRestarting process is starting..'
			await client.send_message(message.channel, s)
			cmd = "refresh"
			subprocess.Popen(cmd)
			cmd = "pgrep -a python | grep '/root/dismona/faucet.py'"
			process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
			stderr=subprocess.PIPE)
			my_pid, err = process.communicate()
client.run(discord_token)
