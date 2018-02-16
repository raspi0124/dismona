import discord
import subprocess
import re
# Python 3.5.2 にて動作を確認
# MySQLdb をインポート
import MySQLdb
client = discord.Client()

# データベース接続とカーソル生成
# 接続情報はダミーです。お手元の環境にあわせてください。
connection = MySQLdb.connect(
    host='localhost', user='root', passwd='laksjd', db='dismona', charset='utf8')
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS dismona.id (id VARCHAR(20), address VARCHAR(50));")


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

INDB = "aaa"

#message.author.name がユーザー名

@client.event
async def on_message(message):
    # 「/register」で始まるか調べる
    if message.content.startswith("/register"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author.name:
            # メッセージを書きます
            if message.author.name != INDB:
                m = "<@" + message.author.id + "> さんのアカウントを作成しますね！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
                await client.send_message(message.channel, m)
                cmd = "monacoin-cli getnewaddress " + message.author.id + ""
                rut  =  subprocess.check_output( cmd.split(" ") )
                print ('Creating <' + message.author.id + ">'s account.. user ID ")
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
                cursor.execute("INSERT INTO dismona.id(id, address) VALUES ('" + message.author.id + "', '" + resultmore5 + "' )")
                print ("---4---")
                print ('----MYSQL COMMAND START----')
                print ("INSERT INTO dismona.id(id, address) VALUES ('" + message.author.id + "', '" + resultmore5 + "' )")
                print ('----MYSQL COMMAND END----')
                print ("---5---")
                m = "<@"+ message.author.id + "> ,Created your account succefully! your address is " + resultmore5 + " enjoy!"
                print ("---6---")
                await client.send_message(message.channel, m)

    if message.content.startswith("/balance"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author.name:
            # メッセージを書きます
                m = "<@" + message.author.id + "> さんの残高チェック中.."
            # メッセージが送られてきたチャンネルへメッセージを送ります
                await client.send_message(message.channel, m)
                cmd = "monacoin-cli getbalance " + message.author.id + ""
                rut  =  subprocess.check_output( cmd.split(" ") )
                balance = rut.decode()
                m = "<@"+ message.author.id + ">"", your balance is " + balance + " mona!"
                print ("---6---")
                await client.send_message(message.channel, m)
    if message.content.startswith("/deposit"):
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
                m = "<@"+ message.author.id + ">,your address is" + address3 + ""
                await client.send_message(message.channel, m)
    if message.content.startswith("/withdrawall"):
        message2 = message.content.replace('/withdrawall', '')
        message3 = message2.replace(' ', '')
        print (message3)
        m ="<@" +message.author.id + "> prepareing for withdraw.. please wait"
        m = "<@" + message.author.id + "> is withdrawalling to " + message3 +""
        await client.send_message(message.channel, m)
        await client.send_message(message.channel, m)
        cmda = "monacoin-cli getbalance " + message.author.id + ""
        ruta  =  subprocess.check_output( cmda.split(" ") )
        balancea = rut.decode()
        cmd = "monacoin-cli sendfrom " + message.author.id + " " + message3 + " " + balance +""
        rut  =  subprocess.check_output( cmd.split(" ") )
        withdrawalldata = rut.decode()
        m = "<@"+ message.author.id + ">,we've just withdrawed all mona you have, to " + address3 + " , and here are some details" + withdrawalldata + ""
        await client.send_message(message.channel, m)
        # メッセージが送られてきたチャンネルへメッセージを送ります
        

            
            
client.run("NDA5MDkwMTE4OTU2MDg5MzQ0.DVZidQ.1MTSYLrrPL2bNeLMXFVQDPc25Mg")

cursor = conn.cursor()


# https://qiita.com/PinappleHunter/items/af4ccdbb04727437477f
# https://qiita.com/komeiy/items/d6b5f25bf1778fa10e21
#