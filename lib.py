import sqlite3
import subprocess
import re
def createaccount(username):
	fromuser = username
	dbpath = '/root/dismona.sqlite'
	connection = sqlite3.connect(dbpath)
	# 自動コミットにする場合は下記を指定（コメントアウトを解除のこと）
	# connection.isolation_level = None
	cursor = connection.cursor()
	cmd = "monacoin-cli getnewaddress " + username + ""
	rut  =  subprocess.check_output( cmd.split(" ") )
	print ('Creating <' + fromuser + ">s account.. user ID ")
	#cursor.execute("insert into dismona.id(id,address) values('message_author', address);")
	resultaddress = rut.decode()
	resultmore = resultaddress.replace('[', '')
	resultmore2 = resultmore.replace(']', '')
	resultmore3 = resultmore2.replace('"', '')
	resultmore4 = resultmore3.replace("\n", "")
	resultmore5 = resultmore4.replace(" ", "")
	address = resultmore5
	cursor.execute("INSERT INTO addresses (username, address) VALUES (?, ?)", (username, resultmore5))
	return address
def getaddress(username):
	fromuser = username
	dbpath = '/root/dismona.sqlite'
	connection = sqlite3.connect(dbpath)
	# 自動コミットにする場合は下記を指定（コメントアウトを解除のこと）
	# connection.isolation_level = None
	cursor = connection.cursor()
	username2 = "'" + username + "'"
	query = 'select address from accounts where username = ' + username2 + ''
	print(query)
	cursor.execute(query)
	address = cursor.fetchall()
	print(address)
	address = address[0]
	address = str(address)
	address = address.rstrip()
	address = address.replace("'", "")
	address = address.replace("(", "")
	address = address.replace(")", "")
	address = address.replace(",", "")
	address = address.replace("\\n", "")
	return address
def getbalance(username):
	fromuser = username
	cmd = "monacoin-cli getbalance " + username + ""
	rut  =  subprocess.check_output( cmd.split(" ") )
	balance = rut.decode()
	return balance
def move(fromuser, to, amount):
	dbpath = '/root/dismona.sqlite'
	connection = sqlite3.connect(dbpath)
	# 自動コミットにする場合は下記を指定（コメントアウトを解除のこと）
	# connection.isolation_level = None
	cursor = connection.cursor()
	cmda = "monacoin-cli walletpassphrase 0124 10"
	ruta  =  subprocess.check_output( cmda.split(" ") )
	print(ruta)
	balance = getbalance(fromuser)
	num2 = 100000000
	balance = float(balance) * float(num2)
	print ("balance")
	print(balance)
	tipto = to
	tipamount = amount
	print("tipamount")
	print(tipamount)
	tipamount = float(tipamount) * float(num2)
	print("multiplyed tipamount")
	print(tipamount)
	minimumtip = "1"
	minimumtip = float(minimumtip)
	if tipamount <= balance:
		if tipamount >= minimumtip:
			try:
				username = fromuser
				tipamount = float(tipamount) / float(num2)
				tipamount = str(tipamount)
				cmd2 = "monacoin-cli move " + fromuser + " " + tipto + " " + tipamount + ""
				rut2  =  subprocess.check_output( cmd2.split(" ") )
				m = "<@" + fromuser + "> sent " + tipamount + " mona to <@" + tipto + ">!\n(message created on " + currenttime + ")"
				cursor.execute("INSERT INTO tiped (id) VALUES (?)", (username,))
				connection.commit()
				cursor.execute("INSERT INTO tiped (id) VALUES (?)", (tipto,))
			except subprocess.CalledProcessError as e:
				eout = e.output.decode()
				m = "<@" + fromuser + ">, sorry, failed to complete your request: <@" + tipto + "> is not yet registered.\n(message created on " + currenttime + ")"
		else:
			m = "<@" + fromuser + ">, sorry, failed to complete your request: your tip must meet the minimum of 10 watanabe (0.00000010 Mona).\n(message created on " + currenttime + ")"
	else:
		m = "<@"+ fromuser + ">, sorry, failed to complete your request: you do not have enough Mona in your account, please double check your balance and your tip amount.\n(message created on " + currenttime + "\n DEBUG: tipamount:" + tipamount + " balance:" + balance + " "
	return m

def withdraw(fromuser, to, amount):
	cmda = "monacoin-cli walletpassphrase 0124 10"
	ruta  =  subprocess.check_output( cmda.split(" ") )
	print(ruta)
	currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
	#getbalance
	balancea = getbalance(fromuser)
	withdrawamount = amount
	fee = "0.005"
	rewithdrawamount = float(withdrawamount) - float(fee)
	rewithdrawamount = str(rewithdrawamount)
	withdrawto = to
	print("--withdrawto--")
	print(withdrawto)
	print("--withdrawamount--")
	print(withdrawamount)
	print("--rewithdrawamount--")
	print(rewithdrawamount)
	if withdrawamount >= "0.01":
		if balancea >= "0":
			if balancea >= "0.01":
				cmd = "monacoin-cli sendfrom " + fromuser + " " + withdrawto + " " + rewithdrawamount + ""
				rut  =  subprocess.check_output( cmd.split(" ") )
				cmd = "monacoin-cli move " + fromuser + " fee " + fee + ""
				ruta  =  subprocess.check_output( cmd.split(" ") )
				print(rut)
				rut = rut.decode()
				m = "<@" + fromuser + ">, " + rewithdrawamount + "mona has been withdrawn to " + withdrawto + ". Transaction details can be found here: https://mona.chainsight.info/tx/" + rut + "\n(message created on " + currenttime + ")"
				cmda = "monacoin-cli getbalance " + fromuser + ""
				ruta  =  subprocess.check_output( cmda.split(" ") )
				balancea = ruta.decode()
				if balancea <= "0":
					defo = "0"
					amounttosendback = float(defo) - float(balancea)
					print("--amounttosendback--")
					print(amounttosendback)
					amounttosendback = str(amounttosendback)


					cmd = "monacoin-cli move fee "  + fromuser + " " + amounttosendback + ""
					ruta  =  subprocess.check_output( cmd.split(" ") )
					print(ruta)

			else:
				m = "<@" + fromuser + "> sorry, failed to complete your request: you do not have enogh mona for withdraw. \n please note that the minimum withdraw amount is 0.01mona.(message created on " + currenttime + ")"

		else:
			m = "<@" + fromuser + ">sorry, failed to complete your request: you do not have any mona at all!(message created on " + currenttime + ")"

	else:
		m = "<@" + fromuser + "> sorry, failed to complete your request: you do not have enogh mona for withdraw. \n please note that the minimum withdraw amount is 0.01mona.(message created on " + currenttime + ")"

	return m
