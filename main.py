import discord
import subprocess
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
                m = "@" + message.author.name + " さんのアカウントを作成しますね！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
                await client.send_message(message.channel, m)
                #DB
                query = """INSERT INTO dismona.id(id,address)
                VALUES 
                """
                value1 = ( 
                values = "address" )
            # subprocess.check_output(["monacoin-cli getaddressesbyaccount" + message.author.name + ])
                print ('Creating ' + message.author.name + "'s account..")
                #cursor.execute("insert into dismona.id(id,address) values('message_author', address);")
                #cursor.execute("INSERT INTO 'dismona.id'('id', 'address') VALUES (message_author,address);")
                print ('----MYSQL COMMAND START----')
                print (query, value1, message.author.name, values)
                print ('----MYSQL COMMAND END----')
                cursor.execute(query, values)
                m = "Created your account succefully! your address is <address>enjoy!"
                await client.send_message(message.channel, m)

            else:
                m = "すみませんがそのアカウント名はすでにこのシステムに登録されているようです。。"
                await client.send_message(message.channel, m)
                print ("failed to create" + message.author.name + "'s account..")
                
            
            
client.run("NDA5MDkwMTE4OTU2MDg5MzQ0.DVZidQ.1MTSYLrrPL2bNeLMXFVQDPc25Mg")

cursor = conn.cursor()


# https://qiita.com/PinappleHunter/items/af4ccdbb04727437477f
# https://qiita.com/komeiy/items/d6b5f25bf1778fa10e21