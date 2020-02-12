This script does not check for the correct of the ip or for the presence of the ip / broken_ip file because this script is not intended for "ordinary" users :)
## Details what he does:
This script takes the ip list from the ip.txt file and checks each of them with a ping. If there is no ping, the ip is written to the broken_ip.txt file and a message is sent that the ip stopped working, if the ip later worked and it was in the broken_ip.txt file, a message is sent that the ip has earned and the ip is deleted from this file. 
### This script is registered in crontab with the condition
`` ``
0/30 * * * *
`` ``
the script is activated every 30 minutes. 
If you want to run my script, you will need to install requirements
`` ``
pip install -r requirements.txt
`` ``
and write your token, chat_id from your Telegram bot and file paths ip.txt, broken_ip.txt to the config.py