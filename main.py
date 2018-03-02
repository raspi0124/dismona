import discord
import subprocess
import re
import time
import math
import random
#import MySQLdb
client = discord.Client()
from datetime import datetime
print (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
import signal

cmda = "monacoin-cli walletpassphrase 0124 32140800"
ruta  =  subprocess.check_output( cmda.split(" ") )
print(ruta)
number1 = "1"
print(number1)
print(5 - 0.5)
# This program minus two numbers

num1 = 1.4
num2 = 0.01

# Add two numbers
sum = float(num1) - float(num2)

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

print(sum)
data = "100000"
data = float(data)
data_size = int (math.log10(data) + 1)
print(data_size)
print(random.randrange(10, 20, 2))
print(random.randrange(1, 50, 2))
def sigint_handler(signum, frame):
    print ('Stop pressing the CTRL+C!')
# データベース接続とカーソル生成
# 接続情報はダミーです。お手元の環境にあわせてください。
#connection = MySQLdb.connect(
#   host='localhost', user='root', passwd='laksjd', db='dismona', charset='utf8')
#cursor = connection.cursor()
#cursor.execute("CREATE TABLE IF NOT EXISTS dismona.id (id VARCHAR(20), address VARCHAR(50));")
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name='/help'))
    time.sleep(1)
    await client.change_presence(game=discord.Game(name=''))


#message.author.name がユーザー名

@client.event
async def on_message(message):
    print("" + message.author.name + " said " + message.content + ". userid:" + message.author.id + "")
    file = open('/home/raspi0124/alllog.txt', 'a')  #追加書き込みモードでオープン
    allmessage = "" + message.author.name + " said " + message.content + " \n"
    file.writelines(allmessage)
    # 「/register」で始まるか調べる
    if message.content.startswith("/register"):
        await client.add_reaction(message, '👌')
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author.name:
            # メッセージを書きます
            m = "<@" + message.author.id + "> さんのアカウントを作成しますね！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await client.send_message(message.channel, m)
            cmd = "monacoin-cli getnewaddress " + message.author.id + ""
            rut  =  subprocess.check_output( cmd.split(" ") )
            print ('Creating <' + message.author.id + ">s account.. user ID ")
            print ("---1---")
            #cursor.execute("insert into dismona.id(id,address) values('message_author', address);")
            resultaddress = rut.decode()
            resultmore = resultaddress.replace('[', '')
            resultmore2 = resultmore.replace(']', '')
            resultmore3 = resultmore2.replace('"', '')
            resultmore4 = resultmore3.replace("\n", "")
            resultmore5 = resultmore4.replace(" ", "")
            print ("---2---")
            #DEBUG
            print ("---decoded---")
            print (resultaddress)
            print ("-----------------")
            print ("---address---")
            print(resultaddress)
            print ("----------------")
            print ("---resultmoreaddress---")
            print (resultmore3)
            print ("------------------------------")
            print ("---removednaddress---")
            print (resultmore4)
            print("-------------------------------")
            print ("---removedsaddress---")
            print (resultmore5)
            print("-------------------------------")
            #DEBUG FIN
            print ("---3---")
            #cursor.execute("INSERT INTO dismona.id(id, address) VALUES ('" + message.author.id + "', '" + resultmore5 + "' )")
            print ("---4---")
            #print ('----MYSQL COMMAND START----')
            #print ("INSERT INTO dismona.id(id, address) VALUES ('" + message.author.id + "', '" + resultmore5 + "' )")
            #print ('----MYSQL COMMAND END----')
            print ("---5---")
            currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
            m = "<@" + message.author.id + ">, successfully created an account for you! Your new address is " + resultmore5 + ", enjoy!\n(message created on " + currenttime + ")"
            print ("---6---")
            await client.send_message(message.channel, m)

    if message.content == "/test":
        m = "test"
        await client.send_message(message.channel, m)

    if message.content.startswith("/balance"):
        await client.add_reaction(message, '👌')
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author.name:
            # メッセージを書きます
                m = "<@" + message.author.id + "> さんの残高チェック中.."
            # メッセージが送られてきたチャンネルへメッセージを送ります
                await client.send_message(message.channel, m)
                cmd = "monacoin-cli getbalance " + message.author.id + ""
                rut  =  subprocess.check_output( cmd.split(" ") )
                balance = rut.decode()
                currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
                m = "<@" + message.author.id + ">, you currently have  " + balance + " mona!\n(message created on " + currenttime + ")"
                print ("---6---")
                await client.send_message(message.channel, m)
    if message.content.startswith("/deposit"):
        await client.add_reaction(message, '👌')
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author.name:
            # メッセージを書きます
                m = "<@" + message.author.id + "> アドレスを確認中..."
            # メッセージが送られてきたチャンネルへメッセージを送ります
                await client.send_message(message.channel, m)
                cmd = "monacoin-cli getaddressesbyaccount " + message.author.id + ""
                rut  =  subprocess.check_output( cmd.split(" ") )
                address = rut.decode()
                address2 = address.replace('[', '')
                address3 = address2.replace(']', '')
                currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
                m = "<@" + message.author.id + ">, the following are your deposit addresses:" + address3 + "\n(message created on " + currenttime + ")"
                await client.send_message(message.channel, m)
    if message.content.startswith("/list"):
        await client.add_reaction(message, '👌')
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author.name:
            # メッセージを書きます
                m = "<@" + message.author.id + "> アドレスを確認中..."
            # メッセージが送られてきたチャンネルへメッセージを送ります
                await client.send_message(message.channel, m)
                cmd = "monacoin-cli getaddressesbyaccount " + message.author.id + ""
                rut  =  subprocess.check_output( cmd.split(" ") )
                address = rut.decode()
                address2 = address.replace('[', '')
                address3 = address2.replace(']', '')
                currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
                m = "<@"+ message.author.id + ">,your address is" + address3 + " \n Created message at " + currenttime + ""
                await client.send_message(message.channel, m)
