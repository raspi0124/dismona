import requests
import json
import subprocess
import sqlite3
import re
import discord
dbpath = '/root/monaparty.sqlite'
connection = sqlite3.connect(dbpath)
cursor = connection.cursor()

if message.content.startswith('/mp info'):
	await client.add_reaction(message, '👌')
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Accept': 'application/json, text/javascript',
    }
    data = '{ "jsonrpc": "2.0", "id": 0, "method": "get_running_info" }'
    response = requests.post('https://api.monaparty.me/api/counterparty', headers=headers, data=data, auth=('rpc', 'hello'))
    m = str(response)
    await client.send_message(reaction.message.channel, m)

if message.content.startswith('/mp balance'):
    address = re.split('\W+', message.content)
    addresses = address[2]
    addresses = '"' + addresses + '"'

    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Accept': 'application/json, text/javascript',
    }
    data = '{ "jsonrpc": "2.0", "id": 0, "method": "get_normalized_balances" "addresses": ' + addresses +' }'
    response = requests.post('https://wallet.monaparty.me/_api', headers=headers, data=data, auth=('rpc', 'hello'))
    m = "here is " + addresses + " balance" + response + ""
