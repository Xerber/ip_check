from time import sleep
from pythonping import ping
from telebot import TeleBot
from config import token, chat_id, file1, file2

#variables
UpIp = ''
DownIp = ''

#main program
bot = TeleBot(token)
with open(file2, 'r') as f2:
    broken = f2.readlines()
    broken = list(map(lambda s: s.strip(), broken))
with open(file1,'r') as f:
    x=f.readlines()
    for ip in x:
        response_list=ping(ip,verbose=False,count=5,timeout=1)
        if response_list._responses[0].success:
            if ip.strip("\n") in broken:
                UpIp+=ip+'\n'
                with open(file2, 'w') as f3:
                    for line in broken:
                        if line.strip("\n") != ip.strip("\n"):
                            f3.write(line)
            else:
                pass
        else:
            if ip not in broken:
                DownIp+=ip
                with open(file2, 'a+') as f3:
                    f3.write(ip)
            else:
                pass

def telesend(list_ip,message):
    if len(list_ip) is not 0:
        bot.send_message(chat_id,message)

telesend(UpIp,'#cam\nis up\n'+UpIp)
telesend(DownIp,'#cam\nis down\n'+DownIp)