#    if message.content.startswith("/withdrawall"):
#        currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
#        await client.add_reaction(message, '👌')
#        message2 = message.content.replace('/withdrawall', '')
#        message3 = message2.replace(' ', '')
#        print (message3)
#        cmda = "monacoin-cli getbalance " + message.author.id + ""
#        ruta  =  subprocess.check_output( cmda.split(" ") )
#        balancea = ruta.decode()
#        fee = "0.005"
#        m ="<@" + message.author.id + ">, preparing your withdrawal, please wait."
#        await client.send_message(message.channel, m)
#        if balancea >= "0":
#                if balancea >= "0.01":
#                    m = "<@" + message.author.id + ">, executing your withdrawal to " + message3 + ""
#                    await client.send_message(message.channel, m)
#                    sum = float(balancea) - float(fee)
#                    sum = round(sum,5)
#                    sum = str(sum)
#                    print("monacoin-cli sendfrom " + message.author.id + " " + message3 + " " + sum + "")
#                    print("monacoin-cli move " + message.author.id + " fee " + fee + "")
#                    cmd = "monacoin-cli sendfrom " + message.author.id + " " + message3 + " " + sum + ""
#                    rut  =  subprocess.check_output( cmd.split(" ") )
#                    cmd = "monacoin-cli move " + message.author.id + " fee " + fee + ""
#                    ruta  =  subprocess.check_output( cmd.split(" ") )
#                    withdrawalldata = rut.decode()
#                    print(withdrawalldata)
#                    m = "<@" + message.author.id + ">, all of your Mona (except for fee) has been withdrawn to " + message3 + ". Transaction details can be found here: https://mona.chainsight.info/tx/" + withdrawalldata + "\n(message created on " + currenttime + ")"
#                    await client.send_message(message.channel, m)
#               else:
#                    m = "<@" + message.author.id + "> sorry, failed to complete your request: you do not have enogh mona for withdraw. \n please note that the minimum withdraw amount is 0.01mona.(message created on " + currenttime + ")"
#                    await client.send_message(message.channel, m)
#        else:
#            m = "<@" + message.author.id + ">sorry, failed to complete your request: you do not have any mona at all!(message created on " + currenttime + ")"
#            await client.send_message(message.channel, m)
    if message.content.startswith("/withdraw"):
        currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
        #getbalance
        cmda = "monacoin-cli getbalance " + message.author.id + ""
        ruta  =  subprocess.check_output( cmda.split(" ") )
        balancea = ruta.decode()
        #okikae
        rmessage = message.content.replace('/withdraw', '')
        print(rmessage)
        pattern = r'([+-]?[0-9]+\.?[0-9]*)'
        print(re.findall(pattern,rmessage))
        withdrawinfo = re.findall(pattern,rmessage)
        print(withdrawinfo[0])
        withdrawamount = withdrawinfo[0]
        rmessage = rmessage.replace(withdrawamount, '')
        withdrawto = rmessage.replace(' ', '')
        fee = "0.005"
        rewithdrawamount = float(withdrawamount) - float(fee)
        rewithdrawamount = str(rewithdrawamount)
        print("--withdrawto--")
        print(withdrawto)
        print("--withdrawamount--")
        print(withdrawamount)
        print("--rewithdrawamount--")
        print(rewithdrawamount)
        if withdrawamount >= "0.01":
            if balancea >= "0":
                if balancea >= "0.01":
                    await client.add_reaction(message, '👌')
                    cmd = "monacoin-cli sendfrom " + message.author.id + " " + withdrawto + " " + rewithdrawamount + ""
                    rut  =  subprocess.check_output( cmd.split(" ") )
                    cmd = "monacoin-cli move " + message.author.id + " fee " + fee + ""
                    ruta  =  subprocess.check_output( cmd.split(" ") )
                    print(rut)
                    rut = rut.decode()
                    m = "<@" + message.author.id + ">, " + rewithdrawamount + "mona has been withdrawn to " + withdrawto + ". Transaction details can be found here: https://mona.chainsight.info/tx/" + rut + "\n(message created on " + currenttime + ")"
                    await client.send_message(message.channel, m)
                    cmda = "monacoin-cli getbalance " + message.author.id + ""
                    ruta  =  subprocess.check_output( cmda.split(" ") )
                    balancea = ruta.decode()
                    if balancea <= "0":
                        defo = "0"
                        amounttosendback = float(defo) - float(balancea)
                        print("--amounttosendback--")
                        print(amounttosendback)
                        amounttosendback = str(amounttosendback)


                        cmd = "monacoin-cli move fee "  + message.author.id + " " + amounttosendback + ""
                        ruta  =  subprocess.check_output( cmd.split(" ") )
                        print(ruta)

                else:
                    m = "<@" + message.author.id + "> sorry, failed to complete your request: you do not have enogh mona for withdraw. \n please note that the minimum withdraw amount is 0.01mona.(message created on " + currenttime + ")"
                    await client.send_message(message.channel, m)
            else:
                m = "<@" + message.author.id + ">sorry, failed to complete your request: you do not have any mona at all!(message created on " + currenttime + ")"
                await client.send_message(message.channel, m)
        else:
            m = "<@" + message.author.id + "> sorry, failed to complete your request: you do not have enogh mona for withdraw. \n please note that the minimum withdraw amount is 0.01mona.(message created on " + currenttime + ")"
            await client.send_message(message.channel, m)
    if message.content.startswith("/rain"):
        cmda = "monacoin-cli getbalance " + message.author.id + ""
        ruta  =  subprocess.check_output( cmda.split(" ") )
        balancea = ruta.decode()
        if message.author.id == "326091178984603669":
            await client.add_reaction(message, '👌')
            currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
            message2 = message.content.replace('/rain ', '')
            pattern = r'([+-]?[0-9]+\.?[0-9]*)'
            raininfo = re.findall(pattern,message2)
            print("--numbertorain--")
            print(raininfo[0])
            print("--amounttorain--")
            print(raininfo[1])
            sum = float(raininfo[1]) / float(raininfo[0])
            print(sum)
            sum = str(sum)
            if balancea >= raininfo[1]:
                m = "you will rain " + sum + "mona to " + raininfo[0] + " people."
                await client.send_message(message.channel, m)
                sum = str(sum)
                numbertosend = raininfo[0]
                #sum=amount to rain for each person
                cmd = "monacoin-cli listaccounts"
                rut  =  subprocess.check_output( cmd.split(" ") )
                data = rut.decode()
                print(data[2])
                pattern = r'([+-]?[0-9]+\.?[0-9]*)'
                print(re.findall(pattern,data))
                data = re.findall(pattern,data)
                tosend = random.randrange(1, 50, 3)
                print(data[tosend])
                numbertosend = int(numbertosend)
                print ("--loop start--")
                for var in range(0, numbertosend):
                    tosend = random.randrange(1, 50, 1)
                    print("--rondomfinish--")
                    tosend = data[tosend]
                    print("--startcommand--")
                    if tosend >= "1":
                        cmd = "monacoin-cli move " + message.author.id + " " + tosend + " " + sum + ""
                        rut  =  subprocess.check_output( cmd.split(" ") )
                        print(rut)
                        m = "raining to <@" + tosend + ">.."
                        await client.send_message(message.channel, m)
                    else:
                        pass

                m = "finished rain to " + raininfo[0] + "people! total amount was " + raininfo[1] + "mona!"
                await client.send_message(message.channel, m)
                print(rut)
            else:
                m = "not enough fund.. double check amount to rain."
                await client.send_message(message.channel, m)

        else:
            m = "currently only available for admin due to some problems.I am working on this,so come back again later!"
            await client.send_message(message.channel, m)
    if message.content.startswith("/tip"):
        await client.add_reaction(message, '👌')
        currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
        message2 = message.content.replace('/tip', '')
        print (message2)
        pattern = r'([+-]?[0-9]+\.?[0-9]*)'
        print(re.findall(pattern,message2))
        tipinfo = re.findall(pattern,message2)
        print(tipinfo[0])
        print(tipinfo[1])
        cmd = "monacoin-cli getbalance " + message.author.id + ""
        rut  =  subprocess.check_output( cmd.split(" ") )
        balance = rut.decode()
        tipto = tipinfo[0]
        tipamount = tipinfo[1]
        if tipamount <= balance:
            if tipamount >= "0.0000001":
                try:
                    cmd2 = "monacoin-cli move " + message.author.id + " " + tipto + " " + tipamount + ""
                    rut2  =  subprocess.check_output( cmd2.split(" ") )
                    m = "<@" + message.author.id + "> sent " + tipamount + " mona to <@" + tipto + ">!\n(message created on " + currenttime + ")"
                    await client.send_message(message.channel, m)
                except subprocess.CalledProcessError as e:
                    eout = e.output.decode()
                    m = "<@" + message.author.id + ">, sorry, failed to complete your request: <@" + tipto + "> is not yet registered.\n(message created on " + currenttime + ")" 
                    await client.send_message(message.channel, m)
            else:
                m = "<@" + message.author.id + ">, sorry, failed to complete your request: your tip must meet the minimum of 10 watanabe (0.00000010 Mona).\n(message created on " + currenttime + ")"
                await client.send_message(message.channel, m)
        else:
            m = "<@"+ message.author.id + ">, sorry, failed to complete your request: you do not have enough Mona in your account, please double check your balance and your tip amount.\n(message created on " + currenttime + ")"
            await client.send_message(message.channel, m)
    if message.content.startswith("/admin info"):
        await client.add_reaction(message, '👌')
        currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
        cmd = "monacoin-cli getinfo"
        rut  =  subprocess.check_output( cmd.split(" ") )
        cmd2 = "monacoin-cli getbalance"
        rut2 = subprocess.check_output( cmd2.split(" "))
        cmd3 = "monacoin-cli listaccounts"
        rut3 = subprocess.check_output( cmd3.split(" "))
        cmd4 = "monacoin-cli listtransactions"
        rut4 = subprocess.check_output( cmd4.split(" "))
        getinfo = rut.decode()
        getbalance = rut2.decode()
        listaccounts = rut3.decode()
        listtransactions = rut4.decode()
        if message.author.id == "326091178984603669":
            m = "Verfifying.. wait a monemt"
            await client.send_message(message.channel, m)
            m = "Successfully verified you as an admin, here is the info you requested:"
            await client.send_message(message.channel, m)
            m = "```getinfo result: " + getinfo + "\n```"
            await client.send_message(message.channel, m)
            time.sleep(1)
            m = "```getbalance result: " + getbalance + "\n```"
            await client.send_message(message.channel, m)
            time.sleep(1)
            m = "```listaccounts result: " + listaccounts + "\n```"
            await client.send_message(message.channel, m)
            time.sleep(1)
            m = "```listtransactions result: " + listtransactions +"\n ```"
            await client.send_message(message.channel, m)
            time.sleep(1)
        else:
            m = "Haha, you don't have permission to do that! Your request has been logged and reported to the admin! (but the admin probably won't care about it, so don't worry.)"
            await client.send_message(message.channel, m)
    if message.content.startswith("/adminc"):
        if message.author.id == "326091178984603669":
            await client.add_reaction(message, '👌')
            message2 = message.content.replace('/adminc', '')
            print(message2)
            cmd = "monacoin-cli" + message2 + ""
            rut = subprocess.check_output( cmd.split(" "))
            result = rut.decode()
            await client.send_message(message.channel, result)
        else:
            m = "sorry, but you are not allowed to do that!"
            await client.send_message(message.channel, m)
    if message.content.startswith('/members'):
        await client.add_reaction(message, '👌')
        for server in client.servers:
            for member in server.members.id:
                print (member)
                list_of_ids = [m.id  for m in server.members]
                print(list_of_ids)
    if message.content.startswith('/adminregister'):
        await client.add_reaction(message, '👌')
        if message.author.id == "326091178984603669":
            message2 = message.content.replace('/adminregister', '')
            message3 = message2.replace(' ', '')
            print(message3)
            cmd = "monacoin-cli getnewaddress " + message3 + ""
            rut = subprocess.check_output( cmd.split(" "))
            address = rut.decode()
            m = "issued account for <@" + message3 + ">. address is " + address + "."
            await client.send_message(message.channel, m)
        else:
            m = "sorry, but you are not allowed to do that!"
            await client.send_message(message.channel, m)
    if message.content.startswith('/adminbalance'):
        await client.add_reaction(message, '👌')
        if message.author.id == "326091178984603669":
            message2 = message.content.replace('/adminbalance', '')
            message3 = message2.replace(' ', '')
            print(message3)
            cmd = "monacoin-cli getbalance " + message3 + ""
            rut = subprocess.check_output( cmd.split(" "))
            balance = rut.decode()
            m = "<@" + message3 + "> 's balance are " + balance + "mona."
            await client.send_message(message.channel, m)
        else:
            m = "sorry, but you are not arrowed to do that!"
            await client.send_message(message.channel, m)
    if message.content.startswith("/image"):
        await client.add_reaction(message, '👌')
        with open('../image.jpg', 'rb') as f:
            await client.send_file(message.channel, f)

    if message.content.startswith("/help"):
        await client.add_reaction(message, '👌')
        currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
        m = "```----------------------------------------------------------------------------------- \
        \n /help - ヘルプを表示します <Show help> \
        \n /register - あなたの財布を新しく作成します <Create your address> \
        \n /balance - あなたの現在の残高を表示します <Show your current balance> \
        \n /deposit - あなたの所有しているアドレスを一覧表示します <List address you currently have> \
        \n /list - あなたの所有しているアドレスを一覧表示します <List address you currently have (same as /deposit)>\
        \n /withdrawall - あなたの持っているmonaすべてを指定されたアドレスに送金します <Send all of your mona to specifyed address> \
        \n /tip - 指定されたmonaを指定されたユーザーに送ります <Tip specified amount of mona to specified user> \
        \n /withdraw - 指定されたmonaを指定されたアドレスに送ります <Withdraw specified amount of mona to specified address> \
        \n /rain - 指定された金額のmonaをランダムに配ります。<Tip specified amount to rondom people. you can chose the number of people to tip> (Currently for admin due to some problem.)\
        \n /admin info - 管理者専用コマンド。管理者がすぐに状況確認できるように作成しました <Admin only command>\
        \n ---使い方 <Usage>---\
        \n /withdrawall <送金先アドレス>\
        \n /withdrawall <address to send> \
        \n /withdraw <金額> <送金先アドレス> \
        \n /withdraw <amount to withdraw> <address to send> \
        \n /tip <ユーザー> <金額> <任意のコメント> \
        \n /tip <User to send mona> <amoun to tip> <comment (optional>> \
        \n /rain <人数> <合計金額> \
        \n /rain <number of people to tip> <total amount to tip> \
        \n Created message at " + currenttime + "```"
        await client.send_message(message.channel, m)
    
    if message.content.startswith("/hello"):
        currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
        m = "こんにちは! <@" + message.author.id + "> さん！" 
        await client.send_message(message.channel, m)
        await client.add_reaction(message, '👌')

    if message.content.startswith("/credit"):
        await client.add_reaction(message, '👌')
        currenttime = (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
        m = "```-----------------------------------------------------------------------------------  \
        \n このプログラムは以下の方たちの協力によって完成しました。この場にて改めて感謝します。(敬称略) \
        \n ---開発、制作--- \
        \n raspi0124 \
        \n ---開発協力--- \
        \n はるまど(Gitlabの提供。勝手にモナオクのgitlab使っちゃってすみませんm(_ _)m) \
        \n kakarichyo(クローズドアルファにおけるテスト) \
        \n ポテト(クローズドアルファにおけるテスト) \
        \n MGQ(アドバイス) \
        \n Discordサーバー 「MGQ club」のみなさん(テスト全般) \
        \n W.S Wsans(W.S 笑サンズ) (Discord.pyについてのアドバイス) \
        \n ぱい (Discord.pyについてのアドバイス \
        \n Monageと遊ぶ鯖に参加してくださった皆さん(テスト) \
        \n lae(アドバイス,英語文法監修) \
        \n 両親(匿名にしておきます) \
        \n ---使用させていただいたプログラム--- \
        \n Python \
        \n Discord.py \
        \n Sublime Text3 \
        \n Nano \
        \n Gitlab \
        \n Ubuntu \
        \n ---その他--- \
        \n 脇山P (WordPressプラグイン、monage作成の際に頂いたmonaをVPS代にありがたくつぎ込ませてもらっています。) \n Created message at " + currenttime + "\
        \n ----------------------------------------------------------------------------------- \
        ```"
        await client.send_message(message.channel, m)
            
client.run("NDA5MDkwMTE4OTU2MDg5MzQ0.DVZidQ.1MTSYLrrPL2bNeLMXFVQDPc25Mg")


# https://qiita.com/PinappleHunter/items/af4ccdbb04727437477f
# https://qiita.com/komeiy/items/d6b5f25bf1778fa10e21
